"""Verifica a integridade dos artefatos de instanciação, não a ontologia.

Executar com Python 3, sem dependências: python avaliacao/verificar-dados.py
Não usa assert: as verificações também funcionam com python -O.
Não executa inferência, consulta SPARQL, análise OntoUML ou validação jurídica.
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path


def exigir(condicao, mensagem):
    if not condicao:
        raise ValueError(mensagem)


def objeto_sem_chaves_repetidas(pares):
    objeto = {}
    for chave, valor in pares:
        exigir(chave not in objeto, f"Chave JSON repetida: {chave}")
        objeto[chave] = valor
    return objeto


def verificar():
    raiz = Path(__file__).resolve().parent.parent
    dados = json.loads(
        (raiz / "avaliacao" / "dados-simulados.json").read_text(encoding="utf-8"),
        object_pairs_hook=objeto_sem_chaves_repetidas,
    )
    texto = (raiz / "tcc-jec.md").read_text(encoding="utf-8")
    exigir(dados["metadados"]["dados_inteiramente_ficticios"] is True,
           "Os dados precisam estar identificados como fictícios.")

    categorias = dados["categorias"]
    classes = [classe for grupo in categorias.values() for classe in grupo]
    exigir(len(classes) == len(set(classes)), "Classe repetida no catálogo de categorias.")
    exigir(all(classe in texto for classe in classes),
           "Uma classe do catálogo não é encontrada no texto da monografia.")
    classes = set(classes)
    predicados = set(dados["relacoes_do_modelo"])

    def categoria(instancia, nome):
        return bool(set(instancia["classes"]) & set(categorias[nome]))

    ids_globais = set()

    def registrar(identificador):
        exigir(identificador not in ids_globais, f"Identificador repetido: {identificador}")
        ids_globais.add(identificador)

    premissas = {}
    for premissa in dados["premissas_externas"]:
        registrar(premissa["id"])
        exigir(bool(premissa["fonte"]) and bool(premissa["descricao"]),
               f"Premissa sem fonte/descrição: {premissa['id']}")
        premissas[premissa["id"]] = premissa

    cenarios = {}
    total_instancias = 0
    total_relacoes = 0
    total_recortes = 0
    grupos_exclusivos_no_recorte = [
        {"Obrigação Cumprida", "Obrigação Parcialmente Cumprida", "Obrigação Não Cumprida"},
        {"Provas Suficientes", "Provas Insuficientes"},
        {"Conciliação Realizada", "Conciliação Frustrada"},
        {"Audiência Designada", "Audiência Dispensada"},
        {"Apto a Julgamento", "Não Apto a Julgamento"},
        {"Cabível no JEF", "Não Cabível no JEF"},
    ]
    particoes_resultado = {
        "Resultado da Determinação de Audiência": {"Audiência Designada", "Audiência Dispensada"},
        "Resultado da Análise de Cabimento": {"Cabível no JEF", "Não Cabível no JEF"},
        "Resultado da Análise Probatória": {"Provas Suficientes", "Provas Insuficientes"},
    }

    for cenario in dados["cenarios"]:
        cid = cenario["id"]
        registrar(cid)
        cenarios[cid] = cenario
        instancias = cenario["instancias"]
        exigir(bool(instancias), f"Cenário vazio: {cid}")
        for iid, instancia in instancias.items():
            registrar(iid)
            exigir(iid.startswith(cid + "-"), f"Indivíduo fora do contexto: {iid}")
            exigir(bool(instancia["classes"]), f"Indivíduo sem classificação: {iid}")
            exigir(set(instancia["classes"]) <= classes, f"Classe não catalogada: {iid}")
            exigir(len(instancia["classes"]) == len(set(instancia["classes"])),
                   f"Classificação repetida: {iid}")
            exigir(type(instancia["marco"]) is int and instancia["marco"] >= 0,
                   f"Marco inválido: {iid}")
            tipos = set(instancia["classes"])
            for geral, alternativas in particoes_resultado.items():
                if geral in tipos or tipos & alternativas:
                    exigir(geral in tipos and len(tipos & alternativas) == 1,
                           f"Resultado sem classificação única na partição declarada: {iid}")
            exigir(not ({"Cabível no JEF", "Não Cabível no JEF"} & tipos
                        and "Processo Judicial Federal" in tipos),
                   f"Resultado de cabimento confundido com o processo: {iid}")

        processo = cenario["processo"]
        if processo is not None:
            exigir(processo in instancias, f"Processo não encontrado: {cid}")
            exigir("Processo Judicial Federal" in instancias[processo]["classes"],
                   f"Classificação do processo ausente: {cid}")
        else:
            exigir(not any("Processo Judicial Federal" in i["classes"] for i in instancias.values()),
                   f"Consulta pré-processual contém processo: {cid}")
            exigir(not any(set(i["classes"]) & {"Demandante", "Demandado"} for i in instancias.values()),
                   f"Consulta pré-processual já atribui papéis de parte: {cid}")
            exigir(any("Pretensão Jurídica" in i["classes"] for i in instancias.values()),
                   f"Consulta pré-processual sem Pretensão Jurídica: {cid}")
            exigir(not any("Demanda" in i["classes"] for i in instancias.values()),
                   f"Consulta pré-processual confundida com demanda judicial: {cid}")

        vistas = set()
        for relacao in cenario["relacoes"]:
            exigir(len(relacao) == 3, f"Relação malformada: {cid}: {relacao}")
            origem, predicado, destino = relacao
            exigir(origem in instancias and destino in instancias,
                   f"Referência não resolvida: {cid}: {relacao}")
            exigir(predicado in predicados, f"Predicado não catalogado: {predicado}")
            exigir(tuple(relacao) not in vistas, f"Relação repetida: {relacao}")
            vistas.add(tuple(relacao))
            a, b = instancias[origem], instancias[destino]
            if predicado == "brings_about":
                exigir(categoria(a, "evento") and categoria(b, "situacao"),
                       f"brings_about deve relacionar evento e situação: {relacao}")
                exigir(a["marco"] <= b["marco"], f"Resultado anterior ao evento: {relacao}")
            elif predicado == "triggers":
                exigir(categoria(a, "situacao") and categoria(b, "evento"),
                       f"triggers deve relacionar situação e evento: {relacao}")
                exigir(a["marco"] <= b["marco"], f"Evento anterior à situação: {relacao}")
            elif predicado == "promove":
                exigir("Audiência Designada" in a["classes"]
                       and "Audiência de Conciliação" in b["classes"],
                       f"Promove deve relacionar designação e audiência: {relacao}")
                exigir(a["marco"] <= b["marco"], f"Audiência anterior à designação: {relacao}")
            elif predicado == "historical_dependence":
                exigir(categoria(a, "evento") and categoria(b, "evento"),
                       f"Dependência deve relacionar eventos: {relacao}")
                exigir(b["marco"] <= a["marco"], f"Antecedente posterior ao dependente: {relacao}")
            elif predicado == "creation":
                exigir(categoria(a, "evento") and not categoria(b, "evento")
                       and not categoria(b, "situacao"), f"Criação mal tipada no ensaio: {relacao}")
                exigir(a["marco"] == b["marco"], f"Criação com marcos distintos: {relacao}")
            elif predicado == "participa_de":
                exigir(categoria(b, "evento") and not categoria(a, "evento")
                       and not categoria(a, "situacao"), f"Participação mal tipada: {relacao}")
                exigir(a["marco"] <= b["marco"], f"Participante ainda inexistente: {relacao}")
            elif predicado == "media":
                exigir(categoria(a, "relator"), f"Origem da mediação não é relator: {relacao}")
            elif predicado == "associa_nao_aptidao":
                exigir("Provas Insuficientes" in a["classes"]
                       and "Não Apto a Julgamento" in b["classes"],
                       f"Associação de não aptidão fora do fragmento desenhado: {relacao}")
                exigir(a["marco"] <= b["marco"], f"Não aptidão anterior à avaliação: {relacao}")
            elif predicado == "possibilita":
                exigir("Provas Suficientes" in a["classes"] and "Apto a Julgamento" in b["classes"],
                       f"Possibilita fora do fragmento de aptidão: {relacao}")
                exigir(a["marco"] <= b["marco"], f"Aptidão anterior à suficiência: {relacao}")

        for iid, instancia in instancias.items():
            portadores = {destino for origem, predicado, destino in cenario["relacoes"]
                          if origem == iid and predicado == "caracteriza"}
            exigir(len(portadores) <= 1, f"Uma propriedade intrínseca com portadores distintos: {iid}")
            if "Determinação de Audiência" in instancia["classes"]:
                resultados = {destino for origem, predicado, destino in cenario["relacoes"]
                              if origem == iid and predicado == "brings_about"
                              and "Resultado da Determinação de Audiência" in instancias[destino]["classes"]}
                exigir(len(resultados) <= 1, f"Determinação com mais de um resultado: {iid}")
            if "Análise de Cabimento no JEF" in instancia["classes"]:
                entradas = [instancias[origem] for origem, predicado, destino in cenario["relacoes"]
                            if destino == iid and predicado == "participa_de"]
                for classe in ("Organização Federal", "Causa de Pedir", "Valor da Causa"):
                    exigir(any(classe in entrada["classes"] for entrada in entradas),
                           f"Entrada de cabimento ausente ({classe}): {iid}")
                exigir(any(any(classe.startswith("Pedido") for classe in entrada["classes"])
                           for entrada in entradas), f"Análise sem pedido: {iid}")
                exigir(any(destino == iid and predicado == "regula"
                           and "Regra de Competência" in instancias[origem]["classes"]
                           for origem, predicado, destino in cenario["relacoes"]),
                       f"Análise sem regra de competência: {iid}")
                resultados = [destino for origem, predicado, destino in cenario["relacoes"]
                              if origem == iid and predicado == "brings_about"
                              and "Resultado da Análise de Cabimento" in instancias[destino]["classes"]]
                exigir(len(resultados) == 1,
                       f"A análise concluída do ensaio deve ter um resultado informado: {iid}")

        recortes = {}
        for recorte in cenario["recortes"]:
            rid = recorte["id"]
            registrar(rid)
            exigir(rid.startswith(cid + "-"), f"Recorte fora do contexto: {rid}")
            exigir(type(recorte["marco"]) is int and recorte["marco"] >= 0,
                   f"Marco de recorte inválido: {rid}")
            recortes[rid] = recorte
            tipos_no_recorte = set()
            for sid in recorte["situacoes"]:
                exigir(sid in instancias, f"Situação inexistente: {rid}: {sid}")
                exigir(categoria(instancias[sid], "situacao"), f"Não é situação: {rid}: {sid}")
                exigir(instancias[sid]["marco"] <= recorte["marco"],
                       f"Situação futura usada no recorte: {rid}: {sid}")
                tipos_no_recorte.update(instancias[sid]["classes"])
            # Os cenários presentes possuem no máximo uma obrigação e uma pretensão
            # e selecionam uma avaliação atual por dimensão no recorte.
            # Este teste de recorte não implementa a semântica geral de disjunção.
            for grupo in grupos_exclusivos_no_recorte:
                exigir(len(tipos_no_recorte & grupo) <= 1,
                       f"Estados incompatíveis no mesmo recorte: {rid}")

        for anotacao in cenario["anotacoes"]:
            registrar(anotacao["id"])
            exigir(anotacao["id"].startswith(cid + "-"), "Anotação fora do contexto.")
            exigir(bool(anotacao["descricao"]), "Anotação sem descrição.")
            for referencia in anotacao["referencias"]:
                exigir(referencia in instancias, f"Referência de anotação ausente: {referencia}")
                exigir(instancias[referencia]["marco"] <= anotacao["marco"],
                       f"Anotação usa fato futuro: {anotacao['id']}: {referencia}")

        for pagamento in cenario.get("pagamentos_simulados", []):
            exigir(pagamento["recorte"] in recortes, "Recorte de pagamento inexistente.")
            exigir(pagamento["obrigacao"] in instancias, "Obrigação do pagamento inexistente.")
            devido = pagamento["devido_centavos"]
            pago = pagamento["pago_acumulado_centavos"]
            saldo = pagamento["saldo_centavos"]
            exigir(all(type(v) is int and v >= 0 for v in (devido, pago, saldo)),
                   "Valores monetários devem ser inteiros não negativos em centavos.")
            exigir(devido == pago + saldo, "Pagamento e saldo não conciliam.")
            tipos = {tipo for sid in recortes[pagamento["recorte"]]["situacoes"]
                     for tipo in instancias[sid]["classes"]}
            esperado = "Obrigação Cumprida" if saldo == 0 else "Obrigação Parcialmente Cumprida"
            exigir(esperado in tipos, "Pagamento não coincide com a situação declarada.")

        total_instancias += len(instancias)
        total_relacoes += len(cenario["relacoes"])
        total_recortes += len(recortes)

    qcs_originais = [int(n) for n in re.findall(r"^QC(\d+)\. ", texto, re.MULTILINE)]
    exigir(qcs_originais == list(range(1, 39)), "A lista original de QCs não contém QC1 a QC38 em ordem.")
    respostas = dados["respostas_esperadas"]
    exigir([r["qc"] for r in respostas] == list(range(1, 39)),
           "As respostas devem cobrir QC1 a QC38, sem repetição e em ordem.")
    for resposta in respostas:
        qc = resposta["qc"]
        exigir(resposta["suporte"] in {"D", "P", "N"}, f"Suporte inválido: QC{qc}")
        exigir(bool(resposta["resposta"]), f"Resposta vazia: QC{qc}")
        exigir(resposta["cenario"] in cenarios, f"Cenário não encontrado: QC{qc}")
        cenario = cenarios[resposta["cenario"]]
        recortes = {r["id"]: r for r in cenario["recortes"]}
        exigir(resposta["recorte"] in recortes, f"Recorte não encontrado: QC{qc}")
        limite = recortes[resposta["recorte"]]["marco"]
        for referencia in resposta["evidencias"]:
            exigir(referencia in cenario["instancias"], f"Evidência inexistente: QC{qc}: {referencia}")
            exigir(cenario["instancias"][referencia]["marco"] <= limite,
                   f"Evidência futura usada: QC{qc}: {referencia}")
        anotacoes = {a["id"]: a for a in cenario["anotacoes"]}
        for referencia in resposta["anotacoes"]:
            exigir(referencia in anotacoes, f"Anotação não encontrada: QC{qc}: {referencia}")
            exigir(anotacoes[referencia]["marco"] <= limite,
                   f"Anotação futura usada: QC{qc}: {referencia}")
        exigir(set(resposta["premissas"]) <= set(premissas), f"Premissa não encontrada: QC{qc}")

    titulo_matriz = re.search(
        r"(?m)^#{1,6}\s+4\.4\.\d+\s+Matriz de rastreabilidade das 38 QCs[^\n]*\n", texto
    )
    exigir(titulo_matriz is not None, "Seção da matriz de rastreabilidade não encontrada.")
    secao_matriz = texto[titulo_matriz.end():]
    proximo_titulo = re.search(r"(?m)^#{1,6}\s+", secao_matriz)
    if proximo_titulo:
        secao_matriz = secao_matriz[:proximo_titulo.start()]
    linhas_matriz = re.findall(
        r"^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$",
        secao_matriz,
        re.MULTILINE,
    )
    exigir(len(linhas_matriz) == 38, "A matriz no TCC deve conter exatamente 38 linhas de QCs.")
    exigir([int(linha[0]) for linha in linhas_matriz] == list(range(1, 39)),
           "A matriz deve usar apenas os números de 1 a 38, sem repetição e em ordem.")
    perguntas = {int(n): pergunta.strip() for n, pergunta in
                 re.findall(r"^QC(\d+)\. (.+)$", texto, re.MULTILINE)}
    for numero, pergunta, elementos, localizacao in linhas_matriz:
        exigir(pergunta.strip() == perguntas[int(numero)],
               f"Pergunta da matriz diverge da formulação original: QC{numero}")
        exigir(">" in elementos, f"Percurso sem separador >: QC{numero}")
        exigir(bool(localizacao.strip()), f"Localização ausente: QC{numero}")

    guia = (raiz / "avaliacao" / "instanciacoes-simuladas.md").read_text(encoding="utf-8")
    linhas_suporte = re.findall(
        r"^\| QC(\d+) \| ([^|]+) \| [^|]+ \| ([DPN]) \|$", guia, re.MULTILINE
    )
    exigir(len(linhas_suporte) == 38 and len({n for n, _, _ in linhas_suporte}) == 38,
           "O guia deve preservar as classificações de suporte das 38 QCs.")
    exigir({int(n): suporte for n, _, suporte in linhas_suporte}
           == {r["qc"]: r["suporte"] for r in respostas},
           "O guia de instanciações e o JSON divergem na classificação de suporte.")
    exigir({int(n): recorte.strip() for n, recorte, _ in linhas_suporte}
           == {r["qc"]: r["recorte"] for r in respostas},
           "O guia de instanciações e o JSON divergem nos recortes das QCs.")

    contagem = Counter(r["suporte"] for r in respostas)
    print("Integridade dos artefatos: OK")
    print(f"Cenários: {len(cenarios)}; indivíduos: {total_instancias}; "
          f"relações declaradas: {total_relacoes}; recortes: {total_recortes}.")
    print("Rastreabilidade: 38 QCs com evidências referenciadas e respostas esperadas.")
    print(f"Suporte documental: D={contagem['D']}; P={contagem['P']}; N={contagem['N']}.")
    print("NÃO foram executados 38 testes de inferência. NÃO é validação formal ou jurídica da ontologia.")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        verificar()
    except (ValueError, KeyError, TypeError, OSError) as erro:
        print(f"Falha na integridade dos artefatos: {erro}", file=sys.stderr)
        sys.exit(1)
