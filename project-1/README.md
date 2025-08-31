# P1 - Primeira Entrega

2025.2 Ciência e Visualização de Dados em Saúde

# Projeto: Redes transcriptômicas relacionadas ao autismo: diferenças sexuais e de desenvolvimento no cérebro humano
# Project: Transcriptomic networks related to autism: sex and developmental differences in the human brain

# Descrição Resumida do Projeto

O projeto tem como objetivo identificar módulos de co-expressão gênica que contenham lncRNAs (RNA longos que não codificam proteínas mas tem papel fundamental no controle da expressão de genes) e genes de risco para TEA (Transtorno do Espectro Autista), observando se há diferenças na forma como eles se comportam em cérebros de indivíduos com diagnóstico de TEA de sexos diferentes. Para tanto, será dado enfoque especial em genes regulados por hormônios sexuais (AR – receptor androgênico, ESR1/2 – receptores de estrogênio, etc.), visando identificar se a expressão gênica e a conectividade de módulos co-expressos podem apresentar padrões sex-específicos que ajudariam a explicar a maior prevalência de autismo em meninos e possíveis mecanismos regulatórios protetores em meninas.

# Slides

[Redes transcriptômicas relacionadas ao autismo: diferenças sexuais e de desenvolvimento no cérebro humano](https://docs.google.com/presentation/d/1CA42IQ7r6LyheKw27NwXXvC2KR4KoUENd_jR16nD_6Q/edit?slide=id.p#slide=id.p)

# Fundamentação Teórica

- Apesar de haver uma  maior taxa de diagnóstico do TEA em homens do que em mulheres, há uma quantidade surpreendentemente pequena de pesquisas focadas nas razões para essa disparidade (Halladay et al., 2015). Em específico investigar diferenças sexuais no TEA pode ajudar na compreensão da  sintomatologia, opções e resposta a tratamentos (Napolitano et al. , 2022).

- Estudos de transcriptoma do cérebro em desenvolvimento demonstram que genes de risco para TEA e lncRNAs tendem a se organizar em módulos de co-expressão específicos, muitos dos quais têm expressão restrita a janelas temporais críticas, como o período pré-natal e início pós-natal, quando ocorre a formação de circuitos neurais essenciais (Willsey et al., 2013).

- A análise de diferenças sexuais em co-expressão permite investigar possíveis mecanismos de proteção em meninas ou maior suscetibilidade em meninos, servindo como proxy da influência hormonal (Lin L, et al. 2019).

# Perguntas de Pesquisa

1. É possível priorizar genes e lncRNAs com maior relevância funcional para explicar diferenças de risco entre sexos no TEA?

2. Quais lncRNAs e genes hub em módulos sex-específicos são detectáveis em tecidos periféricos (GTEx), indicando potencial biomarcador?

3. Existem módulos com expressão preferencial em janelas temporais críticas (pré-natal ou início pós-natal) que apresentam diferenças sexuais significativas, sugerindo períodos de risco ou proteção?

# Bases de Dados

| Base de Dados  | Endereço na Web    | Resumo descritivo |
|-------|--------|----------------|
| GSE 28521 | ()[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28521&utm]| Dados de microarray do córtex frontal e temporal de indivíduos com autismo e controles (Voineagu et al., 2011) |
| GSE 102741 | ()[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102741&utm] | RNA-Seq de córtex pré-frontal e corpo caloso em autismo  (Gupta et al., 2019)|
| Brain Span – Atlas of the Developing Human Brain | ()[https://www.brainspan.org/?utm] |  Dados de 16 regiões cerebrais humanas ao longo do desenvolvimento.              |
| PsychENCODE | ()[https://www.synapse.org/Synapse:syn4921369/wiki/235539]  | Consórcio internacional com dados multiômicos (RNA-Seq, ChIP-Seq, ATAC-Seq, etc.) de transtornos psiquiátricos, incluindo autismo, esquizofrenia e bipolaridade. |
| SFARI Gene |  ()[https://gene.sfari.org/]| Banco de dados em evolução para a comunidade de pesquisa do autismo, centrado em genes implicados na suscetibilidade ao autismo. |

# Modelo Lógico

- O grafo pode ser organizado em camadas, incluindo: genes codificadores, lncRNAs, elementos epigenéticos (picos/DMRs) e anotação de genes de risco. 

- As arestas podem representar a co-expressão entre genes/lncRNAs ou relações com elementos epigenéticos. 

- Cada nó pode ter atributos como expressão média por sexo, pertencimento a genes de risco e detectabilidade em tecidos periféricos. 


# Metodologia

- O projeto pode utilizar dados públicos de transcriptoma do cérebro em desenvolvimento (BrainSpan, GEO) para identificar módulos de co-expressão que incluam lncRNAs e genes de risco para autismo. 

- A análise visa considerar diferenças entre sexos como proxy da influência hormonal e, quando disponíveis, integrará dados epigenéticos (PsychENCODE) para avaliar regulação. 

# Ferramentas

- As ferramentas principais para a análise podem  incluir R (WGCNA para redes de co-expressão, limma/edgeR para análise de expressão) e Python (NetworkX para manipulação de grafos).

# Referências Bibliográficas

- Gupta, A., & Bhat, A. (2019). Sex differences in autism spectrum disorder: Diagnostic, neurobiological and clinical aspects. Frontiers in Psychiatry, 10, 607. https://doi.org/10.3389/fpsyt.2019.00607

- Halladay, A. K., Bishop, S. L., Constantino, J. N., Daniels, A. M., Koenig, K., Palmer, K., Messinger, D., Pelphrey, K., Sanders, S. J., Singer, A. T., Taylor, J. L., & Szatmari, P. (2015). Sex and gender differences in autism spectrum disorder: summarizing evidence gaps and identifying emerging areas of priority. Molecular Autism, 6, 36. https://doi.org/10.1186/s13229-015-0019-y

- Lin L, et al. Integrated Analysis of Brain Transcriptome Reveals Convergent Molecular Pathways in Autism Spectrum Disorder. Front Psychiatry. 2019;10:706.
Napolitano, L., Ferri, R., & Di Filippo, G. (2022). Sex differences in autism spectrum disorder: diagnostic, neurobiological and clinical aspects. Frontiers in Psychiatry, 13, 889636. https://doi.org/10.3389/fpsyt.2022.889636 

- Voineagu, I., et al. (2011). Transcriptomic analysis of autistic brain reveals convergent molecular pathology. Nature, 474(7351), 380–384. https://doi.org/10.1038/nature10110 

- Willsey AJ, et al. Coexpression networks implicate human midfetal deep cortical projection neurons in the pathogenesis of autism. Cell. 2013;155(5):997–1007. PMID: 24138891 


