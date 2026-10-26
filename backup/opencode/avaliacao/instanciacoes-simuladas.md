# Instanciações simuladas e respostas esperadas das 38 QCs

## 1. Finalidade e arquivos

Este material documenta uma **instanciação conceitual parcial com dados inteiramente fictícios** da ontologia apresentada em `tcc-jec.md`. Não utiliza processos reais nem representa orientação jurídica para um caso concreto.

| Arquivo | Conteúdo |
| --- | --- |
| [`../tcc-jec.md`](../tcc-jec.md), Seções 3.8 e 4.4 | Procedimento de avaliação; matriz com número e pergunta na mesma coluna, classes envolvidas, percurso descrito por extenso e localização; cenários e síntese das lacunas em seções próprias. |
| [`dados-simulados.json`](dados-simulados.json) | Inventário de indivíduos, classificações, relações, recortes, anotações, premissas e 38 respostas esperadas. É a fonte dos identificadores deste guia. |
| [`verificar-dados.py`](verificar-dados.py) | Conferência de integridade dos artefatos, sem inferência ontológica ou decisão jurídica. |

**Não confundir:** rastrear 38 questões não significa demonstrar atendimento integral às 38 questões. A revisão atual considera Conciliação, Análise Probatória e Julgamento e o novo diagrama Análise de Cabimento no JEF. Permanecem 16 QCs com suporte descritivo direto e 22 com suporte parcial: os novos resultados são representáveis, mas suas condições jurídicas não são automaticamente executadas. A classificação resulta de inspeção documental, não de um reasoner.

O conjunto atualizado registra **169 indivíduos, 190 relações declaradas e 13 recortes em seis cenários**, na versão 1.2 do JSON. Esses números descrevem os dados simulados, não o número de classes ou termos da ontologia. As fontes imediatas são Conciliação, Análise Probatória e Julgamento e Análise de Cabimento no JEF. Os PNGs e o PDF não foram modificados nesta revisão.

## 2. Convenções de leitura

- **Identificadores:** `C1-AUT` identifica a pessoa autora em C1; `C1-REP-A` identifica uma relação de representação; `C1-TF` identifica um recorte de avaliação. São códigos locais, não números CNJ.
- **Identidade e papel:** um único indivíduo pode receber classificações como `Pessoa` e `Pessoa Física Autora`. Não se cria outra pessoa para representar seu papel. Diferentes códigos de cenários independentes não denotam a mesma entidade, salvo indicação explícita; há apenas uma referência à União, em C3.
- **Tempo:** `marco` é um ordinal local ao cenário. Igualdade de marco não especifica simultaneidade física nem identidade de eventos; indica somente a mesma etapa agregada da simulação. Os ordinais não representam dias ou datas.
- **Recorte:** as situações listadas em um recorte foram selecionadas como vigentes para a leitura do caso. Situações históricas que permanecem no inventário não são automaticamente estados atuais.
- **Evidência:** uma resposta aponta para indivíduos existentes no inventário. Evidências que só surgem depois do recorte não podem ser utilizadas para respondê-la.
- **Anotação:** contexto do processo, prioridade do pedido, valores literais, completude e agendamento são informações auxiliares identificadas, não atributos ou relações silenciosamente adicionados aos diagramas.
- **Resultado e portador:** Cabível no JEF é situação, não o papel Processo Cabível no JEF. Pretensão Jurídica é distinta de Demanda. C1-VAL-PRET e C1-VAL têm valor literal igual, mas são propriedades de portadores distintos.
- **Premissa jurídica externa:** informação normativa usada para contextualizar o exemplo, sem presumir que já exista um axioma executável correspondente na ontologia.
- **Fragmento:** as classificações e relações são seletivas. Não se pretende completar todas as mediações, propriedades, cardinalidades e generalizações de uma população integral.
- **Categorias do JSON:** `agente`, `documento`, `relator`, `evento`, `situacao` e `outro` são grupos auxiliares de conferência do ensaio, não um novo metamodelo nem substitutos dos estereótipos OntoUML.
- **Normalização de grafia:** utilizam-se `Processo Previdenciário`, `Processo Indenizatório` e `Conciliação Frustrada`, registrando no JSON os rótulos gráficos correspondentes com erros de redação. Os PNGs não foram alterados.

As relações são triplas `[origem, relação, destino]`. `possui_demanda`, por exemplo, distingue lexicalmente a associação `possui` entre processo e demanda de outra associação de mesmo nome entre demanda e pedido. Isso não acrescenta uma associação ausente. O catálogo `relacoes_do_modelo` indica o significado e as figuras de origem de cada nome utilizado.

## 3. Cenários

### C1 — Pessoa física, autarquia e obrigação de fazer

Pessoa Alfa propõe demanda previdenciária contra a Autarquia Previdenciária Simulada Alfa, pedindo implantação de benefício simulado. Há um pedido de tutela provisória separado, **sem simulação de decisão que o defira**. O valor da causa é informado como 30 salários mínimos, sem conversão em reais. Matéria não excluída e demais condições de cabimento são premissas positivas estipuladas, não conclusões obtidas do valor.

| Grupo | Instâncias principais |
| --- | --- |
| Partes | `C1-AUT`: Pessoa/Pessoa Física Autora/Demandante; `C1-REU`: Organização/Autarquia Federal/Demandado. |
| Representação | `C1-ADV`, `C1-PF`; relações `C1-REP-A` e `C1-REP-R`. |
| Auxiliares e testemunha | `C1-PER`, `C1-TEST`, `C1-CONC` e `C1-SERV`. |
| Processo e competência | `C1-PROC`, `C1-RJP`, `C1-JEF`, `C1-COMP`, `C1-REG-COMP`, `C1-PODER`. |
| Determinação da audiência | `C1-DETERMINAR-AUD` produz `C1-AUD-DESIGNADA`, que promove `C1-AUD`. |
| Pretensão e análise de cabimento | `C1-PRET`, `C1-VAL-PRET`, `C1-ANALISAR-CAB` e `C1-CABIVEL`; participação de organização, pedidos, causa e valor, com regra reguladora. |
| Demanda | `C1-DEM`, `C1-CAUSA`, `C1-VAL`, `C1-PED` e `C1-TUT`; não se presume uma relação de transformação entre a pretensão e a demanda. |
| Petição e instrução documental | `C1-PET`, `C1-INI`, `C1-INSTR` e `C1-DOC-ADM`. |
| Provas | `C1-PERICIA` cria `C1-LAUDO`; `C1-OITIVA` produz `C1-TEST-COLHIDO`. Há juntadas distintas do documento administrativo e do laudo. |
| Decisão e obrigação | `C1-JULGAR` cria `C1-SENT`; esta impõe `C1-OBR`, composta por `C1-DIREITO` e `C1-DEVER`. |
| Encerramento | `C1-SEM-RECURSO`, `C1-TRANSITO`, `C1-TRANSITADA`, `C1-CUMPRIDA`, `C1-CONCLUIDO` e `C1-ARQUIVADO`. |

**Recortes:** C1-TI, após citação; C1-TP, após instrução e análise; C1-TF, após satisfação e arquivamento.

Exemplos de relações declaradas:

```text
C1-REP-A   --media-->          C1-AUT
C1-REP-A   --media-->          C1-ADV
C1-PROC    --possui_demanda--> C1-DEM
C1-DEM     --possui_pedido-->  C1-PED
C1-DEM     --possui_pedido-->  C1-TUT
C1-PRET    --caracteriza-->    C1-AUT
C1-PRET    --demanda_para-->   C1-REU
C1-PRET    --possui_pedido-->  C1-PED / C1-TUT
C1-PRET    --possui_causa-->   C1-CAUSA
C1-VAL-PRET --caracteriza-->   C1-PRET
C1-REG-COMP --regula-->        C1-ANALISAR-CAB
C1-ANALISAR-CAB --brings_about--> C1-CABIVEL
C1-PER     --participa_de-->   C1-PERICIA
C1-PERICIA --creation-->       C1-LAUDO
C1-ANALISE --brings_about-->   C1-SUF
C1-SUF     --possibilita-->    C1-APTO
C1-APTO    --triggers-->       C1-JULGAR
C1-JULGAR  --creation-->       C1-SENT
C1-SENT    --impoe-->          C1-OBR
C1-OBR     --tem_parte-->      C1-DIREITO
C1-OBR     --tem_parte-->      C1-DEVER
C1-DIREITO --caracteriza-->    C1-AUT
C1-DEVER   --caracteriza-->    C1-REU
```

**Limites revelados:** não há ligação uniforme explícita entre todo ato/situação e o processo; a prioridade de `C1-PED` é anotação; não se instanciou o juiz como organização; suficiência após perícia e oitiva não demonstra julgamento antecipado; arquivamento e trânsito são fatos do cenário, não decisões inferidas.

O resultado de cabimento foi informado no marco 1; não se presume que a classe genérica Regra de Competência já contenha os axiomas legais. A análise neste cenário pode examinar o caso instaurado, enquanto C6 exemplifica análise antes do ajuizamento. As classificações processuais da pessoa referem-se ao contexto judicial de C1; o conjunto não implementa um histórico formal completo de classificações temporais.

### C2 — Microempresa e pagamento parcial seguido de satisfação

Microempresa Beta demanda a Empresa Pública Federal Simulada Beta. O pedido é de R$ 8.000,00 e a sentença acolhe R$ 6.000,00. Pedido, condenação e pagamento não são intercambiáveis.

| Elemento | Identificação |
| --- | --- |
| Autora e ré | `C2-AUT`: Microempresa Autora; `C2-REU`: Empresa Pública Federal/Demandado. |
| Representantes | `C2-ADV`: Advogado Constituído; `C2-ADV-REU`: Advogado de Empresa Pública Federal. |
| Pedido e valor da causa | `C2-PED`: Pedido de Pagar R$ 8.000,00; `C2-VAL`: 800000 centavos. |
| Sentença e obrigação | `C2-SENT`: Procedência Parcial; `C2-OBR`: Obrigação de Pagar R$ 6.000,00. |
| Recorte parcial | `C2-TP`: 200000 centavos pagos, 400000 de saldo; `C2-PARCIAL` e prosseguimento. |
| Recorte final | `C2-TF`: 600000 centavos pagos acumulados, saldo zero; `C2-CUMPRIDA` e `C2-CONCLUIDO`. |

O pagamento é acumulado, não uma segunda parcela a somar novamente ao valor final. O saldo obedece a `devido = pago acumulado + saldo`. Os valores são anotações da simulação; a ontologia atual não especifica esse esquema monetário. Não há arquivamento estipulado em C2-TF. Expedição de RPV/precatório, respectivos prazos e todos os atos intermediários não são simulados.

**Limite revelado:** uma consulta ao histórico sem recorte poderia devolver equivocadamente cumprimento parcial e integral como estados atuais simultâneos. O ensaio mantém as duas situações no histórico, mas somente uma delas no recorte aplicável à mesma obrigação.

### C3 — Empresa de pequeno porte e recurso

Empresa Gama, de pequeno porte, demanda a União em uma pretensão indenizatória inventada. A sentença é de improcedência; a autora interpõe recurso inominado, que é desprovido.

```text
C3-REP-A        --media-->        C3-AUT / C3-ADV
C3-REP-R        --media-->        C3-REU / C3-ADV-REU
C3-REL-REC      --media-->        C3-AUT / C3-SENT
C3-INTERPOR     --creation-->     C3-RECURSO
C3-RECURSO      --impugna-->      C3-SENT
C3-INTERPOR     --brings_about--> C3-INTERPOSTO
C3-INTERPOSTO   --triggers-->     C3-REMETER
C3-REMETER      --destina_a-->    C3-TURMA
C3-REMETER      --brings_about--> C3-ENCAMINHADO
C3-ENCAMINHADO  --triggers-->     C3-JULGAR-REC
C3-JULGAR-REC   --creation-->     C3-ACORDAO
C3-JULGAR-REC   --brings_about--> C3-DESPROVIDO
```

`A / B` abrevia duas triplas com o mesmo predicado, não um indivíduo composto. `C3-REP-A` e `C3-REP-R` são relações de Representação Recursal. O papel Sentença Recorrida é considerado nos recortes posteriores à interposição, não desde a produção do documento. O arquivo não pretende implementar um histórico formal completo de classificações contingentes.

**Recortes:** C3-TR, após remessa e antes do julgamento; C3-TF, após o resultado desprovido. O segundo não afirma trânsito em julgado.

**Premissas externas:** advogado obrigatório no recurso; prazo de dez dias úteis a partir da ciência; tempestividade e admissibilidade estipuladas. A instância `C3-PRAZO` recebe o valor informado, mas não o infere, e não se calcula uma data final.

### C4 — Fundação pública, acordo e obrigação não cumprida

Pessoa Delta, inicialmente representada por `C4-REP`, Representante Designado estipulado como não advogado, celebra acordo com Fundação Pública Federal Simulada Delta. Há procuradora federal da ré e conciliador. A hipótese de admissibilidade da representação inicial é explicitamente externa.

O fragmento contém `C4-DETERMINAR-AUD`, que leva a `C4-AUD-DESIGNADA`; essa situação é classificada como Resultado da Determinação de Audiência e Audiência Designada e promove `C4-AUD`. C5 exemplifica Audiência Dispensada. A versão atual introduziu a partição `{disjoint, complete}` entre esses subtipos. Ela classifica os resultados existentes, mas não obriga todo evento a produzir um resultado: a associação do evento permanece `0..1`. Os critérios jurídicos de escolha continuam informados externamente.

O fragmento distingue:

| Natureza | Instância |
| --- | --- |
| Documento de proposta | `C4-PROPOSTA`: Proposta de Acordo. |
| Evento de apresentação | `C4-APRESENTAR`: Apresentação de Propostas de Acordo. |
| Propriedade dependente | `C4-DEVER-COMP`: Dever de Comparecimento à Audiência, ligado ao evento de audiência conforme o desenho atual. |
| Evento de celebração | `C4-CELEBRAR`: Celebração de Acordo. |
| Relação constituída | `C4-ACORDO`: Acordo Processual, mediando autora e ré. |
| Situação resultante | `C4-CONCILIADA`: Conciliação Realizada. |
| Documento judicial | `C4-SENT`: Sentença Homologatória. |
| Obrigação | `C4-OBR`: Obrigação de Entregar Coisa, descrita como entrega de documento. |
| Resultado de cumprimento | `C4-NAO-CUMPRIDA`: Obrigação Não Cumprida. |

**Recortes:** C4-TI, início; C4-TF, após homologação, trânsito estipulado e início do cumprimento sem satisfação.

**Limites revelados:** a determinação e seus resultados oferecem suporte parcial à QC14, mas não explicitam todos os critérios jurídicos de necessidade. O PNG agora distingue Dever de Comparecimento à Audiência e Dever de Comparecimento à Perícia, porém ambos continuam ligados à Audiência de Conciliação, não à pessoa obrigada; o segundo não foi ligado por suposição a Realização de Perícia. Apenas o primeiro foi instanciado em C4. Faltam titular, intimação e vigência. Acordo e homologação dependem de vínculo narrativo ainda não explícito; atuação inicial sem advogado não equivale à dispensa em recurso. Não se simulou recurso inominado contra homologação de conciliação.

O `{disjoint, complete}` desenhado entre Conciliação Realizada e Conciliação Frustrada está sob a categoria geral Situação Processual. Seu alcance deve ser conferido em relação às outras especializações dessa categoria nos demais módulos. Os fragmentos e o script não certificam essa completude global.

### C5 — Não aptidão, produção complementar e reanálise

`C5-DETERMINAR-AUD` leva a `C5-AUD-DISPENSADA`, agora classificada também como Resultado da Determinação de Audiência. A antiga ligação `impede` foi removida do PNG e do catálogo de relações. Não se cria uma audiência efetivamente ocorrida para representar sua dispensa. `C5-SEM-CONTESTACAO` registra explicitamente a ausência de contestação, sem inferir procedência ou efeitos materiais de revelia.

| Recorte | Dados conhecidos até o marco | Situações selecionadas |
| --- | --- | --- |
| C5-TI, marco 4 | Primeira análise das provas e indicação de complementação; esta ainda não ocorreu. | C5-INSUF: Provas Insuficientes; C5-NAO-APTO: Não Apto a Julgamento. |
| C5-TC, marco 6 | C5-COMPLEMENTAR ocorreu no marco 5, produziu a situação C5-COMPLEMENTO-PRODUZIDO e foi seguido por C5-REANALISE no marco 6. | C5-SUF: Provas Suficientes; C5-APTO: Apto a Julgamento; Prova Complementar Produzida. |

```text
C5-ANALISE --brings_about--> C5-INSUF
C5-INSUF --associa_nao_aptidao--> C5-NAO-APTO
C5-INSUF --triggers--> C5-COMPLEMENTAR
C5-COMPLEMENTAR --brings_about--> C5-COMPLEMENTO-PRODUZIDO
C5-COMPLEMENTO-PRODUZIDO --triggers--> C5-REANALISE
C5-REANALISE --brings_about--> C5-SUF
C5-SUF --possibilita--> C5-APTO
```

`associa_nao_aptidao` é apenas o nome auxiliar da associação sem rótulo desenhada entre Provas Insuficientes e Não Apto a Julgamento. Não introduz causalidade ou impedimento universal. O antigo `impossibilita` não integra a versão atual. A ligação de retorno agora passa pela situação Prova Complementar Produzida, corrigindo o antigo `triggers` entre eventos. Não se presume que Apto e Não Apto formem uma partição completa, pois ela não foi explicitada no desenho.

O tipo concreto e a suficiência da complementação são informações do exemplo. Não há perícia realizada, agendamento ou intimação estipulados nesta nova versão de C5. Os fatos do marco 5 não podem ser usados como evidência no recorte do marco 4. O resultado suficiente da segunda análise não apaga o histórico da primeira, mas também não o torna atual. Aptidão não implica julgamento antecipado nem julgamento já ocorrido. A avaliação jurídica da insuficiência permanece contextualizada por PN05.

### C6 — Contraexemplo pré-processual

Pessoa Zeta consulta sobre mandado de segurança em caso federal com valor de dez salários mínimos. O novo diagrama permite representar essa análise sem criar um processo ou uma demanda judicial já instaurada.

| Indivíduo | Classificação e função |
| --- | --- |
| C6-PESSOA | Pessoa, sem papel de parte processual já constituído. |
| C6-PRET | Pretensão Jurídica, caracterizando a pessoa; não é Demanda ou Processo Judicial Federal. |
| C6-ORG | Organização Federal/Autarquia Federal, contexto institucional considerado na análise; não é automaticamente Demandado. |
| C6-PED / C6-CAUSA | Pedido de Outra Providência e Causa de Pedir possuídos pela pretensão. |
| C6-VAL | Valor da Causa caracterizando C6-PRET, com valor informado de dez salários mínimos. |
| C6-REG-COMP | Regra de Competência que regula a análise, com referência descritiva a PN08. |
| C6-ANALISAR-CAB | Análise de Cabimento no JEF, com participação da organização, pedido, causa e valor. |
| C6-NAO-CABIVEL | Resultado da Análise de Cabimento/Não Cabível no JEF, produzido no marco 1. |

```text
C6-PRET --caracteriza--> C6-PESSOA
C6-PRET --demanda_para--> C6-ORG
C6-PRET --possui_pedido--> C6-PED
C6-PRET --possui_causa--> C6-CAUSA
C6-VAL --caracteriza--> C6-PRET
C6-ORG / C6-PED / C6-CAUSA / C6-VAL --participa_de--> C6-ANALISAR-CAB
C6-REG-COMP --regula--> C6-ANALISAR-CAB
C6-ANALISAR-CAB --brings_about--> C6-NAO-CABIVEL
```

C6-T0 é o recorte inicial; C6-TA, no marco 1, é posterior ao resultado, mas continua pré-processual. Não foram criadas instâncias de Processo Judicial Federal, Processo Cabível no JEF ou Demanda, nem papéis de Demandante/Demandado. O vínculo da pretensão com uma organização não resolve sozinho a legitimidade passiva de um mandado de segurança.

PN08 fundamenta o resultado negativo informado, apesar do valor abaixo do limite. A regra genérica do diagrama não contém automaticamente suas condições legais executáveis. C1 exemplifica o resultado positivo, também informado. Assim, a QC31 passa a rastrear um evento de análise e seus resultados próprios, mantendo suporte parcial para a decisão jurídica completa.

## 4. Respostas esperadas por QC

**D:** descrição direta no fragmento; **P:** parcial; **N:** decisão não determinável pelo modelo atual. Esta tabela resume o registro detalhado do JSON, que contém as listas exatas de indivíduos, anotações e premissas para cada resposta. As respostas são expectativas elaboradas por inspeção documental, não saídas produzidas por consulta automatizada.

| QC | Recorte | Resposta esperada e limite | Suporte |
| --- | --- | --- | --- |
| QC1 | C1-TF | Autora, autarquia ré, advogada, procurador, perita, testemunha, conciliadora e servidor identificáveis. Juiz e integração de vínculos ao processo precisam de revisão. | P |
| QC2 | C2-TP | A autora é microempresa; C1 e C3 exemplificam pessoa física e empresa de pequeno porte. | D |
| QC3 | C4-TF | A ré é fundação pública federal; os demais tipos são exemplificados em C1, C2 e C3. | D |
| QC4 | C1-TF | Advogada Alfa representa a autora; Procurador Alfa representa a autarquia, por relações diferentes. | D |
| QC5 | C3-TR | Há advogada constituída na fase recursal. A obrigatoriedade depende de PN03. | P |
| QC6 | C1-TP | Perita, testemunha e conciliadora participam dos respectivos eventos registrados. | D |
| QC7 | C1-TP | Processo previdenciário segundo classificação informada, sem inferência de uma taxonomia completa de ações. | D |
| QC8 | C1-TI | Implantação de benefício é o pedido principal por C1-A01; a prioridade não está explicitada no modelo. | P |
| QC9 | C2-TP | Pedido de Pagar R$ 8.000,00; não confundir com os R$ 6.000,00 acolhidos. | D |
| QC10 | C1-TI | Existe pedido de tutela provisória, sem afirmar seu deferimento. | D |
| QC11 | C2-TP | Cumprimento parcial em prosseguimento, selecionado pelo recorte externo. | P |
| QC12 | C5-TI | Não houve contestação até a primeira análise, conforme situação negativa explícita; C1 fornece o caso positivo. | D |
| QC13 | C4-TF | Houve proposta e acordo, mas isso não demonstra uma permissão geral para qualquer caso. | P |
| QC14 | C4-TF | Resultado da determinação é designação; C5 exemplifica dispensa. A partição é disjunta e completa, mas a existência de resultado continua opcional em 0..1 e os critérios jurídicos são externos. | P |
| QC15 | C5-TI | Insuficiência e não aptidão indicam complementação no fragmento. A produção efetiva ocorre depois, em C5-TC, sem uso retroativo desse fato. | P |
| QC16 | C1-TP | Cópia administrativa, laudo e testemunho colhido; conteúdo do testemunho e vínculo de indicação pela parte são incompletos. | P |
| QC17 | C1-TP | Há testemunha ouvida; não se demonstra arrolamento prévio nem necessidade de nova oitiva. | P |
| QC18 | C5-TC | Produção complementar, situação produzida e reanálise resultam em suficiência e aptidão informadas, sem concluir julgamento antecipado ou ocorrido. | P |
| QC19 | C5-TI | Provas Insuficientes está associada a Não Apto a Julgamento; o antigo impossibilita foi removido. Isso não torna toda ausência de prova impedimento universal ao julgamento. | P |
| QC20 | C2-TP | Procedência parcial, de R$ 8.000,00 pedidos para R$ 6.000,00 reconhecidos no enunciado. | D |
| QC21 | C4-TF | Obrigação de Entregar Coisa, descrita como entrega de documento; C1 exemplifica fazer e C2 pagar. | D |
| QC22 | C1-TF | Há evento e situação de trânsito declarados; sua formação regular não foi calculada. | D |
| QC23 | C2-TP | Parcialmente cumprida: R$ 2.000,00 de R$ 6.000,00. O pagamento integral posterior não responde sobre esse recorte. | D |
| QC24 | C2-TF | Cumprimento concluído no recorte final, não no parcial. | D |
| QC25 | C1-TF | Arquivamento ocorrido, com única obrigação satisfeita e nenhuma pendência estipulada; autorização geral não formalizada. | P |
| QC26 | C3-TR | Recurso inominado interposto pela autora; C1 fornece ausência de recurso expressa. | D |
| QC27 | C3-TR | Dez dias úteis a partir da ciência, por PN04; valor informado, não cálculo de termo final. | P |
| QC28 | C3-TR | Advogado obrigatório por PN03; a mera presença de Representação Recursal não expressa toda a exigência. | P |
| QC29 | C3-TR | Remessa efetuada à Turma Recursal Simulada Gama. | D |
| QC30 | C3-TF | Recurso desprovido e acórdão produzido, sem afirmar trânsito automático. | D |
| QC31 | C6-TA | Análise de Cabimento no JEF registra Não Cabível no JEF com fundamento informado em PN08; dez salários mínimos não afastam a exclusão legal. C1 exemplifica resultado positivo informado. | P |
| QC32 | C4-TI | No contexto inicial permitido e estipulado, a autora não contratou advogado; a permissão vem de PN02. | P |
| QC33 | C1-TI | Ré indicada também é a organização relacionada à pretensão analisada; demanda para não resolve sozinho a legitimidade passiva de qualquer caso. | P |
| QC34 | C1-TI | Petição e cópia administrativa são selecionadas no exemplo; não são lista legal universal ou exaustiva. | P |
| QC35 | C1-TI | Pode-se explicar o percurso exemplificado, sem afirmar que toda etapa seja obrigatória ou universal. | P |
| QC36 | C5-TC | A complementação já ocorreu e a nova análise registra aptidão. A não aptidão anterior é histórica; a seleção de fase continua contextual, não consulta judicial real. | P |
| QC37 | C4-TF | Há Dever de Comparecimento à Audiência; o novo Dever de Comparecimento à Perícia também está ligado à audiência no PNG. Faltam titular, intimação e exigibilidade individual. | P |
| QC38 | C1-TF | Trânsito, satisfação de obrigação de fazer, conclusão e arquivamento são exemplificados; ofício/RPV/precatório e condições específicas não são exaustivamente cobertos. | P |

## 5. Premissas jurídicas externas

O JSON registra o conteúdo e a fonte de cada premissa. Não são regras automaticamente implementadas.

| Código | Conteúdo e fonte |
| --- | --- |
| PN01 | Competência não depende apenas de valor: Lei nº 10.259/2001, arts. 3º e 6º. |
| PN02 | Possibilidade de representação inicial por advogado ou não, no contexto cível e nas hipóteses admitidas: Lei nº 10.259/2001, art. 10. |
| PN03 | Advogado obrigatório no recurso inominado: Lei nº 9.099/1995, art. 41, § 2º, e aplicação compatível ao JEF. |
| PN04 | Prazo de dez dias úteis, ciência e interrupção por embargos: Lei nº 9.099/1995, arts. 12-A, 42 e 50. Não se calcula data final. |
| PN05 | Critérios de prova e julgamento: CPC, arts. 355, 370 e 373, observada a compatibilidade com o rito especial. |
| PN06 | Exceção à recorribilidade por recurso inominado da sentença homologatória de conciliação: Lei nº 9.099/1995, art. 41, caput. |
| PN07 | Disciplina de cumprimento de obrigações: Lei nº 10.259/2001, arts. 16–17. O procedimento não é integralmente simulado. |
| PN08 | Exclusão de mandado de segurança: Lei nº 10.259/2001, art. 3º, § 1º, I. |

Textos oficiais: [Lei nº 10.259/2001](https://www.planalto.gov.br/ccivil_03/leis/leis_2001/l10259.htm), [Lei nº 9.099/1995](https://www.planalto.gov.br/ccivil_03/leis/l9099.htm) e [CPC](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm). A aplicação das premissas e o refinamento dos modelos devem ser conferidos com o especialista do domínio.

## 6. Reprodução da conferência de integridade

Na pasta que contém `tcc-jec.md`, executar com Python 3:

```powershell
python avaliacao/verificar-dados.py
```

Não são necessárias bibliotecas externas. O script lê os arquivos, não modifica o TCC nem o conjunto de dados. A conferência verifica:

1. JSON sem chaves repetidas; identificadores únicos e referências resolvidas.
2. Classes do catálogo encontradas lexicalmente no texto; classificações e predicados catalogados.
3. Tipos básicos selecionados para `brings_about`, `triggers`, `promove`, dependência histórica, criação, participação, não aptidão, aptidão e origem de mediação. A caracterização do dever pela audiência é registrada, não certificada como adequada.
4. Ordem temporal local das relações verificadas; evidências e anotações não posteriores ao recorte usado pela QC.
5. Partições de resultados declaradas nas instâncias, limite de um resultado por determinação, entrada/regra/resultado informado de cada análise de cabimento concluída e não compartilhamento de uma mesma propriedade intrínseca por portadores distintos. Os recortes selecionam uma avaliação atual por dimensão, uma obrigação e uma pretensão por cenário; não se pretende validar todos os estados possíveis de um processo real.
6. Conciliação dos valores de pagamento e dos estados de C2.
7. Preservação das 38 QCs, com número e pergunta na mesma célula, classes listadas no dicionário e percursos escritos por extenso, sem separadores simbólicos. Essa conferência é lexical e estrutural, não prova que a descrição esteja semanticamente correta. A seção da matriz é reconhecida pelo título, sem fixar sua numeração. Também se confere a correspondência de recorte e classificação de suporte deste guia com o JSON.

As respostas esperadas foram redigidas por inspeção. **O script não consulta o grafo para obtê-las e não prova que seu conteúdo textual é verdadeiro.** Também não verifica todas as cardinalidades, toda a semântica de generalização, equivalência entre conceitos reutilizados, axiomas legais, prazos reais ou a adequação para usuários.

Uma execução bem-sucedida deve ser descrita como **conferência de integridade dos artefatos de instanciação**, nunca como “38 QCs aprovadas por um reasoner”.

## 7. Como atualizar o material após revisar a ontologia

1. Atualizar o diagrama e a explicação do conceito ou regra, em vez de preencher silenciosamente a lacuna só nos exemplos.
2. Rever as linhas correspondentes da matriz em `tcc-jec.md`.
3. Alterar as instâncias, relações e respostas em `dados-simulados.json`, mantendo explícita a diferença entre modelo e anotação.
4. Atualizar este guia quando houver mudança de cenário ou resposta.
5. Executar novamente a conferência e revisar as respostas com o especialista. A classificação P ou N só deve mudar quando houver suporte efetivamente documentado no modelo revisado.
