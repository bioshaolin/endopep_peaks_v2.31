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

e_df = open("e_df.txt", "r")

#######
#  E  #
#######

		############
		# read_csv #
		############
df_ea = pd.read_csv(e_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','LC1','sn_L_1','LC2','sn_L_2','LC3','sn_L_3','LC4','sn_L_4','\
LC5','sn_L_5','LC6','sn_L_6','HC1','sn_H_1','HC2','sn_H_2','HC3','sn_H_3','HC4','sn_H_4','HC5','sn_H_5','HC6','sn_H_6','Intact1','sn_I_1','Intact2','sn_I_2','Intact3','sn_I_3','\
Intact4','sn_I_4','Intact5','sn_I_5','Intact6','sn_I_6','a_non_E1','sn_ae_1','a_non_E2','sn_ae_2','a_non_E3','sn_ae_3','a_non_E4','sn_ae_4','a_non_E5','\
sn_ae_5','a_non_E6','sn_ae_6','a_non_E7','sn_ae_7','a_non_E8','sn_ae_8','a_non_E9','sn_ae_9','a_non_E10','sn_ae_10','a_non_E11','sn_ae_11','\
a_non_E12','sn_ae_12','a_non_E13','sn_ae_13','a_non_E14','sn_ae_14','a_non_E15','sn_ae_15','a_non_E16','sn_ae_16','a_non_E17','sn_ae_17','\
a_non_E18','sn_ae_18','b_non_E1','sn_be_1','b_non_E2','sn_be_2','b_non_E3','sn_be_3','b_non_E4','sn_be_4','b_non_E5','sn_be_5','b_non_E6','\
sn_be_6','b_non_E7','sn_be_7','b_non_E8','sn_be_8','b_non_E9','sn_be_9','b_non_E10','sn_be_10','b_non_E11','sn_be_11','b_non_E12','sn_be_12','\
b_non_E13','sn_be_13','b_non_E14','sn_be_14','b_non_E15','sn_be_15','b_non_E16','sn_be_16','b_non_E17','sn_be_17','b_non_E18','sn_be_18','\
f_non_E1','sn_fe_1','f_non_E2','sn_fe_2','f_non_E3','sn_fe_3','f_non_E4','sn_fe_4','f_non_E5','sn_fe_5','f_non_E6','sn_fe_6','f_non_E7','\
sn_fe_7','f_non_E8','sn_fe_8','f_non_E9','sn_fe_9','f_non_E10','sn_fe_10','f_non_E11','sn_fe_11','f_non_E12','sn_fe_12','f5_non_E1','\
sn_f5e_1','f5_non_E2','sn_f5e_2','f5_non_E3','sn_f5e_3','f5_non_E4','sn_f5e_4','f5_non_E5','sn_f5e_5','f5_non_E6','sn_f5e_6','\
f5_non_E7','sn_f5e_7','f5_non_E8','sn_f5e_8','f5_non_E9','sn_f5e_9','f5_non_E10','sn_f5e_10','f5_non_E11','sn_f5e_11','f5_non_E12','\
sn_f5e_12','f_non_E13','sn_fe_13','f_non_E14','sn_fe_14','f_non_E15','sn_fe_15','f_non_E16','sn_fe_16','f_non_E17','sn_fe_17','f_non_E18','sn_fe_18'])
print(df_ea)

df_ea.dropna(axis=1, how="all", inplace=True)
print(df_ea)

		#######################
		# formatting E chains #
		#######################
df_ea.columns = df_ea.columns.str.replace('^LC\d+', 'LC_E', regex=True)
s = df_ea.stack()
df_ea = s.unstack()
df_ea.columns = df_ea.columns.str.replace('sn_L_\d+', 'sn_LC_E', regex=True)
s2 = df_ea.stack()
df_ea = s2.unstack()
df_ea.columns = df_ea.columns.str.replace('^HC\d+', 'HC_E', regex=True)
s3 = df_ea.stack()
df_ea = s3.unstack()
df_ea.columns = df_ea.columns.str.replace('sn_H_\d+', 'sn_HC_E', regex=True)
s4 = df_ea.stack()
df_ea = s4.unstack()
df_ea.columns = df_ea.columns.str.replace('^Intact\d+', 'Intact_E', regex=True)
s5 = df_ea.stack()
df_ea = s5.unstack()
df_ea.columns = df_ea.columns.str.replace('sn_I_\d+', 'sn_Intact_E', regex=True)
s6 = df_ea.stack()
df_ea = s6.unstack()

df_ea.drop([col for col in df_ea.columns if 'a_non_E' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'sn_ae_' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'b_non_E' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'sn_be_' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'f_non_E' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'sn_fe_' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'f5_non_E' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'sn_f5e_' in col], axis=1, inplace=True)

cols = df_ea.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_E')))
cols.insert(4, cols.pop(cols.index('sn_LC_E')))
cols.insert(5, cols.pop(cols.index('HC_E')))
cols.insert(6, cols.pop(cols.index('sn_HC_E')))
cols.insert(7, cols.pop(cols.index('Intact_E')))
cols.insert(8, cols.pop(cols.index('sn_Intact_E')))
df_ea = df_ea.reindex(columns=cols)

df_ea1 = df_ea.drop(df_ea.index[0])
print(df_ea1)
df_ea1.to_csv("e_final_df.txt", sep="\t")
