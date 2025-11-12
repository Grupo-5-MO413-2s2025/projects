import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



ff, FF = '44', 'dd'
size, fsize = 10, 6
colx, coly = 'log2 FC', 'log10 p-value'

files = [
    # ('cérebro/expressão diferencial - somente TEA_feminino em relação ao masculino.csv', 'Somente TEA feminino x TEA masculino'),
    # ('cérebro/expressão diferencial - TEA feminino (em relação ao controle feminino).csv', 'TEA feminino x controle feminino'),
    ('cérebro/expressão diferencial - TEA feminino (em relação ao TEA masculino).csv', 'TEA feminino x TEA masculino'),
    # ('cérebro/expressão diferencial - TEA masculino (em relação ao controle masculino).csv', 'TEA masculino x controle masculino'),
    # ('sangue/expressão diferencial sangue - TEA feminino (em relação ao TEA masculino).csv', 'Sangue TEA feminino x TEA masculino'),
    # ('sangue/expressão diferencial sangue - TEA masculino (em relação ao controle masculino).csv', 'Sangue TEA masculino x controle masculino')
    # ('demo.csv', 'Demo')
]

# selected_genes = ['ENSG00000196071', 'ENSG00000252616', 'ENSG00000239107', 'ENSG00000133800']
# selected_genes = ['ENSG00000251707', 'ENSG00000225623', 'ENSG00000215252', 'ENSG00000198576', 'ENSG00000166435']
# selected_genes = 
# selected_genes = ['ENSG00000199568', 'ENSG00000200156', 'ENSG00000212402', 'ENSG00000202354', 'ENSG00000207142', 'ENSG00000199298']
selected_genes = ['ENSG00000173372', 'ENSG00000173369', 'ENSG00000159189', 'C1QC', 'ENSG00000165168', 'ENSG00000199459', 'ENSG00000252196', 'ENSG00000143858']
# selected_genes = 
# selected_genes = []

xlim_cer = (-2, 2)
ylim_cer = (-0.3, 6.0)

xlim_sangue = (-8.76, 8.76)
ylim_sangue = (-0.3, 6.7)

for fil, name in files:
    df = pd.read_csv(fil, sep=';', decimal=',')

    if 'Sangue' in name:
        df['GeneID'] = df['GeneID'].str.replace(',', '.')
        xlim = xlim_sangue
        ylim = ylim_sangue
        FC, p_value = 1, 1.3
    else:
        xlim = xlim_cer
        ylim = ylim_cer
        FC, p_value = 1, 1.3

    fig, ax = plt.subplots(1, 1, figsize=(8, 6), dpi=150)

    only_positive = df.loc[(df[colx] >= FC) & (df[coly] <= -p_value)]
    only_negative= df.loc[(df[colx] <= -FC) & (df[coly] <= -p_value)]

    all_changed = pd.concat((only_positive, only_negative))
    all_changed.to_csv(f'FC/{name}.csv', index=False)

    ax.scatter(df[colx], -df[coly], color=f'#{ff}{ff}{ff}', s=size)
    for gene in only_positive.iterrows():
        gene_name, x, y = gene[1]
        if gene_name in selected_genes:
            ax.scatter(x, -y, color=f'#{FF}{ff}{FF}', s=size+10, zorder=10)
        else:
            ax.scatter(x, -y, color=f'#{ff}{ff}{FF}', s=size+1)
        # if not 'Sangue' in name:
        #     ax.annotate(gene_name, (x, -y), xytext=(x+.025, -y), color='#000000', fontsize=fsize)
    for gene in only_negative.iterrows():
        gene_name, x, y = gene[1]
        if gene_name in selected_genes:
            ax.scatter(x, -y, color=f'#{FF}{ff}{FF}', s=size+10, zorder=10)
        else:
            ax.scatter(x, -y, color=f'#{FF}{ff}{ff}', s=size+1)
        # if not 'Sangue' in name:
        #     ax.annotate(gene_name, (x, -y), xytext=(x-.42, -y), color='#000000', fontsize=fsize)

    ax.hlines((p_value, p_value), xmin=(xlim[0], FC), xmax=(-FC, xlim[1]), linestyle='--', color='#000000', linewidth=1, zorder=0)
    ax.vlines((-FC, FC), ymin=p_value, ymax=ylim[1], linestyle='--', color='#000000', linewidth=1, zorder=0)

    # ax.hlines((p_value, p_value), xmin=(xlim[0], xlim[0]), xmax=(xlim[1], xlim[1]), linestyle='--', color='#000000', linewidth=1, zorder=0)
    # ax.vlines((-FC, FC), ymin=ylim[0], ymax=ylim[1], linestyle='--', color='#000000', linewidth=1, zorder=0)

    ax.set_xlabel('Log2 FC', fontdict={'fontweight': 'bold', 'fontsize': 12}, zorder=2)
    ax.set_ylabel('-Log10 p-value', fontdict={'fontweight': 'bold', 'fontsize': 12}, zorder=3)
    ax.set_title(f'Volcano plot {name}', fontdict={'fontweight': 'bold', 'fontsize': 15}, zorder=3)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    fig.tight_layout()
    fig.savefig(f'plots/selected_plot_{name}.png', format='png')
    plt.show()