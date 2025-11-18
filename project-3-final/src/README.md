# src codes

2025.2 Ciência e Visualização de Dados em Saúde

# Projeto: Redes transcriptômicas relacionadas ao autismo: diferenças sexuais e de desenvolvimento no cérebro humano
# Project: Transcriptomic networks related to autism: sex and developmental differences in the human brain

# Descrição Resumida do Projeto

O projeto tem como objetivo identificar módulos de co-expressão gênica que contenham lncRNAs (RNA longos que não codificam proteínas mas tem papel fundamental no controle da expressão de genes) e genes de risco para TEA (Transtorno do Espectro Autista), observando se há diferenças na forma como eles se comportam em cérebros de indivíduos com diagnóstico de TEA de sexos diferentes. Para tanto, será dado enfoque especial em genes regulados por hormônios sexuais (AR – receptor androgênico, ESR1/2 – receptores de estrogênio, etc.), visando identificar se a expressão gênica e a conectividade de módulos co-expressos podem apresentar padrões sex-específicos que ajudariam a explicar a maior prevalência de autismo em meninos e possíveis mecanismos regulatórios protetores em meninas.

# Pasta src

Contém códigos auxiliares em Python para análises

# Instruções

- intersection_brain_blood.py:
    - Execução:
        ~~~bash
        python intersection_brain_blood.py

    - Saída: Genes em comum entre amostras de cérebro e sangue para indivíduos com TEA


- volcano_plots.py:
    - Execução:
        ~~~bash
        python volcano_plots.py

    - Saída: Volcano plots para analisar a expressão diferencial nos dados de cérebro (grupos TEA feminino vs masculino, TEA vs controle feminino, TEA vs controle masculino) e sangue (grupos TEA feminino vs masculino e TEA vs controle masculino), salvos na pasta assets/images com prefixo selected.