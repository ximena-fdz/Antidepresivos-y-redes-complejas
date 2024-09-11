################################################################################
# process level 4 (z-score) LINCS data for antidepressants to generate 
# signed top/bottom network 

# author: Ximena Fernandez
# mail:   xfdzciencias@gmail.com

################################################################################

################################################################################
# import modules 
################################################################################

import pandas as pd
import numpy as np
import cmapPy

################################################################################
# data reading 
################################################################################

# read LINCS gctx file 
gctx_file_path = '/datos/LINCS/GSE92742_Broad_LINCS_Level4_ZSPCINF_mlr12k_n1319138x12328.gctx'
df = cmapPy.pandasGEXpress.parse.parse(gctx_file_path)

# read inst file
inst = pd.read_csv("/datos/LINCS/GSE92742_Broad_LINCS_inst_info.txt", sep="\t", low_memory=False)

# read antidepressant list 
ad = pd.read_csv('antidepressants.tsv', sep='\t')

################################################################################
# data filtering 
################################################################################

# get inst info for ADs 

inst

inst_ad = inst[inst['pert_iname'].isin(ad['pert_iname'])]

# filter for selected cell line: NPC

inst_ad_npc = inst_ad[inst["cell_id"]=="NPC"] 

# filter for max dose and max time 

## find max dose and max time
max_values = inst_ad_npc.groupby('pert_iname').agg({'pert_dose': 'max', 'pert_time': 'max'}).reset_index()

## merge to keep rows with max 'pert_dose' and 'pert_time'
filtered_inst_ad_npc = inst_ad_npc.merge(max_values, on=['pert_iname', 'pert_dose', 'pert_time'])

# subset the LINCS z-score data for selected inst_id and convert to data frame 
columns_to_keep = filtered_inst_ad_npc["inst_id"].tolist()
lincs_df = df.data_df[columns_to_keep]

################################################################################
# data mapping
################################################################################

# create a dictionary to map each 'inst_id' to its corresponding 'pert_iname'
column_to_pert_iname = dict(zip(filtered_inst_ad_npc['inst_id'], filtered_inst_ad_npc['pert_iname']))

# subset the cmapPy data frame to keep only the relevant columns (inst_ids)
subset_data_df = df.data_df[filtered_inst_ad_npc['inst_id'].tolist()]

# rename columns based on the 'pert_iname' mapping
subset_data_df = subset_data_df.rename(columns=column_to_pert_iname)

###### (this is unneeded for this particular dataset, but we keep breaking ties
###### through medians calculation for compatibility reasons)
median_df = subset_data_df.groupby(level=0, axis=1).median()

################################################################################
# data ranking and transformations
################################################################################

# rank the LINCS z-score data on ascending order for each AD
ranked_df = median_df.rank(axis=0, method='average', ascending=True)

# signing top/bottom 100

## initialize the top_bottom data frame with zeros
top_bottom = pd.DataFrame(0, index=ranked_df.index, columns=ranked_df.columns)

## iterate over each column to assign +1, -1 based on the rank
for col in ranked_df.columns:
    ### get the indices of the top 100 and bottom 100 ranked values
    top_100_indices = ranked_df[col].nsmallest(100).index
    bottom_100_indices = ranked_df[col].nlargest(100).index
    ### assign +1 to the highest ranked 100 values
    top_bottom.loc[top_100_indices, col] = 1
    ### assign -1 to the lowest ranked 100 values
    top_bottom.loc[bottom_100_indices, col] = -1

# display the new data frame
print(top_bottom.head())

################################################################################
# write out 
################################################################################

# reset the index of the top_bottom DataFrame to get 'rid' as a column
top_bottom_reset = top_bottom.reset_index().rename(columns={"index": "rid"})

# use the melt function to pivot the DataFrame to long format
long_format_df = top_bottom_reset.melt(id_vars='rid', var_name='cid', value_name='value')

long_format_df[long_format_df['value'] != 0].to_csv(path_or_buf = 'filtered_long_format.csv', index=False)
