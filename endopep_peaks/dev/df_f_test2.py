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

f_df = open("f_df.txt", "r")

#######
#  F  #
#######

		############
		# read_csv #
		############
df_fa = pd.read_csv(f_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','f_LC1','sn_L_1','f_LC2','sn_L_2','f_LC3','sn_L_3','f_LC4','\
sn_L_4','f_LC5','sn_L_5','f_LC6','sn_L_6','f_HC1','sn_H_1','f_HC2','sn_H_2','f_HC3','sn_H_3','f_HC4','sn_H_4','f_HC5','sn_H_5','f_HC6','sn_H_6','f5_LC1','sn_f5_L_1','\
f5_LC2','sn_f5_L_2','f5_LC3','sn_f5_L_3','f5_LC4','sn_f5_L_4','f5_LC5','sn_f5_L_5','f5_LC6','sn_f5_L_6','f5_HC1','sn_f5_H_1','f5_HC2','sn_f5_H_2','f5_HC3','\
sn_f5_H_3','f5_HC4','sn_f5_H_4','f5_HC5','sn_f5_H_5','f5_HC6','sn_f5_H_6','Intact1','sn_I_1','Intact2','sn_I_2','Intact3','sn_I_3','Intact4','sn_I_4','Intact5','\
sn_I_5','Intact6','sn_I_6','a_non_F1','sn_af_1','a_non_F2','sn_af_2','a_non_F3','sn_af_3','a_non_F4','sn_af_4','a_non_F5','sn_af_5','a_non_F6','sn_af_6','\
a_non_F7','sn_af_7','a_non_F8','sn_af_8','a_non_F9','sn_af_9','a_non_F10','sn_af_10','a_non_F11','sn_af_11','a_non_F12','sn_af_12','a_non_F13','\
sn_af_13','a_non_F14','sn_af_14','a_non_F15','sn_af_15','a_non_F16','sn_af_16','a_non_F17','sn_af_17','a_non_F18','sn_af_18','b_non_F1','\
sn_bf_1','b_non_F2','sn_bf_2','b_non_F3','sn_bf_3','b_non_F4','sn_bf_4','b_non_F5','sn_bf_5','b_non_F6','sn_bf_6','b_non_F7','sn_bf_7','b_non_F8','\
sn_bf_8','b_non_F9','sn_bf_9','b_non_F10','sn_bf_10','b_non_F11','sn_bf_11','b_non_F12','sn_bf_12','b_non_F13','sn_bf_13','b_non_F14','\
sn_bf_14','b_non_F15','sn_bf_15','b_non_F16','sn_bf_16','b_non_F17','sn_bf_17','b_non_F18','sn_bf_18','e_non_F1','sn_ef_1','e_non_F2','\
sn_ef_2','e_non_F3','sn_ef_3','e_non_F4','sn_ef_4','e_non_F5','sn_ef_5','e_non_F6','sn_ef_6','e_non_F7','sn_ef_7','e_non_F8','sn_ef_8','e_non_F9','\
sn_ef_9','e_non_F10','sn_ef_10','e_non_F11','sn_ef_11','e_non_F12','sn_ef_12','e_non_F13','sn_ef_13','e_non_F14','sn_ef_14','e_non_F15','\
sn_ef_15','e_non_F16','sn_ef_16','e_non_F17','sn_ef_17','e_non_F18','sn_ef_18'])
print(df_fa)

df_fa.dropna(axis=1, how="all", inplace=True)
print(df_fa)

		#######################
		# formatting F chains #
		#######################
df_fa.columns = df_fa.columns.str.replace('f_LC\d+', 'LC_F', regex=True)
s = df_fa.stack()
df_fa = s.unstack()
df_fa.columns = df_fa.columns.str.replace('sn_L_\d+', 'sn_LC_F', regex=True)
s2 = df_fa.stack()
df_fa = s2.unstack()
df_fa.columns = df_fa.columns.str.replace('f_HC\d+', 'HC_F', regex=True)
s3 = df_fa.stack()
df_fa = s3.unstack()
df_fa.columns = df_fa.columns.str.replace('sn_H_\d+', 'sn_HC_F', regex=True)
s4 = df_fa.stack()
df_fa = s4.unstack()
df_fa.columns = df_fa.columns.str.replace('^Intact\d+', 'Intact_F', regex=True)
s5 = df_fa.stack()
df_fa = s5.unstack()
df_fa.columns = df_fa.columns.str.replace('sn_I_\d+', 'sn_Intact_F', regex=True)
s6 = df_fa.stack()
df_fa = s6.unstack()
#df_fa.columns = df_fa.columns.str.replace('^f5_LC\d+', 'LC_F5', regex=True)
#s7 = df_fa.stack()
#df_fa = s7.unstack()
#df_fa.to_csv("test.csv", sep="\t")
df_fa.columns = df_fa.columns.str.replace('sn_f5_L_\d+', 'sn_LC_F5', regex=True)
s8 = df_fa.stack()
df_fa = s8.unstack()
df_fa.columns = df_fa.columns.str.replace('^f5_HC\d+', 'HC_F5', regex=True)
s9 = df_fa.stack()
df_fa = s9.unstack()
df_fa.columns = df_fa.columns.str.replace('sn_f5_H_\d+', 'sn_HC_F5', regex=True)
s10 = df_fa.stack()
df_fa = s10.unstack()

df_fa.drop([col for col in df_fa.columns if 'a_non_F' in col], axis=1, inplace=True)
df_fa.drop([col for col in df_fa.columns if 'sn_af_' in col], axis=1, inplace=True)
df_fa.drop([col for col in df_fa.columns if 'b_non_F' in col], axis=1, inplace=True)
df_fa.drop([col for col in df_fa.columns if 'sn_bf_' in col], axis=1, inplace=True)
df_fa.drop([col for col in df_fa.columns if 'e_non_F' in col], axis=1, inplace=True)
df_fa.drop([col for col in df_fa.columns if 'sn_ef_' in col], axis=1, inplace=True)
#df_fa.drop([col for col in df_fa.columns if 'e_non_F5' in col], axis=1, inplace=True)
#df_fa.drop([col for col in df_fa.columns if 'sn_ef5_' in col], axis=1, inplace=True)

cols = df_fa.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_F')))
cols.insert(4, cols.pop(cols.index('sn_LC_F')))
cols.insert(5, cols.pop(cols.index('HC_F')))
cols.insert(6, cols.pop(cols.index('sn_HC_F')))
#cols.insert(7, cols.pop(cols.index('LC_F5')))
#cols.insert(8, cols.pop(cols.index('sn_LC_F5')))
#cols.insert(9, cols.pop(cols.index('HC_F5')))
#cols.insert(10, cols.pop(cols.index('sn_HC_F5')))
cols.insert(11, cols.pop(cols.index('Intact_F')))
cols.insert(12, cols.pop(cols.index('sn_Intact_F')))
df_fa = df_fa.reindex(columns=cols)

df_fa1 = df_fa.drop(df_fa.index[0])
print(df_fa1)
df_fa1.to_csv("f_final_df.txt", sep="\t")
