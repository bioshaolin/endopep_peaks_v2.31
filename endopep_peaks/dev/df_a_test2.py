import os
import sys
import subprocess
import re
import glob
import shlex
import operator
from collections import defaultdict
import pandas as pd
import numpy as np


#####################
# FORMAT CHAIN DATA #
#####################

a_df = open("a_df.txt", "r")

#######
#  A  #
#######

		############
		# read_csv #
		############
df_aa = pd.read_csv(a_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','LC1','sn_L_1','LC2','sn_L_2','LC3','sn_L_3','\
LC4','sn_L_4','LC5','sn_L_5','LC6','sn_L_6','HC1','sn_H_1','HC2','sn_H_2','HC3','sn_H_3','HC4','sn_H_4','HC5','sn_H_5','HC6','sn_H_6','Intact1','sn_I_1','Intact2','\
sn_I_2','Intact3','sn_I_3','Intact4','sn_I_4','Intact5','sn_I_5','Intact6','sn_I_6','b_non_A1','sn_ba_1','b_non_A2','sn_ba_2','b_non_A3','sn_ba_3','b_non_A4','\
sn_ba_4','b_non_A5','sn_ba_5','b_non_A6','sn_ba_6','b_non_A7','sn_ba_7','b_non_A8','sn_ba_8','b_non_A9','sn_ba_9','b_non_A10','sn_ba_10','b_non_A11','\
sn_ba_11','b_non_A12','sn_ba_12','b_non_A13','sn_ba_13','b_non_A14','sn_ba_14','b_non_A15','sn_ba_15','b_non_A16','sn_ba_16','b_non_A17','\
sn_ba_17','b_non_A18','sn_ba_18','e_non_A1','sn_ea_1','e_non_A2','sn_ea_2','e_non_A3','sn_ea_3','e_non_A4','sn_ea_4','e_non_A5','sn_ea_5','e_non_A6\
','sn_ea_6','e_non_A7','sn_ea_7','e_non_A8','sn_ea_8','e_non_A9','sn_ea_9','e_non_A10','sn_ea_10','e_non_A11','sn_ea_11','e_non_A12','sn_ea_12','\
','e_non_A13','sn_ea_13','e_non_A14','sn_ea_14','e_non_A15','sn_ea_15','e_non_A16','sn_ea_16','e_non_A17','sn_ea_17','e_non_A18','sn_ea_18','\
','f_non_A1','sn_fa_1','f_non_A2','sn_fa_2','f_non_A3','sn_fa_3','f_non_A4','sn_fa_4','f_non_A5','sn_fa_5','f_non_A6','sn_fa_6','f_non_A7','sn_fa_7','\
','f_non_A8','sn_fa_8','f_non_A9','sn_fa_9','f_non_A10','sn_fa_10','f_non_A11','sn_fa_11','f_non_A12','sn_fa_12','f5_non_A1','sn_f5a_1','\
','f5_non_A2','sn_f5a_2','f5_non_A3','sn_f5a_3','f5_non_A4','sn_f5a_4','f5_non_A5','sn_f5a_5','f5_non_A6','sn_f5a_6','f5_non_A7','sn_f5a_7','\
','f5_non_A8','sn_f5a_8','f5_non_A9','sn_f5a_9','f5_non_A10','sn_f5a_10','f5_non_A11','sn_f5a_11','f5_non_A12','sn_f5a_12','f_non_A13','sn_fa_13','\
','f_non_A14','sn_fa_14','f_non_A15','sn_fa_15','f_non_A16','sn_fa_16','f_non_A17','sn_fa_17','f_non_A18','sn_fa_18'])
print(df_aa)

df_aa.dropna(axis=1, how="all", inplace=True)
print(df_aa)

		#######################
		# formatting A chains #
		#######################
df_aa.columns = df_aa.columns.str.replace('^LC\d+', 'LC_A', regex=True)
s = df_aa.stack()
df_aa = s.unstack()
df_aa.columns = df_aa.columns.str.replace('sn_L_\d+', 'sn_LC_A', regex=True)
s2 = df_aa.stack()
df_aa = s2.unstack()
df_aa.columns = df_aa.columns.str.replace('^HC\d+', 'HC_A', regex=True)
s3 = df_aa.stack()
df_aa = s3.unstack()
df_aa.columns = df_aa.columns.str.replace('sn_H_\d+', 'sn_HC_A', regex=True)
s4 = df_aa.stack()
df_aa = s4.unstack()
df_aa.columns = df_aa.columns.str.replace('^Intact\d+', 'Intact_A', regex=True)
s5 = df_aa.stack()
df_aa = s5.unstack()
df_aa.columns = df_aa.columns.str.replace('sn_I_\d+', 'sn_Intact_A', regex=True)
s6 = df_aa.stack()
df_aa = s6.unstack()

df_aa.drop([col for col in df_aa.columns if 'b_non_A' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'sn_ba_' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'e_non_A' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'sn_ea_' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'f_non_A' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'sn_fa_' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'f5_non_A' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'sn_f5a_' in col], axis=1, inplace=True)



cols = df_aa.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_A')))
cols.insert(4, cols.pop(cols.index('sn_LC_A')))
cols.insert(5, cols.pop(cols.index('HC_A')))
cols.insert(6, cols.pop(cols.index('sn_HC_A')))
cols.insert(7, cols.pop(cols.index('Intact_A')))
cols.insert(8, cols.pop(cols.index('sn_Intact_A')))
df_aa = df_aa.reindex(columns=cols)

df_aa1 = df_aa.drop(df_aa.index[0])
print(df_aa1)
df_aa1.to_csv("a_final_df.txt", sep="\t")
