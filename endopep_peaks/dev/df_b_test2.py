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

b_df = open("b_df.txt", "r")

#######
#  B  #
#######

		############
		# read_csv #
		############
df_ba = pd.read_csv(b_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','LC1','sn_L_1','LC2','sn_L_2','LC3','sn_L_3','LC4','sn_L_4','\
LC5','sn_L_5','LC6','sn_L_6','HC1','sn_H_1','HC2','sn_H_2','HC3','sn_H_3','HC4','sn_H_4','HC5','sn_H_5','HC6','sn_H_6','Intact1','sn_I_1','Intact2','sn_I_2','Intact3','sn_I_3','\
Intact4','sn_I_4','Intact5','sn_I_5','Intact6','sn_I_6','a_non_B1','sn_ab_1','a_non_B2','sn_ab_2','a_non_B3','sn_ab_3','a_non_B4','sn_ab_4','a_non_B5','\
sn_ab_5','a_non_B6','sn_ab_6','a_non_B7','sn_ab_7','a_non_B8','sn_ab_8','a_non_B9','sn_ab_9','a_non_B10','sn_ab_10','a_non_B11','sn_ab_11','\
a_non_B12','sn_ab_12','a_non_B13','sn_ab_13','a_non_B14','sn_ab_14','a_non_B15','sn_ab_15','a_non_B16','sn_ab_16','a_non_B17','sn_ab_17','\
a_non_B18','sn_ab_18','e_non_B1','sn_eb_1','e_non_B2','sn_eb_2','e_non_B3','sn_eb_3','e_non_B4','sn_eb_4','e_non_B5','sn_eb_5','e_non_B6','\
sn_eb_6','e_non_B7','sn_eb_7','e_non_B8','sn_eb_8','e_non_B9','sn_eb_9','e_non_B10','sn_eb_10','e_non_B11','sn_eb_11','e_non_B12','sn_eb_12','\
e_non_B13','sn_eb_13','e_non_B14','sn_eb_14','e_non_B15','sn_eb_15','e_non_B16','sn_eb_16','e_non_B17','sn_eb_17','e_non_B18','sn_eb_18','\
f_non_B1','sn_fb_1','f_non_B2','sn_fb_2','f_non_B3','sn_fb_3','f_non_B4','sn_fb_4','f_non_B5','sn_fb_5','f_non_B6','sn_fb_6','f_non_B7','sn_fb_7','\
f_non_B8','sn_fb_8','f_non_B9','sn_fb_9','f_non_B10','sn_fb_10','f_non_B11','sn_fb_11','f_non_B12','sn_fb_12','f5_non_B1','sn_f5b_1','\
f5_non_B2','sn_f5b_2','f5_non_B3','sn_f5b_3','f5_non_B4','sn_f5b_4','f5_non_B5','sn_f5b_5','f5_non_B6','sn_f5b_6','f5_non_B7','sn_f5b_7','\
f5_non_B8','sn_f5b_8','f5_non_B9','sn_f5b_9','f5_non_B10','sn_f5b_10','f5_non_B11','sn_f5b_11','f5_non_B12','sn_f5b_12','f_non_B13','sn_fb_13','\
f_non_B14','sn_fb_14','f_non_B15','sn_fb_15','f_non_B16','sn_fb_16','f_non_B17','sn_fb_17','f_non_B18','sn_fb_18'])
print(df_ba)

df_ba.dropna(axis=1, how="all", inplace=True)
print(df_ba)

		#######################
		# formatting B chains #
		#######################
df_ba.columns = df_ba.columns.str.replace('^LC\d+', 'LC_B', regex=True)
s = df_ba.stack()
df_ba = s.unstack()
df_ba.columns = df_ba.columns.str.replace('sn_L_\d+', 'sn_LC_B', regex=True)
s2 = df_ba.stack()
df_ba = s2.unstack()
df_ba.columns = df_ba.columns.str.replace('^HC\d+', 'HC_B', regex=True)
s3 = df_ba.stack()
df_ba = s3.unstack()
df_ba.columns = df_ba.columns.str.replace('sn_H_\d+', 'sn_HC_B', regex=True)
s4 = df_ba.stack()
df_ba = s4.unstack()
df_ba.columns = df_ba.columns.str.replace('^Intact\d+', 'Intact_B', regex=True)
s5 = df_ba.stack()
df_ba = s5.unstack()
df_ba.columns = df_ba.columns.str.replace('sn_I_\d+', 'sn_Intact_B', regex=True)
s6 = df_ba.stack()
df_ba = s6.unstack()

df_ba.drop([col for col in df_ba.columns if 'a_non_B' in col], axis=1, inplace=True)
df_ba.drop([col for col in df_ba.columns if 'sn_ab_' in col], axis=1, inplace=True)
df_ba.drop([col for col in df_ba.columns if 'e_non_B' in col], axis=1, inplace=True)
df_ba.drop([col for col in df_ba.columns if 'sn_eb_' in col], axis=1, inplace=True)
df_ba.drop([col for col in df_ba.columns if 'f_non_B' in col], axis=1, inplace=True)
df_ba.drop([col for col in df_ba.columns if 'sn_fb_' in col], axis=1, inplace=True)
df_ba.drop([col for col in df_ba.columns if 'f5_non_B' in col], axis=1, inplace=True)
df_ba.drop([col for col in df_ba.columns if 'sn_f5b_' in col], axis=1, inplace=True)

cols = df_ba.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_B')))
cols.insert(4, cols.pop(cols.index('sn_LC_B')))
cols.insert(5, cols.pop(cols.index('HC_B')))
cols.insert(6, cols.pop(cols.index('sn_HC_B')))
cols.insert(7, cols.pop(cols.index('Intact_B')))
cols.insert(8, cols.pop(cols.index('sn_Intact_B')))
df_ba = df_ba.reindex(columns=cols)

df_ba1 = df_ba.drop(df_ba.index[0])
print(df_ba1)
df_ba1.to_csv("b_final_df.txt", sep="\t")
