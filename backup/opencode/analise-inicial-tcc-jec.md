# Análise inicial da monografia sobre o Juizado Especial Federal Cível

> Nota de atualização: este parecer registra a análise anterior à criação da matriz e das instanciações. A etapa posterior foi documentada nas Seções 3.8 e 4.4 de `tcc-jec.md` e em `avaliacao/`. Ela acrescenta rastreabilidade das 38 QCs e exemplos fictícios, mas não constitui validação formal nem elimina automaticamente as lacunas conceituais apontadas neste parecer.

## 1. Escopo e diagnóstico geral

Foi realizada a leitura integral de `tcc-jec.md`, com conferência de trechos do PDF, inspeção dos 16 arquivos de `diagramas/` e consulta dirigida às fontes fornecidas. Também foram consultados os textos oficiais das Leis nº 10.259/2001, nº 9.099/1995 e nº 13.105/2015 para conferir questões jurídicas específicas.

Esta análise é uma revisão inicial de conteúdo, coerência e apresentação. Não constitui validação jurídica exaustiva nem verificação formal do modelo: não há, neste diretório, um arquivo editável da ontologia que permita executar verificações na ferramenta de modelagem. A consulta às fontes foi dirigida aos pontos discutidos abaixo, não uma leitura integral de todas as teses e publicações.

**Diagnóstico:** o trabalho já apresenta uma base substancial: domínio delimitado, fundamentação em UFO/UFO-L, adoção da SABiO, 38 questões de competência, 15 diagramas de classes e um diagrama de pacotes. Entretanto, ainda são necessárias alterações importantes antes de considerá-lo uma versão final. As prioridades são demonstrar a avaliação, corrigir inconsistências conceituais dos diagramas, completar as referências e substituir os trechos remanescentes do modelo de monografia.

### Pontos positivos

- O recorte no JEF Cível é socialmente relevante e permite uma contribuição identificável em representação do conhecimento.
- A separação entre aspectos estruturais e procedimentais ajuda a organizar um domínio complexo.
- A distinção entre ontologia de referência e implementação operacional está explicitada na metodologia.
- As questões de competência oferecem uma boa base para organizar e avaliar a contribuição.
- A distinção entre documentos, eventos e relações jurídicas está presente em diversas partes do modelo, embora ainda precise de ajustes de consistência.

## 2. Prioridades de alteração

| Prioridade | Local | Alteração necessária |
| --- | --- | --- |
| Crítica | Seções 1.2, 3.3, 3.4 e Capítulo 4 | Apresentar evidências e resultados da avaliação anunciada. |
| Crítica | Seção 4.2.2 e `diagramas/organizacoes.png` | Distinguir o magistrado, pessoa que exerce um papel, do órgão jurisdicional. |
| Alta | Seções 4.2.5, 4.3.2, 4.3.7, 4.3.9 e 4.3.10 | Rever categorias ontológicas, relações temporais e condições jurídicas. |
| Alta | Referências e citações | Incluir as obras efetivamente utilizadas e conferir a identificação das fontes. |
| Alta | Elementos pré-textuais e Capítulo 5 | Substituir campos de preenchimento, texto fictício e instruções do modelo. |
| Média | Dicionário, quadros e apresentação | Conciliar nomes e quantidades, corrigir tabelas e restaurar as figuras no Markdown. |

## 3. Avaliação da ontologia: principal lacuna metodológica

O objetivo específico de validação aparece na Seção 1.2. A Seção 3.3 afirma que houve acompanhamento e validação por especialistas; a Seção 3.4 afirma que as questões foram retomadas na avaliação. No entanto, o Capítulo 4 descreve os diagramas sem apresentar um procedimento de avaliação e seus resultados de maneira verificável.

Isso não permite concluir que a avaliação não ocorreu. Significa que **o texto ainda não permite ao leitor verificar como ela foi realizada e o que demonstrou**.

Recomenda-se acrescentar uma seção de avaliação contendo:

1. **Procedimento:** o que foi inspecionado, quais critérios foram utilizados e em que momento.
2. **Participantes:** quantidade e perfil dos especialistas, forma de participação e materiais examinados, com anonimização quando necessária.
3. **Rastreabilidade das 38 QCs:** quais classes, relações, atributos e axiomas sustentam cada resposta.
4. **Instanciações ou cenários:** exemplos concretos, reais devidamente anonimizados ou hipotéticos explicitamente identificados, que mostrem a representação dos casos.
5. **Resultados:** problemas encontrados, alterações realizadas, questões atendidas parcialmente e limitações restantes.

Para uma ontologia de referência, essa avaliação pode ser conceitual e estática. **Não é necessário transformar o trabalho em uma implementação OWL para suprir essa lacuna.** Falbo (2014), no processo de avaliação da SABiO, recomenda uma tabela de correspondência entre QCs e elementos da ontologia e a validação por julgamento de especialistas e instanciação; ver páginas 11–12 de `fonte-sabio.pdf`.

### QCs que merecem atenção especial

Os exemplos abaixo são indícios de cobertura incompleta a verificar, não resultados de uma avaliação formal:

| QC | O que ainda precisa ser demonstrado |
| --- | --- |
| QC5 e QC28: necessidade de advogado | A existência de um representante não expressa, sozinha, a regra de obrigatoriedade por fase. A representação recursal também precisa distinguir o representante habilitado como advogado do representante designado que não o seja. |
| QC27: prazo recursal | A classe `Prazo Recursal` não informa, por si só, a duração aplicável, o termo inicial, a contagem em dias úteis e as causas de interrupção. |
| QC31: cabimento no JEF | É preciso explicitar os critérios legais, não apenas nomear `Processo Cabível no JEF`: valor, matéria, partes e exclusões legais, conforme o recorte. |
| QC34: documentos necessários | `Documento Necessário ao Processo` é uma categoria geral. Falta mostrar como identificar os documentos exigidos para o caso concreto. |
| QC37: comparecimento a audiência ou perícia | Representar a ocorrência de audiência ou perícia não equivale a representar sua designação, a intimação e a necessidade de comparecimento. |

Questões como “Em que fase está meu processo?” exigiriam, em um sistema futuro, dados de um processo específico e critérios de interpretação desses dados. A ontologia de referência oferece o suporte conceitual; ela não consulta nem acompanha processos por si só.

## 4. Pontos conceituais a revisar no texto e nos diagramas

### 4.1 Magistrado não é uma organização

**Local:** Seção 4.2.2 e `diagramas/organizacoes.png`.

No diagrama, `Juiz` especializa `Órgão Julgador`, que especializa `Organização Federal` e `Organização`. Isso faz com que todo juiz seja classificado como uma organização. No dicionário, porém, `Juiz` é definido como magistrado.

É necessário separar:

- a pessoa que desempenha o papel de juiz;
- o juízo/JEF ou órgão jurisdicional em que ela atua;
- a Turma Recursal, órgão colegiado integrado por magistrados.

Uma direção possível é representar o magistrado como um papel de `Pessoa` e relacioná-lo ao órgão em que exerce a função. A decisão final deve considerar o padrão de agentes institucionais adotado. Apenas trocar a palavra no texto, mantendo o diagrama, não resolveria a inconsistência.

Também é preciso esclarecer a relação entre `Órgão Julgador`, usado nesse diagrama, e `Órgão Judicial`, apresentado como `kind` independente no diagrama de competência.

### 4.2 Interesse de agir não se reduz a uma intenção

**Local:** Seção 4.2.5 e `diagramas/competencia.png`.

`Interesse de Agir` está classificado como `intention`. Entretanto, na acepção processual utilizada no próprio dicionário, refere-se à necessidade/utilidade da tutela jurisdicional, e não simplesmente a um estado mental do demandante. O art. 17 do CPC trata do interesse e da legitimidade para postular em juízo.

Recomenda-se reexaminar a categoria ontológica e distinguir a intenção de ajuizar uma demanda da condição jurídica de interesse processual. A classificação substituta depende da conceituação adotada; não foi alterada automaticamente.

É positivo que o texto não torne o requerimento administrativo prévio obrigatório para todo processo. Ainda assim, é necessário documentar em quais hipóteses esse requerimento é relevante, com fundamento jurídico específico.

### 4.3 Generalizações e conjuntos de especialização

**Locais:** diagramas de organizações, representantes, serventuários e demanda/causa/pedido.

- **Pedidos:** fazer, não fazer e pagar classificam a prestação pretendida; tutela provisória classifica outra dimensão da tutela. Um pedido de tutela provisória pode buscar uma obrigação de fazer. É preciso justificar ou revisar a disjunção dessas categorias, preferencialmente separando as dimensões de classificação.
- **Processos:** `Processo FGTS` e `Processo Habitacional` aparecem como especializações de `Processo Indenizatória`. Demandas de FGTS ou habitacionais não são necessariamente indenizatórias. Essa hierarquia precisa ser revista.
- **Serventuários:** o agrupamento de perito e conciliador como serventuários precisa de definição e justificativa. `Auxiliar da Justiça`, já existente no modelo, é uma categoria a considerar. O art. 149 do CPC oferece apoio à distinção; além disso, oficial de justiça também pode ser servidor judicial, o que exige cuidado com `{disjoint}`.
- **Representantes:** `Representante Designado` não significa necessariamente “não advogado”. A exclusividade em relação a `Advogado Constituído` precisa ser justificada ou reformulada.
- **Organizações:** a União é um ente singular. Convém explicar se `União Federal` representa um tipo com restrição de uma única instância ou se deveria ser representada como indivíduo, evitando confundir tipo e instância.

Os marcadores `{disjoint, complete}` impõem exclusividade e cobertura total. A expressão “no escopo deste trabalho” não dispensa demonstrar que essas restrições são adequadas à interpretação do modelo.

### 4.4 Eventos, situações e relações temporais

**Locais:** Seções 4.3.2, 4.3.9 e 4.3.10 e diagramas correspondentes.

Na fundamentação de eventos consultada, `triggers` relaciona uma **situação a um evento**, enquanto `brings about` relaciona um **evento à situação resultante**. Ver Seção 3.4, página 7 de `fonte-TowardsOntologicalFoundationsfortheConceptualmodelingofevents-4.pdf`.

Há usos que precisam ser ajustados:

- O texto de Procedimentos descreve `Apresentação de Contestação` como origem de `triggers` para `Apto a Julgamento`, invertendo as categorias esperadas nessa relação.
- Em Recursos, o documento `Sentença` aparece como origem de `triggers` para `Decurso do Prazo Recursal`. É necessário distinguir o documento, sua ciência/intimação, a situação de prazo em curso e o término do prazo.
- Em Cumprimento, `Prosseguimento do Cumprimento` se liga por `brings about` a `Conclusão do Cumprimento`, embora ambos estejam classificados como eventos.

Também se deve diferenciar dependência histórica de simples ordem de apresentação. Os diagramas não devem transformar um percurso frequente em sequência obrigatória para todos os processos.

### 4.5 Contestação, instauração e julgamento

**Locais:** Seções 4.3.2, 4.3.3, 4.3.4 e 4.3.7.

- A afirmação de que a contestação somente pode ser apresentada depois da citação é excessivamente absoluta. O comparecimento espontâneo pode suprir a falta ou nulidade da citação: art. 18, § 3º, da Lei nº 9.099/1995 e art. 239, § 1º, do CPC.
- A modelagem geral faz o julgamento depender historicamente da apresentação de contestação. É preciso comportar, conforme o recorte, a ausência de defesa e decisões que não pressupõem essa apresentação.
- `Protocolização` e `Ajuizamento` são descritos como etapas sucessivas distintas. O art. 312 do CPC considera proposta a ação quando a petição inicial é protocolada. A Lei nº 9.099/1995, art. 14, também admite apresentação oral do pedido. Se forem mantidos eventos separados, sua diferença precisa ser juridicamente e ontologicamente justificada.
- O caminho inicial deve permitir a atuação sem advogado nas hipóteses admitidas, sem obrigar um representante na constituição de toda petição. A apresentação oral reduzida a escrito pela secretaria também merece ser considerada ou expressamente delimitada como não contemplada.
- Provas insuficientes não impedem invariavelmente o julgamento nem impõem um ciclo ilimitado de complementação. É preciso considerar o encerramento da instrução e as consequências do ônus da prova. Os arts. 355, 370 e 373 do CPC ajudam a fundamentar essa revisão, observada sua compatibilidade com o procedimento especial.

### 4.6 Recursos e cumprimento: delimitar o que efetivamente está representado

**Locais:** Seções 3.2, 4.3.9 e 4.3.10.

O módulo recursal concentra-se no recurso inominado. O escopo deve deixar claro se embargos de declaração, pedido de uniformização e recurso extraordinário estão fora da ontologia, apesar de integrarem o contexto jurídico dos JEFs.

Para o recurso inominado, a Lei nº 9.099/1995 prevê prazo de dez dias a partir da ciência da sentença (art. 42), contagem em dias úteis (art. 12-A) e representação obrigatória por advogado (art. 41, § 2º). Os embargos de declaração interrompem o prazo recursal (art. 50). Essas disposições devem ser consideradas em conjunto com a Lei nº 10.259/2001 e o recorte adotado.

Quanto ao cumprimento, os arts. 16–17 da Lei nº 10.259/2001 diferenciam obrigações e disciplinam o pagamento por requisição, incluindo hipóteses de precatório. O modelo pode abstrair esses detalhes, mas então não deve sugerir cobertura integral do procedimento. Recomenda-se declarar expressamente essas limitações e verificar se as QCs pretendem exigir esse nível de detalhamento.

## 5. Fundamentação, reúso e contribuição

### Pontos confirmados nas fontes

- A OntoRS efetivamente apresenta `Judicial Process` e `Petition` como tipos de `relator`. Isso é descrito na Seção 3 de `fonte-ontors.pdf`, página 4 do PDF, página impressa 82. **Não é adequado mudar essas classificações apenas porque os nomes também designam documentos ou atividades em outros contextos.** O trabalho precisa explicitar qual acepção está reutilizando e como ela se distingue de `Documento de Petição Inicial` e dos eventos de peticionamento.
- A distinção entre `Legal Norm` e `Legal Normative Description` está explicitada na tese de Griffo: Seção 5.3, páginas impressas 105–108. Vale explicar no TCC a diferença entre norma, texto normativo e documento que o registra.
- A definição de `Collective` que negava o fornecimento de identidade precisava de correção. A tese de Guizzardi (2005), Quadro 8-1, páginas impressas 317–318, trata `kind`, `quantity` e `collective` como substance sortals. Essa correção foi feita no Quadro 1 do Markdown, com inclusão de Guizzardi na indicação de fonte.

### Melhorias de argumentação

- Formular de maneira explícita o problema de pesquisa: qual lacuna de representação semântica existe no domínio e como o artefato procura tratá-la.
- Na introdução, manter como contribuição principal o desenvolvimento da ontologia, e não a exposição dos benefícios da Lei nº 10.259/2001. Esses benefícios contextualizam e justificam o trabalho.
- Diferenciar os resultados obtidos das aplicações futuras: peticionamento, acompanhamento e maior compreensão pelo cidadão são usos potenciais, não benefícios empiricamente demonstrados neste trabalho.
- Explicitar o que foi reutilizado, adaptado e criado em relação à OntoRS e à UFO-L. O quadro de reúso é um bom começo, mas deve permitir reconhecer a contribuição original e as mudanças realizadas.
- Explicar a acepção de “processo”: relação jurídico-processual, conjunto de autos/documentos e desenvolvimento temporal não são a mesma entidade. Isso é especialmente importante no exemplo da Seção 2.2.1 e no reúso de `Processo Judicial Federal`.
- Uniformizar a narrativa temporal: a Seção 1.3 anuncia etapas futuras, enquanto o Capítulo 3 descreve atividades concluídas. A redação deve refletir o estágio real de cada atividade, sem transformar avaliação planejada em avaliação realizada.

## 6. Referências e partes ainda não concluídas

### Referências

A lista final contém quatro entradas de Souza e colaboradores associadas ao modelo de monografia, mas não apresenta as principais obras citadas no desenvolvimento. É necessário conferir a correspondência entre todas as citações e as referências finais.

Entre as fontes a incluir, conforme o uso efetivo no texto, estão:

- Falbo (2014), sobre SABiO;
- Guizzardi (2005), Guizzardi et al. (2011, 2013 e 2015) e Guizzardi e Wagner (2005);
- Griffo (2018), sobre UFO-L;
- Scherp et al. (2011), sobre ontologias de núcleo;
- Ribeiro e Sanzovo (2011), sobre o JEF e acesso à justiça;
- os trabalhos de Costa e colaboradores de 2022 e 2023 relacionados à OntoRS;
- as leis e demais fontes normativas efetivamente utilizadas.

O arquivo `fonte-estereotiposOntologia.pdf` contém apenas duas páginas internas de uma publicação do ENANCIB 2017, sem identificação bibliográfica completa visível. É preciso confirmar a autoria atribuída a “Guimarães et al. (2017)” e completar essa referência. Não há informação suficiente nesse recorte para fazê-lo com segurança.

A versão local de `Designing Core Ontologies` apresenta-se como relatório técnico de 2011. A referência final deve identificar corretamente a versão utilizada, sem combinar automaticamente os dados desse relatório com os da publicação em periódico.

### Elementos pré-textuais e conclusão

Permanecem no arquivo:

- “Título do Trabalho”, “Nome do Aluno”, nomes fictícios de orientador e banca e palavras-chave de exemplo;
- ano 2020 nos elementos iniciais, em contraste com fontes de figuras datadas de 2026;
- texto *Lorem ipsum* em agradecimentos, resumo e outros elementos opcionais;
- listas de ilustrações e tabelas provenientes do modelo;
- instruções de elaboração no Capítulo 5, em vez de conclusão e trabalhos futuros.

Essas partes precisam ser substituídas com dados reais ou removidas quando opcionais. O resumo deve sintetizar problema, objetivo, método, artefato e resultados efetivamente obtidos. A conclusão deve retomar os objetivos e reconhecer as limitações da avaliação e do escopo.

Sugestão de título, apenas para consideração: **“Uma ontologia de referência para o domínio dos Juizados Especiais Federais Cíveis”**.

## 7. Dicionário e apresentação

### Dicionário de termos

- O texto anuncia **154 termos**, mas a tabela contém **157 entradas nomeadas**, sem duplicatas nominais exatas. É necessário conciliar a tabela com o inventário do modelo antes de afirmar a quantidade de conceitos da ontologia.
- O parágrafo de apresentação promete fontes de informação, mas a tabela tem apenas as colunas `Termo` e `Descrição`. Incluir a origem de cada definição ou corrigir a apresentação, conforme o objetivo do dicionário.
- `Ação Instaurada` aparece no dicionário, enquanto os diagramas e a exposição utilizam `Processo Instaurado`.
- O texto utiliza `Recurso Não Conhecido`, enquanto o diagrama e o dicionário usam `Não Conhecido`.
- Há rótulos gráficos a corrigir, como `Processo Previdenciária`, `Processo Indenizatória` e `Conciliação Frustada`. A correção deste último termo foi feita apenas no dicionário; a imagem continua exigindo ajuste.
- Se o dicionário foi elaborado pelo autor do TCC, sua apresentação como **apêndice**, e não anexo, deve ser considerada conforme as orientações institucionais.

### Apresentação do Markdown

O Markdown contém sinais de extração automática do PDF: texto ilegível entre comentários de imagens, quebras artificiais de parágrafo e tabelas partidas entre páginas. As figuras não estão inseridas como imagens no arquivo.

Recomenda-se, em uma revisão de apresentação:

1. vincular os diagramas de `diagramas/` às figuras correspondentes;
2. recuperar as figuras teóricas das fontes e conferir suas atribuições;
3. recompor os Quadros 2, 3, 4 e o dicionário, eliminando fragmentações da extração;
4. uniformizar níveis de títulos, legendas, nomes dos módulos e a sigla JEF;
5. atualizar sumário, listas, paginação e metadados no documento de origem usado para gerar o PDF.

As correções feitas no Markdown não modificam automaticamente o PDF existente.

## 8. Alterações já realizadas em `tcc-jec.md`

Foram feitas alterações pontuais, sem reescrever a contribuição nem modificar os diagramas:

- correções de acentuação, concordância, pontuação e trechos acidentalmente duplicados;
- recomposição da lista de perguntas exemplificativas da Seção 2.1 e separação das QCs que estavam na mesma linha;
- correção da Seção 1.4 para refletir os quatro capítulos posteriores à introdução e os títulos efetivamente existentes;
- organização da numeração das figuras do corpo do texto em sequência de 1 a 22;
- correção de `Figura X` para `Figura 6` e da referência aos quadros de estereótipos;
- correção da definição de `Collective`, fundamentada na fonte primária;
- ajuste da descrição de ontologias operacionais e da redação sobre o recorte da SABiO;
- ajuste de `Scherp (2011)` para `Scherp et al. (2011)`, conforme a autoria da fonte;
- substituição da promessa de implementação futura por uma possibilidade de expansão;
- ajuste dos títulos das Seções 4.3.8 e 4.3.9 para cabeçalhos Markdown.

Não foram preenchidos resumo ou conclusão, inventados dados de especialistas, incluídos resultados de testes não documentados nem alteradas as classificações conceituais que dependem de revisão conjunta do texto e do modelo. O PDF e os PNGs foram preservados.

## 9. Ordem recomendada para a próxima revisão

1. Resolver com o orientador e o especialista as inconsistências de modelagem, começando por juiz/órgão, interesse de agir, hierarquias e relações de eventos.
2. Revisar as QCs e construir a matriz de rastreabilidade, explicitando critérios legais e limites de cobertura.
3. Realizar ou documentar a avaliação com instanciações e resultados, registrando o que foi efetivamente feito.
4. Atualizar a exposição dos resultados, o dicionário e as referências para refletir o modelo revisado.
5. Redigir conclusão e resumo; finalizar elementos pré-textuais e apresentação.

## Textos normativos consultados

- [Lei nº 10.259/2001](https://www.planalto.gov.br/ccivil_03/leis/leis_2001/l10259.htm).
- [Lei nº 9.099/1995](https://www.planalto.gov.br/ccivil_03/leis/l9099.htm).
- [Código de Processo Civil — Lei nº 13.105/2015](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm).

As recomendações jurídicas devem ser discutidas com o especialista do domínio, considerando o recorte temporal e as fontes normativas e jurisprudenciais adotados no trabalho.
