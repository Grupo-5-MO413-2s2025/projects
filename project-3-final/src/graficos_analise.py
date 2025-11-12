import pandas as pd
import matplotlib.pyplot as plt

#dados
dados_female = '/cérebro/female_asd_de.csv' 
df_f         = pd.read_csv(dados_female)

dados_male = '/cérebro/male_asd_de.csv' 
df_m       = pd.read_csv(dados_male)

#primeiro, dados female

#definição de limites
limite_superior_x = 1  
limite_inferior_x = -1
limite_y = 1.3

#figura
plt.figure(figsize=(12, 6))

#acima do limite superior x e acima do limite y
acimax_acimay = (df_f['log2_FC'] >= limite_superior_x) & (df_f['-log10_p-value'] >= limite_y)
plt.scatter(df_f[acimax_acimay]['log2_FC'], df_f[acimax_acimay]['-log10_p-value'], color='red', label=f'Time > {limite_superior_x}', alpha=1, s=50)

#entre limites do x e acima do limite y
entrex_acimay = (df_f['log2_FC'] > limite_inferior_x) & (df_f['log2_FC'] < limite_superior_x) & (df_f['-log10_p-value'] >= limite_y)
plt.scatter(df_f[entrex_acimay]['log2_FC'], df_f[entrex_acimay]['-log10_p-value'], color='black', label='Time', alpha=1, s=50)

#abaixo do limite inferior x e acima do limite y
abaixox_acimay = (df_f['log2_FC'] <= limite_inferior_x) & (df_f['-log10_p-value'] >= limite_y)
plt.scatter(df_f[abaixox_acimay]['log2_FC'], df_f[abaixox_acimay]['-log10_p-value'], color='blue', label=f'Time ≤ {limite_inferior_x}', alpha=1, s=50)

#abaixo do limite y
abaixoy = (df_f['-log10_p-value'] < limite_y)
plt.scatter(df_f[abaixoy]['log2_FC'], df_f[abaixoy]['-log10_p-value'], color='black', label=f'Time ≤ {limite_inferior_x}', alpha=1, s=50)


#referência de limite
#plt.axvline(x=limite_superior_x, color='blue', linestyle='--', linewidth=1.5, label=f'limite (time={limite})')

#legendas
plt.xlabel('log2 FC', fontsize=12)
plt.ylabel('-log10 p-value', fontsize=12)
plt.title('FC vs p-value', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
input()

#agora male

plt.figure(figsize=(12, 6))

#acima do limite superior x e acima do limite y
acimax_acimay = (df_m['log2_FC'] >= limite_superior_x) & (df_m['-log10_p-value'] >= limite_y)
plt.scatter(df_m[acimax_acimay]['log2_FC'], df_m[acimax_acimay]['-log10_p-value'], color='red', label=f'Time > {limite_superior_x}', alpha=1, s=50)

#entre limites do x e acima do limite y
entrex_acimay = (df_m['log2_FC'] > limite_inferior_x) & (df_m['log2_FC'] < limite_superior_x) & (df_m['-log10_p-value'] >= limite_y)
plt.scatter(df_m[entrex_acimay]['log2_FC'], df_m[entrex_acimay]['-log10_p-value'], color='black', label='Time', alpha=1, s=50)

#abaixo do limite inferior x e acima do limite y
abaixox_acimay = (df_m['log2_FC'] <= limite_inferior_x) & (df_m['-log10_p-value'] >= limite_y)
plt.scatter(df_m[abaixox_acimay]['log2_FC'], df_m[abaixox_acimay]['-log10_p-value'], color='blue', label=f'Time ≤ {limite_inferior_x}', alpha=1, s=50)

#abaixo do limite y
abaixoy = (df_m['-log10_p-value'] < limite_y)
plt.scatter(df_m[abaixoy]['log2_FC'], df_m[abaixoy]['-log10_p-value'], color='black', label=f'Time ≤ {limite_inferior_x}', alpha=1, s=50)

plt.xlabel('log2 FC', fontsize=12)
plt.ylabel('-log10 p-value', fontsize=12)
plt.title('FC vs p-value', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
input()