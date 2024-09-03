import pandas as pd
import numpy as np
from cmapPy.pandasGEXpress.parse import parse

# Abrir el archivo de genes de LINCS
gctx_file_path = '/datos/LINCS/GSE92742_Broad_LINCS_Level4_ZSPCINF_mlr12k_n1319138x12328.gctx'
data = parse(gctx_file_path)

# Convertir a df
df = data.data_df
print(df.head())

# Importar el archivo LINCS con los datos de las instancias experimentales
inst = pd.read_csv("/datos/LINCS/GSE92742_Broad_LINCS_inst_info.txt", sep="\t", low_memory=False)
print(inst)
print(inst.info())

# Mapear los datos de perturbaciones al df de niveles de expresión génica
inst_selected = inst[['inst_id', 'pert_id', 'pert_iname', 'pert_dose', 'pert_time', 'cell_id']]
inst_selected = inst_selected.set_index('inst_id').loc[df.columns]
df = pd.concat([df, inst_selected.T])

# Importar el archivo de antidepresivos
ad = pd.read_csv('antidepressants.tsv', sep='\t')

# Filtrar las columnas de 'df' incluyendo sólo instancias experimentales usando antidepresivos presentes en 'ad'
filtered_columns = df.loc['pert_iname'].isin(ad['pert_iname'])
df_filtered = df.loc[:, filtered_columns]

# Filtrar las columnas de 'df' incluyendo sólo instancias experimentales usando antidepresivos en tejido nervioso
npc_columns = df.loc['cell_id'] == 'NPC'
df_filtered = df_filtered.loc[:, npc_columns]

# Encontrar las instancias experimentales con máxima dosis y tiempo de exposición dentro de cada 'pert_id'
max_dose = df_filtered.loc['pert_dose'].groupby(df_filtered.loc['pert_id']).transform('max')
max_time = df_filtered.loc['pert_time'].groupby(df_filtered.loc['pert_id']).transform('max')

# Crear una máscara para seleccionar las columnas que cumplen ambas condiciones
mask = (df_filtered.loc['pert_dose'] == max_dose) & (df_filtered.loc['pert_time'] == max_time)

# Filtrar las columnas de 'df' incluyendo sólo las instancias experimentales usando antidepresivos en tejido nervioso con máxima dosis y tiempo de exposición
df_final = df_filtered.loc[:, mask]

print(df_final)

# Calcular la mediana de los niveles de expresión normalizados por gen para cada pert_id
df_filtered_medians = df_final.iloc[:-5].groupby(df_final.loc['pert_id'], axis=1).median()

# Añadir los datos de perturbaciones al df
df_filtered_medians.loc['pert_iname'] = df_final.loc['pert_iname'].groupby(df_final.loc['pert_id']).first()

print(df_filtered_medians)

# Convertir todos los valores de niveles de expresión normalizados por gen a float, ignorando 'pert_iname'
df_filtered_medians_float = df_filtered_medians[df_filtered_medians.index != 'pert_iname'].apply(pd.to_numeric, errors='coerce')

# Inicializar con 0 un df para el ranking de los niveles de expresión por gen para cada pert_id, conservando 'pert_iname'
df_ranking = pd.DataFrame(0, index=df_filtered_medians.index, columns=df_filtered_medians.columns)
df_ranking.loc['pert_iname'] = df_filtered_medians.loc['pert_iname']

# Obtener los top 100 y bottom 100 genes con cambios en los niveles de expresión para cada pert_id y actualizar el ranking
for col in df_filtered_medians.columns:
    sorted_indices = df_filtered_medians_float[col].sort_values(ascending=False).index
    df_ranking.loc[sorted_indices[:100], col] = range(1, 101)
    df_ranking.loc[sorted_indices[-100:], col] = range(-1, -101, -1)

print(df_ranking)

# Crear la matriz de conexiones no ponderadas según si está presente en el ranking de los top 100 (1), bottom 100 (-1) o ausente (0), conservando 'pert_iname'
df_links = df_ranking[df_ranking.index != 'pert_iname'].map(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
df_links.loc['pert_iname'] = df_ranking.loc['pert_iname']

print(df_links)

# Exportar archivo
df_links.to_csv('LINCS_ad_ranked_genes_level4.csv', index=True)

