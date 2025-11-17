# P3 - Terceira Entrega

2025.2 Ciência e Visualização de Dados em Saúde

# Projeto: Redes transcriptômicas relacionadas ao autismo: diferenças sexuais e de desenvolvimento no cérebro humano
# Project: Transcriptomic networks related to autism: sex and developmental differences in the human brain

# Descrição Resumida do Projeto

Transtornos do Neurodesenvolvimento (NDDs) afetam algo em torno de 18% da população mundial. Dentre esses o Transtorno do Espectro Autista (TEA) é um dos mais prevalentes. Quando analisa-se a proporção diagnóstica do TEA entre homens e mulheres, observa-se um maior número de homens diagnosticados, aproximadamente 3-4:1. Teorias do por quê dessa prevalência no sexo masculino incluem a ideia de que mulheres seriam melhores em mascarar a sintomatologia, mas também a possibilidade de que mulheres podem necessitar de maior carga de risco genético (ou de mutações mais penetrantes) para manifestar TEA, efeito chamado de “protetivo feminino”. Pensando nisso, o presente trabalho, buscou bases de dados públicas, que incluissem amostras genéticas de indivíduos diagnosticados com TEA, visando analisar se haveriam diferenças entre: indivíduos diagnosticados do sexo feminino versus masculino e diferenças entre indivíduos neurotípicos versus neurodivergentes. Encontraram-se algumas bases de dados interessantes, em especial na base GEO (Gene Expression Omnibus) e SFARI. Dentre os principais desafios encontrados, destaca-se a não diferenciação por sexo em algumas bases (como é o caso do SFARI) e poucas amostras do sexo feminino. Os resultados apontam para descobertas similares às da literatura disponível. Estudos futuros provavelmente poderiam focar na identificação de amostras por nível de gravidade e sintomatologia. 

# Slides

[Redes transcriptômicas para estudo das diferenças de expressão gênica sexo-específicas no Transtorno do Espectro Autista (TEA)](https://docs.google.com/presentation/d/1V4jU9-_xXqlAjIQOqwQ8WGE6kgRY32t2/edit?slide=id.p1#slide=id.p1)

# Fundamentação Teórica

Transtornos do Neurodesenvolvimento (NDDs) afetam algo em torno de 18% da população mundial. Dentre esses, o Transtorno do Espectro Autista (TEA) é um dos mais prevalentes (KAUR et al., 2022). Dentre os diagnósticos realizados observa-se que há uma maior frequência diagnóstica em meninos do que em meninas. Em específico, relatórios de vigilância de grande escala mostram uma razão menino:menina de aproximadamente 3–4:1, dependendo do conjunto de dados e da faixa etária analisada (CDC, 2025).

Dentre os casos diagnosticados, há indicativo de que meninas podem apresentar maior gravidade global ou maior carga de déficit adaptativo do que meninos, informação sobre a qual teoriza-se que possa ter relação com o fato de que somente os casos mais severos em meninas chegam ao diagnóstico na infância (SAURE et al., 2023; PARK et al., 2012). Além disso, as diferenças nas sintomatologias entre o sexo biológico feminino e masculino incluem comorbidades internas (ansiedade, depressão) com uma tendência a ser mais frequentemente relatadas em mulheres autistas, enquanto comportamentos externalizantes (hiperatividade, agressão) aparecem com maior frequência em homens; o que pode influenciar tanto a apresentação clínica quanto os motivos de encaminhamento para avaliação. (HULL; PETRIDES; MANDY, 2020; WERLING; GESCHWIND, 2013).

Essa diferença no diagnóstico entre homens e mulheres muito provavelmente não é explicada por um único fator, mas sim de um conjunto de fatores inter-relacionados: diferenças fenotípicas (incluindo camuflagem), limitação dos instrumentos e critérios diagnósticos, vieses de encaminhamento e, possivelmente, efeitos protetores biológicos nas mulheres  (HULL; PETRIDES; MANDY, 2020; COOK et al., 2021; CORBETT et al., 2020; WIGDOR et al., 2022; GOCKLEY et al., 2015; ZHANG et al., 2020; CDC, 2025; WERLING; GESCHWIND, 2013).

Apesar de haver uma  maior taxa de diagnóstico do TEA em homens do que em mulheres, há uma quantidade surpreendentemente pequena de pesquisas focadas nas razões para essa disparidade (Halladay et al., 2015). Em específico investigar diferenças sexuais no TEA pode ajudar na compreensão da  sintomatologia, opções e resposta a tratamentos (Napolitano et al. , 2022). 

Estudos de transcriptoma do cérebro em desenvolvimento demonstram que genes de risco para TEA e lncRNAs tendem a se organizar em módulos de co-expressão específicos, muitos dos quais têm expressão restrita a janelas temporais críticas, como o período pré-natal e início pós-natal, quando ocorre a formação de circuitos neurais essenciais (Willsey et al., 2013). A análise de diferenças sexuais em co-expressão permite investigar possíveis mecanismos de proteção em meninas ou maior suscetibilidade em meninos, servindo como proxy da influência hormonal (Lin L, et al. 2019).

Pensando em formas de ampliar a análise dessas diferenças, o presente trabalho buscou identificar estudos que buscassem comparar diferenças genéticas entre indivíduos diagnosticados e neurotípicos, além de entre indivíduos diagnosticados de sexo diferente. 


# Perguntas de Pesquisa

1. É possível identificar genes “hubs” e módulos de expressão que diferenciam amostras de neurodivergentes femininos e masculinos? É possível ampliar o escopo de comparação entre neurodivergentes e neurotípicos?

2. A expressão destes genes centrais, se relaciona com a co-expressão de genes de hormonas sexuais regulados pelo eixo hipotálamo-hipófise de maneira diferencial?

3. Os genes “hubs” identificados aqui  já foram previamente associados ao TEA?

4. Existe correlação entre os genes “hubs” identificados e a localização cromossomal em X e Y?

5. Existe correlação entre os genes “hubs” identificados no cérebro e genes “hubs” identificados no sangue? É possível propô-los como biomarcadores?


# Metodologia

## Bases de Dados e Evolução


| Base de Dados  | Endereço na Web    | Resumo descritivo |
|-------|--------|----------------|
| GSE 102741 | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm| Dados públicos do [GEO](https://www.ncbi.nlm.nih.gov/gds) de RNA-seq, com normalização RPKM, extraídos de amostras do Cortex prefrontal dorsolateral do cérebro humano, para os grupos TEA e controle e metadados sobre idade e sexo. |
| E-MTAB-13871 | https://www.omicsdi.org/dataset/biostudies-arrayexpress/E-MTAB-13871 | Dados públicos do ArrayExpress, contendo amostras de sangue de humanos controle e com TEA, extraindo RNA-seq de mRNA com normalização binomial negativa por células mononucleares do sangue periférico, e metadados de idade e sexo. |
| GSE28521  | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28521 | Dados públicos do [GEO](https://www.ncbi.nlm.nih.gov/gds), contendo amostras do cérebro humano post-mortem, para os grupos controle e TEA, extraindo RNA-seq de mRNA com normalização log2 do Cortex Frontal, Cerebelo e Lobo Temporal, e metadados de idade e sexo. |
| GSE18123 | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=gse18123 | Dados públicos do [GEO](https://www.ncbi.nlm.nih.gov/gds), contendo amostras de sangue de humanos controle e com TEA, extraindo RNA-seq de mRNA com normalização log2 por células sanguíneas, e metadados de idade e sexo. |
| SFARI gene | https://gene.sfari.org/ | Conecta informações sobre genes candidatos ao autismo do módulo principal “Human Gene” a dados de diversos módulos complementares. |


Durante as pesquisas deste trabalho, foi identificada a plataforma [SFARI gene](https://gene.sfari.org/), que conecta informações sobre genes candidatos ao autismo do módulo principal “Human Gene” a dados de diversos módulos complementares. Os genes de risco para o TEA (Transtorno do Espectro Autista) são então pontuados segundo um conjunto de regras de anotação chamados de “gene-score” e classificados em categorias conforme o nível de evidência que apoia sua relação com o autismo. A plataforma hoje não possui dados separados por sexo, mas classifica as informações por cromossomos. Com isso, os bancos de dados do [SFARI gene](https://gene.sfari.org/), foram utilizados para contextualização biológica, de forma a consultar as classificações de genes segundo seu nível de evidência para associação com TEA, atribuindo gene scores entre 1 (evidência mais forte) e 3. Além disso, o [SFARI gene](https://gene.sfari.org/) também organiza genes por cromossomo, permitindo avaliar se genes encontrados nos outros datasets apresentavam histórico de associação com TEA.

Como fonte de dados, foram identificados datasets na base [GEO](https://www.ncbi.nlm.nih.gov/gds) (Gene Expression Omnibus), repositório público de dados de genômica funcional, funcionando como suporte a submissões de dados baseados em arrays e sequenciamento, além de conter ferramentas de análise e download dos dados já com alguns tratamentos. 

O dataset do GEO [GSE102741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm), foi usado no estudo de Wright et al. (2017) que demonstrou que, embora genes individuais ligados à sinalização histaminérgica não atinjam significância após correção múltipla, o conjunto desses genes apresenta alteração coletiva no córtex pré-frontal dorsolateral de indivíduos com TEA, sugerindo que vias moduladoras de cognição, sono e neuroinflamação podem contribuir para o fenótipo observado. Esta base contém amostras do cérebro humano pós-mortem (córtex pré-frontal dorsolateral) com normalização RPKM, para os grupos TEA e controle. Além disso, metadados sobre idade e sexo estão disponíveis no dataset. Como tratamento para uso nas análises, as amostras foram filtradas por critério de idade, mantendo apenas as relacionadas à indivíduos adultos (com mais de 18 anos) e separadas para o sexo masculino e feminino. Percebeu-se nesta base um certo desbalanceamento entre as classes da base [GSE102741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm) após os tratamentos, com 18 amostras controle (3 do sexo feminino e 15 do sexo masculino) e 6 amostras relacionadas ao TEA (1 do sexo feminio e 5 do sexo masculino). Este processamento foi realizado por meio da ferramenta [Orange](https://orangedatamining.com/). O workflow construído para esta etapa está mostrado na figura abaixo.


![Orange_preprocessing_workflow.png](assets/images/Orange_preprocessing_workflow.png)


A média de log2 RPKM foi calculada para ambos os grupos, com a ferramenta [GraphPad Prism](https://www.graphpad.com/features). Ainda no [Orange](https://orangedatamining.com/), foram filtrados os genes ruidosos e de baixa expressão (remoção dos valores com média de log2 RPKM menor que 0.5). A figura abaixo mostra o workflow da pipeline até esta etapa.

![Differential_expression_workflow.png](assets/images/Differential_expression_workflow.png)

Portanto, foram obtidos 4 grupos de análise:
    - Genes exclusivamente abundantes em grupos TEA (masculino e feminino)
    - Genes exclusivamente abundantes entre grupos específicos (TEA e Controle)
    - Genes diferencialmente expressos entre grupos com TEA (masculino e feminino)
    - Genes diferencialmente expressos entre todos os grupos (TEA e Controle)


Com relação à base [E-MTAB-13871](https://www.omicsdi.org/dataset/biostudies-arrayexpress/E-MTAB-13871) do ArrayExpress foram separados para análise apenas os Genes diferencialmente expressos em todos os grupos (neurodivergentes vs neurotípicos), utilizando o mesmo workflow detalhado acima. Este dataset contem amostras de sangue de humanos controle e de humanos com TEA, extraindo RNA-seq de mRNA com normalização binomial negativa por células mononucleares do sangue periférico, além de metadados de idade e sexo.

Além disso, de forma a enriquecer as análises com maior disponibilidade de dados, foram incluidos os datasets [GSE28521](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28521) (cérebro) e [GSE18123](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=gse18123) (sangue). A série [GSE28521](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28521), de Voineagu et al. (2011), identifica desorganização da arquitetura transcriptômica cortical, incluindo atenuação das diferenças típicas entre córtex frontal e temporal, além de módulos de co-expressão alterados. Entre eles, destaca-se um módulo neuronal enriquecido para genes de risco ao TEA e um módulo imune/glial associado a respostas reativas. Já a série [GSE18123](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=gse18123), é utilizada no estudo de Kong et al., 2012, em que é demonstrado que assinaturas de expressão gênica no sangue podem discriminar indivíduos com TEA, principalmente homens, com desempenho moderado (AUC ≈ 0,70). A baixa acurácia em mulheres destaca a relevância de diferenças sexuais em biomarcadores e sugere heterogeneidade biológica que deve ser contemplada em modelos diagnósticos. Essas últimas bases apresentadas possuem normalização em log2.


Por fim, as bases [GSE102741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm), [GSE28521](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28521) e [GSE18123](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=gse18123) foram integradas, desta vez não realizando o filtro por idade, porém foram removidos genes de baixa significância (p-valor maior que 0.05) e de baixa expressão (log2FC menor que 0.7).Para este processamento, foi utilizado o GEO2R de forma a visualizar plots dos dados, e o [Orange](https://orangedatamining.com/) para filtragem se ruído e significância. O workflow está mostrado na figura abaixo.

![workflow_3_bases.png](assets/images/workflow_3_bases.png)

Códigos auxiliares em Python também foram utilizados, além dos processamentos feitos no [Orange](https://orangedatamining.com/).


## Modelo Lógico

O grafo pode ser organizado em camadas, incluindo: genes codificadores, lncRNAs, elementos epigenéticos (picos/DMRs) e anotação de genes de risco. As arestas podem representar a co-expressão entre genes/lncRNAs ou relações com elementos epigenéticos. Cada nó pode ter atributos como expressão média por sexo, pertencimento a genes de risco e detectabilidade em tecidos periféricos. A figura abaixo mostra o modelo lógico da base de grafos para este projeto.

![alt text](assets/images/modelo_logico.jpg)


## Integração entre Bases

Os processamentos com filtros de sexo e idade foram feitos de forma separada por base de dados, obtendo arquivos temporários que foram utilizados nas análises. Já os processamentos relacionados a remoção de genes com baixa expressão e significância, foram feitos em conjunto, independendo da junção de bases de dados. Os maiores desafios envolveram o tratamento inicial dos dados brutos e link com os metadados fornecidos, que nem sempre são disponibilizados em uma estrutura de fácil compreensão.


## Análises Realizadas

A primeira análise realizada, envolveu retirar alguns insights do [SFARI gene](https://gene.sfari.org/), envolvendo a pesquisa sobre as proteínas comumente associadas ao autismo e os grupos funcionais recorrentes em proteínas autismo-relacionadas. Além disso, foi feita uma análise de distribuição de genes-scores do SFARI. 

Para a análise do dataset [GSE102741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm), foram utilizados os dados processados, detalhados na seção Bases de Dados e Evolução. Estes dados foram representados em grafos utilizando a ferramenta [Cytoscape](https://cytoscape.org/), com objetivo de visualizar os genes com maior abundância em indivíduos com TEA masculinos e femininos e entre ambos os grupos de análise (TEA e controle). As ferramentas [Genome Browser](https://genome.ucsc.edu/) e [GeneLoc](https://geneloc.weizmann.ac.il//index.shtml) foram utilizadas para a anotação de idiogramas. Foi realizada, também, uma análise de enriquecimento por meio da ferramentas [Enrichr](https://maayanlab.cloud/Enrichr/) e [David Bioinformatics](https://davidbioinformatics.nih.gov/), com objetivo de determinar os perfis funcionais, de localização e processuais exclusivos para os genes diferencialmente expressos associados ao TEA em indivíduos femininos e masculinos, identificando assim a divergência molecular por sexo.

Para a análise e enriquecimento, a pesquisa foi focada nas três categorias principais da Gene Ontology (GO), utilizando a biblioteca mais recente para a espécie em estudo:
   - **GO Biological Process (BP)**: Processos e vias biológicas.
   - **GO Cellular Component (CC)**: Localização e estruturas celulares.
   - **GO Molecular Function (MF)**: Funções e atividades moleculares elementares.

Por fim, foram realizadas as análises de expressão diferencial entre grupos com TEA (masculino e feminino) e entre todos os grupos (TEA e controle)

Para o dataset [E-MTAB-13871](https://www.omicsdi.org/dataset/biostudies-arrayexpress/E-MTAB-13871), assim como no GSE102741, foram utilizadas as ferramentas [Cytoscape](https://cytoscape.org/) para representação em grafos e [Enrichr](https://maayanlab.cloud/Enrichr/) e [David Bioinformatics](https://davidbioinformatics.nih.gov/) para enriquecimento. Foi realizada a análise de expressão diferencial para o caso entre todos os grupos (TEA e controle), seguida por uma análise de co-expressão entre cérebro (GSE102741) e sangue (E-MTAB-13871), comparando TEA e controle para os sexos masculino e feminino, e comparação entre TEA masculino e TEA feminino.

Ao integrar as bases [GSE102741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm), [GSE28521](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28521) e [GSE18123](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=gse18123), foi montada uma rede no [Cytoscape](https://cytoscape.org/) com os dados processados de forma a avaliar padrões de interação entre os genes e realizar análises de clustering e identificação de genes diferencialmente expressos. A ferramenta [GEO2R](https://www.ncbi.nlm.nih.gov/geo/geo2r/) foi utilizada para produzir Volcano plots para as análises de expressão diferencial. Códigos em Python também foram utilizados para visualizações.

De forma a relacionar as descobertas com os dados do [SFARI gene](https://gene.sfari.org/), a matriz de expressão final foi combinada com dados do SFARI, possibilitando: (a) checar se genes diferenciais possuíam score SFARI; (b) analisar distribuição cromossômica dos genes de alto score; e (c) investigar se genes identificados como “centrais” nas redes de coexpressão já estavam relacionados a mecanismos sinápticos, neurais ou imunológicos previamente implicados no TEA. 


## Evolução do Projeto

Dentre os principais desafios encontrados para o cumprimento da proposta inicial, destaca-se a não diferenciação por sexo em algumas bases (como é o caso do SFARI) e poucas amostras disponíveis do sexo feminino, que pode estar associada com a menor taxa de diagnósticos de TEA em pessoas do sexo feminino, como discutido na fundamentação teórica. Este fato gerou algumas mudanças de rumo com relação ao que foi aporesentado na entrega 2, que envolveram o acréscimo de mais bases de dados no estudo, que não estavam previstas de serem analisadas anteriormente. Além disso, uma análise mais detalhada dos dados do SFARI foi necessária para a compreensão maior dos resultados.

# Ferramentas

- [Orange](https://orangedatamining.com/)
- [GraphPad Prism](https://www.graphpad.com/features)
- [Cytoscape](https://cytoscape.org/)
- [SFARI gene](https://gene.sfari.org/)
- [AutDB](https://ngdc.cncb.ac.cn/databasecommons/database/id/3574)
- [Genome Browser](https://genome.ucsc.edu/)
- [GeneLoc](https://geneloc.weizmann.ac.il//index.shtml)
- [Enrichr](https://maayanlab.cloud/Enrichr/)
- [TargetMine](https://targetmine.mizuguchilab.org/)
- [David Bioinformatics](https://davidbioinformatics.nih.gov/)


# Resultados e Discussão


As proteínas associadas ao autismo decorrente de estudos prévios tendem a se agrupar em três grandes redes funcionais (ABRAHAM et al, 2019; BOURGERON, 2015):

![alt text](assets/images/redes_funcionais_proteinas.png)

Ao integrar os dados com o [SFARI gene](https://gene.sfari.org/), verificou-se que uma parcela dos genes identificados nas análises já possuía registro de associação com TEA, especialmente genes presentes nos módulos neuronais. Além disso, a plataforma evidenciou três grandes grupos funcionais recorrentes em proteínas autismo-relacionadas: (1) vias sinápticas; (2) regulação transcricional; e (3) imunomodulação, padrões coerentes com os módulos encontrados nas redes de coexpressão.

A análise de distribuição de gene scores revelou forte representação de genes SFARI score 1 e 2 nos cromossomos 7, 15, 17 e X, sendo o cromossomo X particularmente destacado, embora os genes diferenciais encontrados neste estudo tenham se distribuído principalmente nos cromossomos 1 e 15, e não de forma concentrada em X ou Y. Isso indica que, apesar do reconhecimento prévio do papel do cromossomo X no TEA, a expressão diferencial sexo-específica observada neste conjunto de dados não dependeu majoritariamente de genes ligados ao sexo. A figuras abaixo mostram os genes mais referenciados no SFARI.


![alt text](assets/images/genes_mais_expressos_sfari.png)

![alt text](assets/images/grafico_genes_sfari.png)

Ao analisar a distribuição de gene Score 1 por Cromossomo no SFARI, foram obtidos o seguinte gráfico:

![alt text](assets/images/genes_score1.png)

Os gene-scores por cromossomo mostram como os níveis de evidência dos genes variam em cada região do genoma. No gráfico é possível observar a proporção de genes com alta evidência científica (score 1) por cromossomo. Aqui novamente o cromossomo X aparece em destaque.

Ainda, quando observamos o boxplot da distribuição dos gene-scores por cromossomo, alguns cromossomos (como 7, 15, 17 e X) têm medianas mais baixas, indicando uma maior concentração de genes com forte evidência (score 1–2) de associação ao autismo.

![alt text](assets/images/boxplot_score1.png)


Com relação às análises feitas para dados do cérebro ([GSE102741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm)). Foram obtidos os seguintes resultados para cada uma das análises:

- Análise de abundância dos genes para o grupo com TEA
![alt text](assets/images/abundancia_exclusivas_neurodivergentes.png)
![alt text](assets/images/idiograma_neurodivergentes.png)
![alt text](assets/images/enriquecimento_neurodivergentes.png)

- Análise de abundância dos genes para os grupos TEA e Controle
![alt text](assets/images/abundancia_exclusivas_neurodivergentes_controle.png)
![alt text](assets/images/idiograma_entre_grupos.png)
![alt text](assets/images/enriquecimento_tea_controle.png)

- Análise de expressão diferencial para TEA e controle
![alt text](assets/images/expressao_diferencial_tea_controle1.png)
![alt text](assets/images/expressao_diferencial_tea_controle2.png)
![alt text](assets/images/expressao_diferencial_tea_controle3.png)

- Análise de expressão diferencial para indivíduos com TEA
![alt text](assets/images/expressao_diferencial_tea.png)

- Rede de co-expressão obtida (nós representam os genes, as arestas as interações entre os genes, as cores representam os clusters e o tamanho do nó a medida de centralidade)
![alt text](assets/images/rede_coexpressao_cerebro.png)

- Rede de co-expressão para genes expressos em amostras TEA e controle (nós representam os genes, as arestas as interações entre os genes e o tamanho do nó a medida de centralidade)
![alt text](assets/images/coexpressao_tea_controle.jpeg)

- Rede de co-expressão para genes expressos somente em amostras TEA (nós representam os genes, as arestas as interações entre os gene e o tamanho do nó a medida de centralidade)
![alt text](assets/images/coexpressao_tea.jpeg)


Já para dados de sangue ([E-MTAB-13871](https://www.omicsdi.org/dataset/biostudies-arrayexpress/E-MTAB-13871)). Foram obtidos os seguintes resultados para as análises testadas:

- Análise de expressão diferencial para TEA e controle
![alt text](assets/images/volcano_tea_controle_masc.png)
![alt text](assets/images/volcano_tea_fem_controle_masc.png)

Devido a ausência de replicatas biológicas entre os grupos TEA feminino e Controle feminino, a análise de significância estatística (p-valor) não pôde ser realizada. Os resultados reportados refletem apenas a magnitude da alteração (Log2 Fold Change) e não a confiança estatística.


Para a análise de co-expressão entre cérebro e sangue, foram obtidos os seguintes resultados (os nós representam os genes, o tamanho e coloração dos nós indicam a variação de log2 fold change, as arestas representam o tipo de amostra onde o gene foi identificado)

- Controle vs TEA masculino
![alt text](assets/images/coexpressao_masc.png)

- Controle vs TEA feminino
![alt text](assets/images/coexpressao_fem.png)
    - Para o caso feminino, o ARC é um biomarcador promissor. Ele participa de vias relacionadas ao autismo e outros processos de regulação sináptica em transtornos como esquizofrenia, estresse e ansiedade.

- TEA feminino vs controle masculino
![alt text](assets/images/coexpressao_tea_fem_control_masc.png)

Nas análises comparativas entre cérebro e sangue, observou-se que não houve intersecção significativa de genes diferenciais em homens, mas quatro genes coincidiram entre os tecidos em mulheres: ARC, FAM153CP, XRRA1 e Y_RNA. Destes, ARC (score alto no SFARI e amplamente associado à plasticidade sináptica) emergiu como um gene de especial relevância: estava up-regulado no cérebro e down-regulado no sangue, um padrão consistente com sua participação em regulação sináptica pós-sináptica e com modelos etiológicos do TEA envolvendo sinaptopatia. Essa convergência multidataset, aliada ao histórico robusto no SFARI, sugere ARC como forte candidato a biomarcador sexo-específico para TEA feminino. Por outro lado, genes diferenciais no sangue masculino não apresentaram associação SFARI, reforçando heterogeneidade molecular por sexo. No dataset E-MTAB-13871, a ausência de replicatas femininas limitou a significância estatística, mas permitiu observar tendências funcionais coerentes com vias associadas ao TEA no SFARI, sobretudo sinápticas e imunológicas.


Para a análise em conjuntos dos datasets [GSE102741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm), [GSE28521](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28521) e [GSE18123](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=gse18123). Foram obtidos:

- Volcano plots obtidos pelo GEO2R

![alt text](assets/images/volcano_3_data.png)

- Rede resultante no Cytoscape após filtragem (nós representam os genes, as arestas as interações entre os genes. À esquerda mostra-se os nós com tamanho proporcional à centralidade)

![alt text](assets/images/redes_3_data.png)

Genes como MALAT1, NEAT1, FMNL1 e NEFH foram superexpressos em indivíduos neurodivergentes, indicando maior atividade neuronal e desregulação da arquitetura celular, enquanto genes imunes como IL1B, CXCL8, C1QB, CD14 e APOC1 estavam reprimidos, sugerindo alterações neuroimunes. A análise de redes revelou módulos neuronais (GAD1, GAD2, PVALB, SCN1B), imunológicos (C1QB, CD163) e inflamatórios (FOS, IL1B), consistentes com literatura sobre desequilíbrio excitatório-inibitório e neuroinflamação no TEA.


# Conclusão

A integração de múltiplos bancos transcriptômicos com dados do SFARI Gene permitiu identificar padrões consistentes de expressão diferencial e módulos biológicos associados ao TEA, destacando diferenças entre sexos e entre tecidos. Embora não tenham sido encontradas associações relevantes com genes de eixos hormonais, vários genes identificados já possuíam evidência SFARI, reforçando sua relevância biológica. 


A análise sexo-específica destacou ARC como principal candidato a biomarcador feminino, sustentado tanto por sua expressão diferencial em cérebro e sangue quanto por sua classificação SFARI em vias ligadas a plasticidade sináptica. A ausência de padrões fortes no cromossomo X entre os genes diferenciais sugere que mecanismos sexo-específicos no TEA podem depender mais de redes funcionais do que de localização cromossômica. 

Dentre os principais desafios encontrados encontra-se a não diferenciação por sexo em algumas bases (como é o caso do SFARI) e poucas amostras do sexo feminino. Além disso, as bases de dados encontradas não possuem dados específicos que poderiam enriquecer a análise, tais como a identificação de amostras por nível de gravidade e sintomatologia, visto que grande parte das diferenças entre homens e mulheres identificadas em estudos anteriores pode ter relação com a forma como o transtorno é expresso. Isso abre caminho para que próximos estudos levem em consideração dados desse tipo, possibilitando o refinamento da compreensão molecular sexo-específica no TEA.


Com relação às perguntas de pesquisa:

1. É possível identificar genes centrais e módulos de expressão que diferenciam amostras de neurodivergentes femininos e masculinos? É possível ampliar o escopo de comparação entre neurodivergentes e neurotípicos?

    Foi possível criar módulos ou grupos de análise a partir da filtragem dos dados. Os genes “centrais” para nossas redes, são aqueles que fazem intersecção entre módulos/grupos.

2. A expressão destes genes centrais, se relaciona com a co-expressão de genes de hormonas sexuais regulados pelo eixo hipotálamo-hipófise de maneira diferencial?
    
    Não encontramos co-expressão de genes centrais identificados com genes de hormonas sexuais.

3. Os genes centrais identificados aqui  já foram previamente associados ao TEA?

    Sim! Alguns dos genes centrais identificados já foram associados ao TEA! O que é um bom indicativo de correlação entre a expressão diferencial e a possibilidade de propô-lo como biomarcadores!

4. Existe correlação entre os genes centrais identificados e a localização cromossomal em X e Y?

    Não. A localização dos genes centrais identificados não está enviesada para os cromossomos X e Y. Observamos uma alta frequência de genes centrais nos cromossomos 15  e 1. 

5. Existe correlação entre os genes centrais identificados no cérebro e no sangue? É possível propô-los como biomarcadores?

    Sim! Encontramos duas intersecções, mas a mais interessante foi: ARC (para TEA feminino, comparado a indivíduos neurotípicos femininos). O fold change foi de pelo menos 2x, o que talvez já poderia ser um indicativo de um biomarcador para TEA feminino no sangue?*


# Trabalhos Futuros

Mais estudos são necessários, com um maior número de amostras/replicatas de TEA feminino para avaliar a robustez estatística, o que acabou sendo uma limitação deste estudo. Além disso, estudos com bases maiores de dados contendo metadados para a diferenciação clara entre sexos podem ocorrer para a obtenção de resultados mais consistentes e mais significantes cientificamente. Além disso, metadados relacionados à gravidade do TEA nos indivíduos das amostras coletadas podem ser determinantes para os resultados. Isso abre caminho para que próximos estudos levem em consideração dados desse tipo, possibilitando o refinamento da compreensão molecular sexo-específica no TEA.


# Referências Bibliográficas

- Gupta, A., & Bhat, A. (2019). Sex differences in autism spectrum disorder: Diagnostic, neurobiological and clinical aspects. Frontiers in Psychiatry, 10, 607. https://doi.org/10.3389/fpsyt.2019.00607

- Halladay, A. K., Bishop, S. L., Constantino, J. N., Daniels, A. M., Koenig, K., Palmer, K., Messinger, D., Pelphrey, K., Sanders, S. J., Singer, A. T., Taylor, J. L., & Szatmari, P. (2015). Sex and gender differences in autism spectrum disorder: summarizing evidence gaps and identifying emerging areas of priority. Molecular Autism, 6, 36. https://doi.org/10.1186/s13229-015-0019-y

- Lin L, et al. Integrated Analysis of Brain Transcriptome Reveals Convergent Molecular Pathways in Autism Spectrum Disorder. Front Psychiatry. 2019;10:706.
Napolitano, L., Ferri, R., & Di Filippo, G. (2022). Sex differences in autism spectrum disorder: diagnostic, neurobiological and clinical aspects. Frontiers in Psychiatry, 13, 889636. https://doi.org/10.3389/fpsyt.2022.889636 

- Voineagu, I., et al. (2011). Transcriptomic analysis of autistic brain reveals convergent molecular pathology. Nature, 474(7351), 380–384. https://doi.org/10.1038/nature10110 

- Willsey AJ, et al. Coexpression networks implicate human midfetal deep cortical projection neurons in the pathogenesis of autism. Cell. 2013;155(5):997–1007. PMID: 24138891 

- AMERICAN PSYCHIATRIC ASSOCIATION. Manual diagnóstico e estatístico de transtornos mentais: DSM-5. 5. ed. Porto Alegre: Artmed, 2014.

- ABRAHAM, Joseph R. et al. Proteomic Investigations of Autism Brain Identify Known and Novel Pathogenetic Processes. Scientific Reports, v. 9, n. 1, art. 13118, 11 sept. 2019. DOI: 10.1038/s41598-019-49533-y.

- BOURGERON, Thomas. From the genetic architecture to synaptic plasticity in autism spectrum disorder. Nature Reviews Neuroscience, v. 16, n. 9, p. 551–563, 2015. DOI: 10.1038/nrn3992.

- COSTA-MATTIOLI, Mauro; MONTEGGIA, Lisa M. mTOR complexes in neurodevelopmental and neuropsychiatric disorders. Nature Neuroscience, v. 16, n. 11, p. 1537–1543, 2013. DOI: 10.1038/nn.3546.

- LIU, Wenlong et al. Integration of Urine Proteomic and Metabolomic Profiling Reveals Novel Insights Into Neuroinflammation in Autism Spectrum Disorder. Frontiers in Psychiatry, v. 13, 2022. DOI: 10.3389/fpsyt.2022.780747.

- KONG, Sek Won et al. Characteristics and predictive value of blood transcriptome signature in males with autism spectrum disorders. PLoS ONE, v. 7, n. 12, e49475, dez. 2012. DOI: 10.1371/journal.pone.0049475.

- PARIKSHAK, Neelroop N.; GANDAL, Michael J.; GESCHWIND, Daniel H. Systems biology and gene networks in neurodevelopmental and neurodegenerative disorders. Nature Reviews Genetics, v. 16, p. 441–458, 2015. DOI: 10.1038/nrg3934.

- CDC — CENTERS FOR DISEASE CONTROL AND PREVENTION. Prevalence and Early Identification of Autism Spectrum Disorder Among Children Aged 4 and 8 Years — Autism and Developmental Disabilities Monitoring Network, 16 Sites, United States, 2022. MMWR Surveillance Summaries, 2025;74(SS-2). Disponível em: https://www.cdc.gov/mmwr/volumes/74/ss/ss7402a1.htm

- CORBETT, B. A. et al. Camouflaging in Autism: Examining Sex-Based and Compensatory Models in Social Cognition and Communication. Autism Res. 2021 Jan;14(1):127-142. doi: 10.1002/aur.2440. Epub 2020 Nov 21. PMID: 33220170; PMCID: PMC7986572.

- COOK, J. L. et al. Camouflaging in autism: A systematic review. Journal of Autism and Developmental Disorders, 2021. Clin Psychol Rev. 2021 Nov;89:102080. doi: 10.1016/j.cpr.2021.102080. Epub 2021 Sep 6. PMID: 34563942.

- HULL, L.; PETRIDES, K. V.; MANDY, W. The Female Autism Phenotype and Camouflaging: a Narrative Review. Review Journal of Autism and Developmental Disorders, v.7, p.306–317, 2020. DOI: 10.1007/s40489-020-00197-9.

- GOCKLEY, J. et al. The female protective effect in autism spectrum disorder is not mediated by a single genetic locus. Molecular Autism, v.6, art. 25, 2015. DOI: 10.1186/s13229-015-0014-3.

- KAUR, M.; COSTELLO, J.; WILLIS, E.; KELM, K.; REFORMAT, M. Z.; BOLDUC, F. V. Deciphering the diversity of mental models in neurodevelopmental disorders: knowledge graph representation of public data using natural language processing. Journal of Medical Internet Research, v. 24, n. 8, e39888, 5 ago. 2022. DOI: 10.2196/39888. Disponível em: https://pubmed.ncbi.nlm.nih.gov/35930346/

- PROSPERI, M. et al. Sex Differences in Autism Spectrum Disorder. Frontiers in Integrative Neuroscience, 2021.

- SAURE, E. et al. Intellectual disabilities moderate sex/gender differences in ... Journal of Intellectual Disability Research, 2023.

- WERLING, D. M.; GESCHWIND, D. H. Sex differences in autism spectrum disorders. Current Opinion in Neurology, 2013.

- WIGDOR, E. M. et al. The female protective effect against autism spectrum disorder. Cell Genomics, v.2, 2022. DOI: 10.1016/j.xgen.2022.100134.
