import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



ff, FF = '44', 'dd'
size, fsize = 10, 6
colx, coly = 'log2 FC', 'log10 p-value'

files = [
    ('cérebro/expressão diferencial - somente TEA_feminino em relação ao masculino.csv', 'Somente TEA feminino x TEA masculino'),
    ('cérebro/expressão diferencial - TEA feminino (em relação ao controle feminino).csv', 'TEA feminino x controle feminino'),
    ('cérebro/expressão diferencial - TEA feminino (em relação ao TEA masculino).csv', 'TEA feminino x TEA masculino'),
    ('cérebro/expressão diferencial - TEA masculino (em relação ao controle masculino).csv', 'TEA masculino x controle masculino'),
    ('sangue/expressão diferencial sangue - TEA feminino (em relação ao TEA masculino).csv', 'Sangue TEA feminino x TEA masculino'),
    ('sangue/expressão diferencial sangue - TEA masculino (em relação ao controle masculino).csv', 'Sangue TEA masculino x controle masculino')
]

# xs = []
# ys = []

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
        ax.scatter(x, -y, color=f'#{ff}{ff}{FF}', s=size+1)
        # if not 'Sangue' in name:
        #     ax.annotate(gene_name, (x, -y), xytext=(x+.025, -y), color='#000000', fontsize=fsize)
    for gene in only_negative.iterrows():
        gene_name, x, y = gene[1]
        ax.scatter(x, -y, color=f'#{FF}{ff}{ff}', s=size+1)
        # if not 'Sangue' in name:
        #     ax.annotate(gene_name, (x, -y), xytext=(x-.42, -y), color='#000000', fontsize=fsize)

    if 'C1Q' in gene_name:
        print(gene_name)

    ax.hlines((p_value, p_value), xmin=(xlim[0], FC), xmax=(-FC, xlim[1]), linestyle='--', color='#000000', linewidth=1, zorder=0)
    ax.vlines((-FC, FC), ymin=p_value, ymax=ylim[1], linestyle='--', color='#000000', linewidth=1, zorder=0)

    ax.set_xlabel('Log2 FC', fontdict={'fontweight': 'bold', 'fontsize': 12}, zorder=2)
    ax.set_ylabel('-Log10 p-value', fontdict={'fontweight': 'bold', 'fontsize': 12}, zorder=3)
    ax.set_title(f'Volcano plot {name}', fontdict={'fontweight': 'bold', 'fontsize': 15}, zorder=3)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    # xs.append(ax.get_xlim())
    # ys.append(ax.get_ylim())

    fig.tight_layout()
    fig.savefig(f'plots/plot_{name}.png', format='png')
    plt.show()

    # raise SystemExit

# xs = np.array(xs)
# ys = np.array(ys)

# print(xs[:-2])
# print(ys[:-2])
# print(f'Min Cérebro X: {min(xs[:-2,0])}')# Min X: -8.741188412349999
# print(f'Max Cérebro X: {max(xs[:-2,1])}')# Max X: 8.11152855335
# print()
# print(f'Min Cérebro Y: {min(ys[:-2,0])}')# Min Y: -0.31689734827640004
# print(f'Max Cérebro Y: {max(ys[:-2,1])}')# Max Y: 6.6548589401084
# print('============')
# print(xs)
# print(ys)
# print(f'Min Sangue X: {min(xs[:,0])}')# Min X: -8.741188412349999
# print(f'Max Sangue X: {max(xs[:,1])}')# Max X: 8.11152855335
# print()
# print(f'Min Sangue Y: {min(ys[:,0])}')# Min Y: -0.31689734827640004
# print(f'Max Sangue Y: {max(ys[:,1])}')# Max Y: 6.6548589401084