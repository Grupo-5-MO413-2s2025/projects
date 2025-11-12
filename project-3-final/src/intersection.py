import pandas as pd



folder = 'FC'

sangue_TEAS_orig = pd.read_csv('FC/Sangue TEA feminino x TEA masculino.csv')
sangue_M_orig = pd.read_csv('FC/Sangue TEA masculino x controle masculino.csv')
sangue_TEAS_orig['initial_alias'] = sangue_TEAS_orig['GeneID']
sangue_M_orig['initial_alias'] = sangue_M_orig['GeneID']

sangue_TEAS_conv = pd.read_csv('FC/sangue_TEAS_conv.csv', usecols=["initial_alias", "converted_alias"])
sangue_M_conv = pd.read_csv('FC/sangue_M_conv.csv', usecols=["initial_alias", "converted_alias"])

sangue_TEAS = sangue_TEAS_conv.merge(sangue_TEAS_orig, on='initial_alias', how='outer')#.drop(['GeneID', 'initial_alias'], axis=1)
sangue_M = sangue_M_conv.merge(sangue_M_orig, on='initial_alias')#.drop(['GeneID', 'initial_alias'], axis=1)

# print(sangue_TEAS_orig.head(20))
# print(sangue_TEAS_conv.head(20))
# print(sangue_TEAS.head(20))

mapper = {
    'converted_alias': 'ensembl_gene_id',
    'log2 FC': 'log2 FC - Sangue',
    'log10 p-value': 'log10 p-value - Sangue'
}
sangue_TEAS.rename(mapper, axis=1, inplace=True)
sangue_M.rename(mapper, axis=1, inplace=True)



cer_TEAS_only = pd.read_csv('FC/Somente TEA feminino x TEA masculino.csv')
cer_TEAS = pd.read_csv('FC/TEA feminino x TEA masculino.csv')
cer_F = pd.read_csv('FC/TEA feminino x controle feminino.csv')
cer_M = pd.read_csv('FC/TEA masculino x controle masculino.csv')



mapper = {
    'log2 FC': 'log2 FC - Cer',
    'log10 p-value': 'log10 p-value - Cer'
}
cer_TEAS_only.rename(mapper, axis=1, inplace=True)
cer_TEAS.rename(mapper, axis=1, inplace=True)
cer_F.rename(mapper, axis=1, inplace=True)
cer_M.rename(mapper, axis=1, inplace=True)

# print(sangue_TEAS.columns)
# print(sangue_M.columns)
# print(cer_TEAS_only.columns)
# print(cer_TEAS.columns)
# print(cer_M.columns)
# print(cer_F.columns)

sangue_x_cer_TEAS_only = sangue_TEAS.merge(cer_TEAS_only, on='ensembl_gene_id')
sangue_x_cer_TEAS = sangue_TEAS.merge(cer_TEAS, on='ensembl_gene_id')
sangue_x_cer_M = sangue_M.merge(cer_M, on='ensembl_gene_id')

print(sangue_x_cer_TEAS_only)
print()
print(sangue_x_cer_TEAS)
print()
print(sangue_x_cer_M)