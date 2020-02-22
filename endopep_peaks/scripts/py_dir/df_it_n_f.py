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

##########################
# RESTRUCTURE CHAIN DATA #
##########################

f = open("f_out.txt", "r")

#######
#  F  #
#######

	############
	# read_csv #
	############

df_f = pd.read_csv(f, sep="\t", header=None, names=['date','plate','bot_id','test','peak_1','peak_2','peak_3','peak_4','peak_5','peak_6'])
print(df_f)
df_f1 = df_f.round(decimals=12)

		##light_chain##
df_f1.insert(10, 'f_LC1', np.where(np.logical_and(df_f1['peak_1']>= 1342.500000000000,df_f1['peak_1']<=1347.900000000000) , df_f1['peak_1'], ""))
df_f1.insert(11, 'f_LC2', np.where(np.logical_and(df_f1['peak_2']>= 1342.500000000000,df_f1['peak_2']<=1347.900000000000) , df_f1['peak_2'], ""))
df_f1.insert(12, 'f_LC3', np.where(np.logical_and(df_f1['peak_3']>= 1342.500000000000,df_f1['peak_3']<=1347.900000000000) , df_f1['peak_3'], ""))
df_f1.insert(13, 'f_LC4', np.where(np.logical_and(df_f1['peak_4']>= 1342.500000000000,df_f1['peak_4']<=1347.900000000000) , df_f1['peak_4'], ""))
df_f1.insert(14, 'f_LC5', np.where(np.logical_and(df_f1['peak_5']>= 1342.500000000000,df_f1['peak_5']<=1347.900000000000) , df_f1['peak_5'], ""))
df_f1.insert(15, 'f_LC6', np.where(np.logical_and(df_f1['peak_6']>= 1342.500000000000,df_f1['peak_6']<=1347.900000000000) , df_f1['peak_6'], ""))
		##heavy_chain##
df_f1.insert(16, 'f_HC1', np.where(np.logical_and(df_f1['peak_1']>= 3777.300000000000,df_f1['peak_1']<=3792.500000000000) , df_f1['peak_1'], ""))
df_f1.insert(17, 'f_HC2', np.where(np.logical_and(df_f1['peak_2']>= 3777.300000000000,df_f1['peak_2']<=3792.500000000000) , df_f1['peak_2'], ""))
df_f1.insert(18, 'f_HC3', np.where(np.logical_and(df_f1['peak_3']>= 3777.300000000000,df_f1['peak_3']<=3792.500000000000) , df_f1['peak_3'], ""))
df_f1.insert(19, 'f_HC4', np.where(np.logical_and(df_f1['peak_4']>= 3777.300000000000,df_f1['peak_4']<=3792.500000000000) , df_f1['peak_4'], ""))
df_f1.insert(20, 'f_HC5', np.where(np.logical_and(df_f1['peak_5']>= 3777.300000000000,df_f1['peak_5']<=3792.500000000000) , df_f1['peak_5'], ""))
df_f1.insert(21, 'f_HC6', np.where(np.logical_and(df_f1['peak_6']>= 3777.300000000000,df_f1['peak_6']<=3792.500000000000) , df_f1['peak_6'], ""))
		##f5_light_chain##
df_f1.insert(22, 'f5_LC1', np.where(np.logical_and(df_f1['peak_1']>= 1870.300000000000,df_f1['peak_1']<=1877.700000000000) , df_f1['peak_1'], ""))
df_f1.insert(23, 'f5_LC2', np.where(np.logical_and(df_f1['peak_2']>= 1870.300000000000,df_f1['peak_2']<=1877.700000000000) , df_f1['peak_2'], ""))
df_f1.insert(24, 'f5_LC3', np.where(np.logical_and(df_f1['peak_3']>= 1870.300000000000,df_f1['peak_3']<=1877.700000000000) , df_f1['peak_3'], ""))
df_f1.insert(25, 'f5_LC4', np.where(np.logical_and(df_f1['peak_4']>= 1870.300000000000,df_f1['peak_4']<=1877.700000000000) , df_f1['peak_4'], ""))
df_f1.insert(26, 'f5_LC5', np.where(np.logical_and(df_f1['peak_5']>= 1870.300000000000,df_f1['peak_5']<=1877.700000000000) , df_f1['peak_5'], ""))
df_f1.insert(27, 'f5_LC6', np.where(np.logical_and(df_f1['peak_6']>= 1870.300000000000,df_f1['peak_6']<=1877.700000000000) , df_f1['peak_6'], ""))
		##f5_heavy_chain##
df_f1.insert(28, 'f5_HC1', np.where(np.logical_and(df_f1['peak_1']>= 3248.500000000000,df_f1['peak_1']<=3261.500000000000) , df_f1['peak_1'], ""))
df_f1.insert(29, 'f5_HC2', np.where(np.logical_and(df_f1['peak_2']>= 3248.500000000000,df_f1['peak_2']<=3261.500000000000) , df_f1['peak_2'], ""))
df_f1.insert(30, 'f5_HC3', np.where(np.logical_and(df_f1['peak_3']>= 3248.500000000000,df_f1['peak_3']<=3261.500000000000) , df_f1['peak_3'], ""))
df_f1.insert(31, 'f5_HC4', np.where(np.logical_and(df_f1['peak_4']>= 3248.500000000000,df_f1['peak_4']<=3261.500000000000) , df_f1['peak_4'], ""))
df_f1.insert(32, 'f5_HC5', np.where(np.logical_and(df_f1['peak_5']>= 3248.500000000000,df_f1['peak_5']<=3261.500000000000) , df_f1['peak_5'], ""))
df_f1.insert(33, 'f5_HC6', np.where(np.logical_and(df_f1['peak_6']>= 3248.500000000000,df_f1['peak_6']<=3261.500000000000) , df_f1['peak_6'], ""))
		##intact##
df_f1.insert(34, 'Intact1', np.where(np.logical_and(df_f1['peak_1']>= 5100.800000000000,df_f1['peak_1']<=5121.200000000000) , df_f1['peak_1'], ""))
df_f1.insert(35, 'Intact2', np.where(np.logical_and(df_f1['peak_2']>= 5100.800000000000,df_f1['peak_2']<=5121.200000000000) , df_f1['peak_2'], ""))
df_f1.insert(36, 'Intact3', np.where(np.logical_and(df_f1['peak_3']>= 5100.800000000000,df_f1['peak_3']<=5121.200000000000) , df_f1['peak_3'], ""))
df_f1.insert(37, 'Intact4', np.where(np.logical_and(df_f1['peak_4']>= 5100.800000000000,df_f1['peak_4']<=5121.200000000000) , df_f1['peak_4'], ""))
df_f1.insert(38, 'Intact5', np.where(np.logical_and(df_f1['peak_5']>= 5100.800000000000,df_f1['peak_5']<=5121.200000000000) , df_f1['peak_5'], ""))
df_f1.insert(39, 'Intact6', np.where(np.logical_and(df_f1['peak_6']>= 5100.800000000000,df_f1['peak_6']<=5121.200000000000) , df_f1['peak_6'], ""))
		###a_lc_noise###
df_f1.insert(40, 'a_non_f1', np.where(np.logical_and(df_f1['peak_1']>= 0996.800000000000,df_f1['peak_1']<=1000.800000000000) , df_f1['peak_1'], ""))
df_f1.insert(41, 'a_non_f2', np.where(np.logical_and(df_f1['peak_2']>= 0996.800000000000,df_f1['peak_2']<=1000.800000000000) , df_f1['peak_2'], ""))
df_f1.insert(42, 'a_non_f3', np.where(np.logical_and(df_f1['peak_3']>= 0996.800000000000,df_f1['peak_3']<=1000.800000000000) , df_f1['peak_3'], ""))
df_f1.insert(43, 'a_non_f4', np.where(np.logical_and(df_f1['peak_4']>= 0996.800000000000,df_f1['peak_4']<=1000.800000000000) , df_f1['peak_4'], ""))
df_f1.insert(44, 'a_non_f5', np.where(np.logical_and(df_f1['peak_5']>= 0996.800000000000,df_f1['peak_5']<=1000.800000000000) , df_f1['peak_5'], ""))
df_f1.insert(45, 'a_non_f6', np.where(np.logical_and(df_f1['peak_6']>= 0996.800000000000,df_f1['peak_6']<=1000.800000000000) , df_f1['peak_6'], ""))
		##a_hc_noise##
df_f1.insert(46, 'a_non_f7', np.where(np.logical_and(df_f1['peak_1']>= 2302.900000000000,df_f1['peak_1']<=2312.100000000000) , df_f1['peak_1'], ""))
df_f1.insert(47, 'a_non_f8', np.where(np.logical_and(df_f1['peak_2']>= 2302.900000000000,df_f1['peak_2']<=2312.100000000000) , df_f1['peak_2'], ""))
df_f1.insert(48, 'a_non_f9', np.where(np.logical_and(df_f1['peak_3']>= 2302.900000000000,df_f1['peak_3']<=2312.100000000000) , df_f1['peak_3'], ""))
df_f1.insert(49, 'a_non_f10', np.where(np.logical_and(df_f1['peak_4']>= 2302.900000000000,df_f1['peak_4']<=2312.100000000000) , df_f1['peak_4'], ""))
df_f1.insert(50, 'a_non_f11', np.where(np.logical_and(df_f1['peak_5']>= 2302.900000000000,df_f1['peak_5']<=2312.100000000000) , df_f1['peak_5'], ""))
df_f1.insert(51, 'a_non_f12', np.where(np.logical_and(df_f1['peak_6']>= 2302.900000000000,df_f1['peak_6']<=2312.100000000000) , df_f1['peak_6'], ""))
		##a_intact_noise##
df_f1.insert(52, 'a_non_f13', np.where(np.logical_and(df_f1['peak_1']>= 3280.700000000000,df_f1['peak_1']<=3293.700000000000) , df_f1['peak_1'], ""))
df_f1.insert(53, 'a_non_f14', np.where(np.logical_and(df_f1['peak_2']>= 3280.700000000000,df_f1['peak_2']<=3293.700000000000) , df_f1['peak_2'], ""))
df_f1.insert(54, 'a_non_f15', np.where(np.logical_and(df_f1['peak_3']>= 3280.700000000000,df_f1['peak_3']<=3293.700000000000) , df_f1['peak_3'], ""))
df_f1.insert(55, 'a_non_f16', np.where(np.logical_and(df_f1['peak_4']>= 3280.700000000000,df_f1['peak_4']<=3293.700000000000) , df_f1['peak_4'], ""))
df_f1.insert(56, 'a_non_f17', np.where(np.logical_and(df_f1['peak_5']>= 3280.700000000000,df_f1['peak_5']<=3293.700000000000) , df_f1['peak_5'], ""))
df_f1.insert(57, 'a_non_f18', np.where(np.logical_and(df_f1['peak_6']>= 3280.700000000000,df_f1['peak_6']<=3293.700000000000) , df_f1['peak_6'], ""))
		##b_lc_noise##
df_f1.insert(58, 'b_non_f1', np.where(np.logical_and(df_f1['peak_1']>= 1756.500000000000,df_f1['peak_1']<=1763.700000000000) , df_f1['peak_1'], ""))
df_f1.insert(59, 'b_non_f2', np.where(np.logical_and(df_f1['peak_2']>= 1756.500000000000,df_f1['peak_2']<=1763.700000000000) , df_f1['peak_2'], ""))
df_f1.insert(60, 'b_non_f3', np.where(np.logical_and(df_f1['peak_3']>= 1756.500000000000,df_f1['peak_3']<=1763.700000000000) , df_f1['peak_3'], ""))
df_f1.insert(61, 'b_non_f4', np.where(np.logical_and(df_f1['peak_4']>= 1756.500000000000,df_f1['peak_4']<=1763.700000000000) , df_f1['peak_4'], ""))
df_f1.insert(62, 'b_non_f5', np.where(np.logical_and(df_f1['peak_5']>= 1756.500000000000,df_f1['peak_5']<=1763.700000000000) , df_f1['peak_5'], ""))
df_f1.insert(63, 'b_non_f6', np.where(np.logical_and(df_f1['peak_6']>= 1756.500000000000,df_f1['peak_6']<=1763.700000000000) , df_f1['peak_6'], ""))
		##b_hc_noise##
df_f1.insert(64, 'b_non_f7', np.where(np.logical_and(df_f1['peak_1']>= 2277.700000000000,df_f1['peak_1']<=2286.900000000000) , df_f1['peak_1'], ""))
df_f1.insert(65, 'b_non_f8', np.where(np.logical_and(df_f1['peak_2']>= 2277.700000000000,df_f1['peak_2']<=2286.900000000000) , df_f1['peak_2'], ""))
df_f1.insert(66, 'b_non_f9', np.where(np.logical_and(df_f1['peak_3']>= 2277.700000000000,df_f1['peak_3']<=2286.900000000000) , df_f1['peak_3'], ""))
df_f1.insert(67, 'b_non_f10', np.where(np.logical_and(df_f1['peak_4']>= 2277.700000000000,df_f1['peak_4']<=2286.900000000000) , df_f1['peak_4'], ""))
df_f1.insert(68, 'b_non_f11', np.where(np.logical_and(df_f1['peak_5']>= 2277.700000000000,df_f1['peak_5']<=2286.900000000000) , df_f1['peak_5'], ""))
df_f1.insert(69, 'b_non_f12', np.where(np.logical_and(df_f1['peak_6']>= 2277.700000000000,df_f1['peak_6']<=2286.900000000000) , df_f1['peak_6'], ""))
		##b_intact_noise##
df_f1.insert(70, 'b_non_f13', np.where(np.logical_and(df_f1['peak_1']>= 4018.400000000000,df_f1['peak_1']<=4034.600000000000) , df_f1['peak_1'], ""))
df_f1.insert(71, 'b_non_f14', np.where(np.logical_and(df_f1['peak_2']>= 4018.400000000000,df_f1['peak_2']<=4034.600000000000) , df_f1['peak_2'], ""))
df_f1.insert(72, 'b_non_f15', np.where(np.logical_and(df_f1['peak_3']>= 4018.400000000000,df_f1['peak_3']<=4034.600000000000) , df_f1['peak_3'], ""))
df_f1.insert(73, 'b_non_f16', np.where(np.logical_and(df_f1['peak_4']>= 4018.400000000000,df_f1['peak_4']<=4034.600000000000) , df_f1['peak_4'], ""))
df_f1.insert(74, 'b_non_f17', np.where(np.logical_and(df_f1['peak_5']>= 4018.400000000000,df_f1['peak_5']<=4034.600000000000) , df_f1['peak_5'], ""))
df_f1.insert(75, 'b_non_f18', np.where(np.logical_and(df_f1['peak_6']>= 4018.400000000000,df_f1['peak_6']<=4034.600000000000) , df_f1['peak_6'], ""))
		##e_lc_noice##
df_f1.insert(76, 'e_non_f1', np.where(np.logical_and(df_f1['peak_1']>= 1129.200000000000,df_f1['peak_1']<=1133.800000000000) , df_f1['peak_1'], ""))
df_f1.insert(77, 'e_non_f2', np.where(np.logical_and(df_f1['peak_2']>= 1129.200000000000,df_f1['peak_2']<=1133.800000000000) , df_f1['peak_2'], ""))
df_f1.insert(78, 'e_non_f3', np.where(np.logical_and(df_f1['peak_3']>= 1129.200000000000,df_f1['peak_3']<=1133.800000000000) , df_f1['peak_3'], ""))
df_f1.insert(79, 'e_non_f4', np.where(np.logical_and(df_f1['peak_4']>= 1129.200000000000,df_f1['peak_4']<=1133.800000000000) , df_f1['peak_4'], ""))
df_f1.insert(80, 'e_non_f5', np.where(np.logical_and(df_f1['peak_5']>= 1129.200000000000,df_f1['peak_5']<=1133.800000000000) , df_f1['peak_5'], ""))
df_f1.insert(81, 'e_non_f6', np.where(np.logical_and(df_f1['peak_6']>= 1129.200000000000,df_f1['peak_6']<=1133.800000000000) , df_f1['peak_6'], ""))
		##e_hc_noise##
df_f1.insert(82, 'e_non_f7', np.where(np.logical_and(df_f1['peak_1']>= 2493.600000000000,df_f1['peak_1']<=2503.600000000000) , df_f1['peak_1'], ""))
df_f1.insert(83, 'e_non_f8', np.where(np.logical_and(df_f1['peak_2']>= 2493.600000000000,df_f1['peak_2']<=2503.600000000000) , df_f1['peak_2'], ""))
df_f1.insert(84, 'e_non_f9', np.where(np.logical_and(df_f1['peak_3']>= 2493.600000000000,df_f1['peak_3']<=2503.600000000000) , df_f1['peak_3'], ""))
df_f1.insert(85, 'e_non_f10', np.where(np.logical_and(df_f1['peak_4']>= 2493.600000000000,df_f1['peak_4']<=2503.600000000000) , df_f1['peak_4'], ""))
df_f1.insert(86, 'e_non_f11', np.where(np.logical_and(df_f1['peak_5']>= 2493.600000000000,df_f1['peak_5']<=2503.600000000000) , df_f1['peak_5'], ""))
df_f1.insert(87, 'e_non_f12', np.where(np.logical_and(df_f1['peak_6']>= 2493.600000000000,df_f1['peak_6']<=2503.600000000000) , df_f1['peak_6'], ""))
		##e_intact_noise##
df_f1.insert(88, 'e_non_f13', np.where(np.logical_and(df_f1['peak_1']>= 3607.800000000000,df_f1['peak_1']<=3622.200000000000) , df_f1['peak_1'], ""))
df_f1.insert(89, 'e_non_f14', np.where(np.logical_and(df_f1['peak_2']>= 3607.800000000000,df_f1['peak_2']<=3622.200000000000) , df_f1['peak_2'], ""))
df_f1.insert(90, 'e_non_f15', np.where(np.logical_and(df_f1['peak_3']>= 3607.800000000000,df_f1['peak_3']<=3622.200000000000) , df_f1['peak_3'], ""))
df_f1.insert(91, 'e_non_f16', np.where(np.logical_and(df_f1['peak_4']>= 3607.800000000000,df_f1['peak_4']<=3622.200000000000) , df_f1['peak_4'], ""))
df_f1.insert(92, 'e_non_f17', np.where(np.logical_and(df_f1['peak_5']>= 3607.800000000000,df_f1['peak_5']<=3622.200000000000) , df_f1['peak_5'], ""))
df_f1.insert(93, 'e_non_f18', np.where(np.logical_and(df_f1['peak_6']>= 3607.800000000000,df_f1['peak_6']<=3622.200000000000) , df_f1['peak_6'], ""))

df_f2 = df_f1.drop(['test','peak_1','peak_2','peak_3','peak_4','peak_5','peak_6'], axis=1)
df_f2.set_index('date', inplace=True)
print(df_f2)
df_f2.to_csv("f_df.txt", sep="\t")

#####################
# FORMAT CHAIN DATA #
#####################

f_df = open("f_df.txt", "r")

#######
#  F  #
#######

		############
		# read_csv #
		############
df_fa = pd.read_csv(f_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','f_LC1','f_LC2','f_LC3','f_LC4','f_LC5','f_LC6','f_HC1','f_HC2','f_HC3','f_HC4','f_HC5','f_HC6','f5_LC1','f5_LC2','f5_LC3','f5_LC4','f5_LC5','f5_LC6','f5_HC1','f5_HC2','f5_HC3','f5_HC4','f5_HC5','f5_HC6','Intact1','Intact2','Intact3','Intact4','Intact5','Intact6','a_non_f1','a_non_f2','a_non_f3','a_non_f4','a_non_f5','a_non_f6','a_non_f7','a_non_f8','a_non_f9','a_non_f10','a_non_f11','a_non_f12','a_non_f13','a_non_f14','a_non_f15','a_non_f16','a_non_f17','a_non_f18','b_non_f1','b_non_f2','b_non_f3','b_non_f4','b_non_f5','b_non_f6','b_non_f7','b_non_f8','b_non_f9','b_non_f10','b_non_f11','b_non_f12','b_non_f13','b_non_f14','b_non_f15','b_non_f16','b_non_f17','b_non_f18','e_non_f1','e_non_f2','e_non_f3','e_non_f4','e_non_f5','e_non_f6','e_non_f7','e_non_f8','e_non_f9','e_non_f10','e_non_f11','e_non_f12','e_non_f13','e_non_f14','e_non_f15','e_non_f16','e_non_f17','e_non_f18'])
print(df_fa)

df_fa.dropna(axis=1, how="all", inplace=True)
print(df_fa)

		#######################
		# formatting F chains #
		#######################
df_fa.columns = df_fa.columns.str.replace('f_LC\d+', 'LC_F', regex=True)
s = df_fa.stack()
df_fa = s.unstack()
df_fa.columns = df_fa.columns.str.replace('f_HC\d+', 'HC_F', regex=True)
s2 = df_fa.stack()
df_fa = s2.unstack()
df_fa.columns = df_fa.columns.str.replace('^Intact\d+', 'Intact_F', regex=True)
s3 = df_fa.stack()
df_fa = s3.unstack()
df_fa.columns = df_fa.columns.str.replace('f5_LC\d+', 'LC_F5', regex=True)
s4 = df_fa.stack()
df_fa = s4.unstack()
df_fa.columns = df_fa.columns.str.replace('f5_HC\d+', 'HC_F5', regex=True)
s5 = df_fa.stack()
df_fa = s5.unstack()
df_fa.columns = df_fa.columns.str.replace('a_non_f\d+', 'A_non_F', regex=True)
s6 = df_fa.stack()
df_fa = s6.unstack()
df_fa.columns = df_fa.columns.str.replace('b_non_f\d+', 'B_non_F', regex=True)
s7 = df_fa.stack()
df_fa = s7.unstack()
df_fa.columns = df_fa.columns.str.replace('e_non_f\d+', 'E_non_F', regex=True)
s8 = df_fa.stack()
df_fa = s8.unstack()

cols = df_fa.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_F')))
cols.insert(4, cols.pop(cols.index('HC_F')))
cols.insert(5, cols.pop(cols.index('LC_F5')))
cols.insert(6, cols.pop(cols.index('HC_F5')))
cols.insert(7, cols.pop(cols.index('Intact_F')))
df_fa = df_fa.reindex(columns=cols)

df_fa1 = df_fa.drop(df_fa.index[0])
print(df_fa1)
df_fa1.to_csv("f_final_df.txt", sep="\t")


df_final = df_fa1[::2]
df_final.to_csv("test3.csv", sep="\t")
print(df_final)
df_final = df_final.loc[:, ~df_final.columns.str.contains('^Unnamed')]
df_final = df_final.loc[:, ~df_final.columns.duplicated()]
#df_final.to_csv("test.csv", sep="\t")

def highlight_1(s):
	color = '#FF6666'
	return 'background-color: %s' % color
def highlight_2(s):
	color = '#009933'
	return 'background-color: %s' % color
def highlight_3(s):
	color = '#FFFF66'
	return 'background-color: %s' % color
def highlight_4(s):
	color = '#6699FF'
	return 'background-color: %s' % color
def highlight_5(s):
	color = "#CC6600"
	return 'color: %s' % color


df_final_1 = df_final.reset_index(drop=True).style.applymap(highlight_4, subset=pd.IndexSlice[:, ['Peak_1_F','Peak_2_F','Peak_1_F5','Peak_2_F5','Intact_F']])
print(df_final_1)
df_final_1.to_excel("noise_reference.xlsx", index=False)

df_final_2 = df_final[['date','plate','bot_id','LC_F','HC_F','LC_F5','HC_F5','Intact_F']]
df_final_2.columns = ['date','plate','bot_id','Peak_1_F','Peak_2_F','Peak_1_F5','Peak_2_F5','Intact_F']
df_final_2 = df_final_2.sort_values(['date', 'plate', 'bot_id'])
df_final_2 = df_final_2.reset_index(drop=True).style.applymap(highlight_4, subset=pd.IndexSlice[:, ['Peak_1_F','Peak_2_F','Peak_1_F5','Peak_2_F5','Intact_F']])
print(df_final_2)
df_final_2.to_excel("endopep_peak_list_n.xlsx", index=False)
