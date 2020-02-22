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

a = open("a_out.txt", "r")


#######
#  A  #
#######

	############
	# read_csv #
	############

df_a = pd.read_csv(a, sep="\t", header=None, names=['date','plate','bot_id','test','peak_1','peak_2','peak_3','peak_4','peak_5','peak_6'])
print(df_a)
df_a1 = df_a.round(decimals=12)

		###light chain###
df_a1.insert(10, 'LC1', np.where(np.logical_and(df_a1['peak_1']>= 0996.800000000000,df_a1['peak_1']<=1000.800000000000) , df_a1['peak_1'], ""))
df_a1.insert(11, 'LC2', np.where(np.logical_and(df_a1['peak_2']>= 0996.800000000000,df_a1['peak_2']<=1000.800000000000) , df_a1['peak_2'], ""))
df_a1.insert(12, 'LC3', np.where(np.logical_and(df_a1['peak_3']>= 0996.800000000000,df_a1['peak_3']<=1000.800000000000) , df_a1['peak_3'], ""))
df_a1.insert(13, 'LC4', np.where(np.logical_and(df_a1['peak_4']>= 0996.800000000000,df_a1['peak_4']<=1000.800000000000) , df_a1['peak_4'], ""))
df_a1.insert(14, 'LC5', np.where(np.logical_and(df_a1['peak_5']>= 0996.800000000000,df_a1['peak_5']<=1000.800000000000) , df_a1['peak_5'], ""))
df_a1.insert(15, 'LC6', np.where(np.logical_and(df_a1['peak_6']>= 0996.800000000000,df_a1['peak_6']<=1000.800000000000) , df_a1['peak_6'], ""))
		##heavy chain##
df_a1.insert(16, 'HC1', np.where(np.logical_and(df_a1['peak_1']>= 2302.900000000000,df_a1['peak_1']<=2312.100000000000) , df_a1['peak_1'], ""))
df_a1.insert(17, 'HC2', np.where(np.logical_and(df_a1['peak_2']>= 2302.900000000000,df_a1['peak_2']<=2312.100000000000) , df_a1['peak_2'], ""))
df_a1.insert(18, 'HC3', np.where(np.logical_and(df_a1['peak_3']>= 2302.900000000000,df_a1['peak_3']<=2312.100000000000) , df_a1['peak_3'], ""))
df_a1.insert(19, 'HC4', np.where(np.logical_and(df_a1['peak_4']>= 2302.900000000000,df_a1['peak_4']<=2312.100000000000) , df_a1['peak_4'], ""))
df_a1.insert(20, 'HC5', np.where(np.logical_and(df_a1['peak_5']>= 2302.900000000000,df_a1['peak_5']<=2312.100000000000) , df_a1['peak_5'], ""))
df_a1.insert(21, 'HC6', np.where(np.logical_and(df_a1['peak_6']>= 2302.900000000000,df_a1['peak_6']<=2312.100000000000) , df_a1['peak_6'], ""))
		##intact##
df_a1.insert(22, 'Intact1', np.where(np.logical_and(df_a1['peak_1']>= 3280.700000000000,df_a1['peak_1']<=3293.700000000000) , df_a1['peak_1'], ""))
df_a1.insert(23, 'Intact2', np.where(np.logical_and(df_a1['peak_2']>= 3280.700000000000,df_a1['peak_2']<=3293.700000000000) , df_a1['peak_2'], ""))
df_a1.insert(24, 'Intact3', np.where(np.logical_and(df_a1['peak_3']>= 3280.700000000000,df_a1['peak_3']<=3293.700000000000) , df_a1['peak_3'], ""))
df_a1.insert(25, 'Intact4', np.where(np.logical_and(df_a1['peak_4']>= 3280.700000000000,df_a1['peak_4']<=3293.700000000000) , df_a1['peak_4'], ""))
df_a1.insert(26, 'Intact5', np.where(np.logical_and(df_a1['peak_5']>= 3280.700000000000,df_a1['peak_5']<=3293.700000000000) , df_a1['peak_5'], ""))
df_a1.insert(27, 'Intact6', np.where(np.logical_and(df_a1['peak_6']>= 3280.700000000000,df_a1['peak_6']<=3293.700000000000) , df_a1['peak_6'], ""))
		##b_lc_noise##
df_a1.insert(28, 'b_non_A1', np.where(np.logical_and(df_a1['peak_1']>= 1756.500000000000,df_a1['peak_1']<=1763.700000000000) , df_a1['peak_1'], ""))
df_a1.insert(29, 'b_non_A2', np.where(np.logical_and(df_a1['peak_2']>= 1756.500000000000,df_a1['peak_2']<=1763.700000000000) , df_a1['peak_2'], ""))
df_a1.insert(30, 'b_non_A3', np.where(np.logical_and(df_a1['peak_3']>= 1756.500000000000,df_a1['peak_3']<=1763.700000000000) , df_a1['peak_3'], ""))
df_a1.insert(31, 'b_non_A4', np.where(np.logical_and(df_a1['peak_4']>= 1756.500000000000,df_a1['peak_4']<=1763.700000000000) , df_a1['peak_4'], ""))
df_a1.insert(32, 'b_non_A5', np.where(np.logical_and(df_a1['peak_5']>= 1756.500000000000,df_a1['peak_5']<=1763.700000000000) , df_a1['peak_5'], ""))
df_a1.insert(33, 'b_non_A6', np.where(np.logical_and(df_a1['peak_6']>= 1756.500000000000,df_a1['peak_6']<=1763.700000000000) , df_a1['peak_6'], ""))
		##b_hc_noise##
df_a1.insert(34, 'b_non_A7', np.where(np.logical_and(df_a1['peak_1']>= 2277.700000000000,df_a1['peak_1']<=2286.900000000000) , df_a1['peak_1'], ""))
df_a1.insert(35, 'b_non_A8', np.where(np.logical_and(df_a1['peak_2']>= 2277.700000000000,df_a1['peak_2']<=2286.900000000000) , df_a1['peak_2'], ""))
df_a1.insert(36, 'b_non_A9', np.where(np.logical_and(df_a1['peak_3']>= 2277.700000000000,df_a1['peak_3']<=2286.900000000000) , df_a1['peak_3'], ""))
df_a1.insert(37, 'b_non_A10', np.where(np.logical_and(df_a1['peak_4']>= 2277.700000000000,df_a1['peak_4']<=2286.900000000000) , df_a1['peak_4'], ""))
df_a1.insert(38, 'b_non_A11', np.where(np.logical_and(df_a1['peak_5']>= 2277.700000000000,df_a1['peak_5']<=2286.900000000000) , df_a1['peak_5'], ""))
df_a1.insert(39, 'b_non_A12', np.where(np.logical_and(df_a1['peak_6']>= 2277.700000000000,df_a1['peak_6']<=2286.900000000000) , df_a1['peak_6'], ""))
		##b_intact_noise##
df_a1.insert(40, 'b_non_A13', np.where(np.logical_and(df_a1['peak_1']>= 4018.400000000000,df_a1['peak_1']<=4034.600000000000) , df_a1['peak_1'], ""))
df_a1.insert(41, 'b_non_A14', np.where(np.logical_and(df_a1['peak_2']>= 4018.400000000000,df_a1['peak_2']<=4034.600000000000) , df_a1['peak_2'], ""))
df_a1.insert(42, 'b_non_A15', np.where(np.logical_and(df_a1['peak_3']>= 4018.400000000000,df_a1['peak_3']<=4034.600000000000) , df_a1['peak_3'], ""))
df_a1.insert(43, 'b_non_A16', np.where(np.logical_and(df_a1['peak_4']>= 4018.400000000000,df_a1['peak_4']<=4034.600000000000) , df_a1['peak_4'], ""))
df_a1.insert(44, 'b_non_A17', np.where(np.logical_and(df_a1['peak_5']>= 4018.400000000000,df_a1['peak_5']<=4034.600000000000) , df_a1['peak_5'], ""))
df_a1.insert(45, 'b_non_A18', np.where(np.logical_and(df_a1['peak_6']>= 4018.400000000000,df_a1['peak_6']<=4034.600000000000) , df_a1['peak_6'], ""))
		##e_lc_noise##
df_a1.insert(46, 'e_non_A1', np.where(np.logical_and(df_a1['peak_1']>= 1129.200000000000,df_a1['peak_1']<=1133.800000000000) , df_a1['peak_1'], ""))
df_a1.insert(47, 'e_non_A2', np.where(np.logical_and(df_a1['peak_2']>= 1129.200000000000,df_a1['peak_2']<=1133.800000000000) , df_a1['peak_2'], ""))
df_a1.insert(48, 'e_non_A3', np.where(np.logical_and(df_a1['peak_3']>= 1129.200000000000,df_a1['peak_3']<=1133.800000000000) , df_a1['peak_3'], ""))
df_a1.insert(49, 'e_non_A4', np.where(np.logical_and(df_a1['peak_4']>= 1129.200000000000,df_a1['peak_4']<=1133.800000000000) , df_a1['peak_4'], ""))
df_a1.insert(50, 'e_non_A5', np.where(np.logical_and(df_a1['peak_5']>= 1129.200000000000,df_a1['peak_5']<=1133.800000000000) , df_a1['peak_5'], ""))
df_a1.insert(51, 'e_non_A6', np.where(np.logical_and(df_a1['peak_6']>= 1129.200000000000,df_a1['peak_6']<=1133.800000000000) , df_a1['peak_6'], ""))
		##e_hc_noise##
df_a1.insert(52, 'e_non_A7', np.where(np.logical_and(df_a1['peak_1']>= 2493.600000000000,df_a1['peak_1']<=2503.600000000000) , df_a1['peak_1'], ""))
df_a1.insert(53, 'e_non_A8', np.where(np.logical_and(df_a1['peak_2']>= 2493.600000000000,df_a1['peak_2']<=2503.600000000000) , df_a1['peak_2'], ""))
df_a1.insert(54, 'e_non_A9', np.where(np.logical_and(df_a1['peak_3']>= 2493.600000000000,df_a1['peak_3']<=2503.600000000000) , df_a1['peak_3'], ""))
df_a1.insert(55, 'e_non_A10', np.where(np.logical_and(df_a1['peak_4']>= 2493.600000000000,df_a1['peak_4']<=2503.600000000000) , df_a1['peak_4'], ""))
df_a1.insert(56, 'e_non_A11', np.where(np.logical_and(df_a1['peak_5']>= 2493.600000000000,df_a1['peak_5']<=2503.600000000000) , df_a1['peak_5'], ""))
df_a1.insert(57, 'e_non_A12', np.where(np.logical_and(df_a1['peak_6']>= 2493.600000000000,df_a1['peak_6']<=2503.600000000000) , df_a1['peak_6'], ""))
		##e_intact_noise##
df_a1.insert(58, 'e_non_A13', np.where(np.logical_and(df_a1['peak_1']>= 3607.800000000000,df_a1['peak_1']<=3622.200000000000) , df_a1['peak_1'], ""))
df_a1.insert(59, 'e_non_A14', np.where(np.logical_and(df_a1['peak_2']>= 3607.800000000000,df_a1['peak_2']<=3622.200000000000) , df_a1['peak_2'], ""))
df_a1.insert(60, 'e_non_A15', np.where(np.logical_and(df_a1['peak_3']>= 3607.800000000000,df_a1['peak_3']<=3622.200000000000) , df_a1['peak_3'], ""))
df_a1.insert(61, 'e_non_A16', np.where(np.logical_and(df_a1['peak_4']>= 3607.800000000000,df_a1['peak_4']<=3622.200000000000) , df_a1['peak_4'], ""))
df_a1.insert(62, 'e_non_A17', np.where(np.logical_and(df_a1['peak_5']>= 3607.800000000000,df_a1['peak_5']<=3622.200000000000) , df_a1['peak_5'], ""))
df_a1.insert(63, 'e_non_A18', np.where(np.logical_and(df_a1['peak_6']>= 3607.800000000000,df_a1['peak_6']<=3622.200000000000) , df_a1['peak_6'], ""))
		##f_lc_noise##
df_a1.insert(64, 'f_non_A1', np.where(np.logical_and(df_a1['peak_1']>= 1342.500000000000,df_a1['peak_1']<=1347.900000000000) , df_a1['peak_1'], ""))
df_a1.insert(65, 'f_non_A2', np.where(np.logical_and(df_a1['peak_2']>= 1342.500000000000,df_a1['peak_2']<=1347.900000000000) , df_a1['peak_2'], ""))
df_a1.insert(66, 'f_non_A3', np.where(np.logical_and(df_a1['peak_3']>= 1342.500000000000,df_a1['peak_3']<=1347.900000000000) , df_a1['peak_3'], ""))
df_a1.insert(67, 'f_non_A4', np.where(np.logical_and(df_a1['peak_4']>= 1342.500000000000,df_a1['peak_4']<=1347.900000000000) , df_a1['peak_4'], ""))
df_a1.insert(68, 'f_non_A5', np.where(np.logical_and(df_a1['peak_5']>= 1342.500000000000,df_a1['peak_5']<=1347.900000000000) , df_a1['peak_5'], ""))
df_a1.insert(69, 'f_non_A6', np.where(np.logical_and(df_a1['peak_6']>= 1342.500000000000,df_a1['peak_6']<=1347.900000000000) , df_a1['peak_6'], ""))
		##f_hc_noise##
df_a1.insert(70, 'f_non_A7', np.where(np.logical_and(df_a1['peak_1']>= 3777.300000000000,df_a1['peak_1']<=3792.500000000000) , df_a1['peak_1'], ""))
df_a1.insert(71, 'f_non_A8', np.where(np.logical_and(df_a1['peak_2']>= 3777.300000000000,df_a1['peak_2']<=3792.500000000000) , df_a1['peak_2'], ""))
df_a1.insert(72, 'f_non_A9', np.where(np.logical_and(df_a1['peak_3']>= 3777.300000000000,df_a1['peak_3']<=3792.500000000000) , df_a1['peak_3'], ""))
df_a1.insert(73, 'f_non_A10', np.where(np.logical_and(df_a1['peak_4']>= 3777.300000000000,df_a1['peak_4']<=3792.500000000000) , df_a1['peak_4'], ""))
df_a1.insert(74, 'f_non_A11', np.where(np.logical_and(df_a1['peak_5']>= 3777.300000000000,df_a1['peak_5']<=3792.500000000000) , df_a1['peak_5'], ""))
df_a1.insert(75, 'f_non_A12', np.where(np.logical_and(df_a1['peak_6']>= 3777.300000000000,df_a1['peak_6']<=3792.500000000000) , df_a1['peak_6'], ""))
		##f5_lc_noise##
df_a1.insert(76, 'f5_non_A1', np.where(np.logical_and(df_a1['peak_1']>= 1870.300000000000,df_a1['peak_1']<=1877.700000000000) , df_a1['peak_1'], ""))
df_a1.insert(77, 'f5_non_A2', np.where(np.logical_and(df_a1['peak_2']>= 1870.300000000000,df_a1['peak_2']<=1877.700000000000) , df_a1['peak_2'], ""))
df_a1.insert(78, 'f5_non_A3', np.where(np.logical_and(df_a1['peak_3']>= 1870.300000000000,df_a1['peak_3']<=1877.700000000000) , df_a1['peak_3'], ""))
df_a1.insert(79, 'f5_non_A4', np.where(np.logical_and(df_a1['peak_4']>= 1870.300000000000,df_a1['peak_4']<=1877.700000000000) , df_a1['peak_4'], ""))
df_a1.insert(80, 'f5_non_A5', np.where(np.logical_and(df_a1['peak_5']>= 1870.300000000000,df_a1['peak_5']<=1877.700000000000) , df_a1['peak_5'], ""))
df_a1.insert(81, 'f5_non_A6', np.where(np.logical_and(df_a1['peak_6']>= 1870.300000000000,df_a1['peak_6']<=1877.700000000000) , df_a1['peak_6'], ""))
		##f5_hc_noise##
df_a1.insert(82, 'f5_non_A7', np.where(np.logical_and(df_a1['peak_1']>= 3248.500000000000,df_a1['peak_1']<=3261.500000000000) , df_a1['peak_1'], ""))
df_a1.insert(83, 'f5_non_A8', np.where(np.logical_and(df_a1['peak_2']>= 3248.500000000000,df_a1['peak_2']<=3261.500000000000) , df_a1['peak_2'], ""))
df_a1.insert(84, 'f5_non_A9', np.where(np.logical_and(df_a1['peak_3']>= 3248.500000000000,df_a1['peak_3']<=3261.500000000000) , df_a1['peak_3'], ""))
df_a1.insert(85, 'f5_non_A10', np.where(np.logical_and(df_a1['peak_4']>= 3248.500000000000,df_a1['peak_4']<=3261.500000000000) , df_a1['peak_4'], ""))
df_a1.insert(86, 'f5_non_A11', np.where(np.logical_and(df_a1['peak_5']>= 3248.500000000000,df_a1['peak_5']<=3261.500000000000) , df_a1['peak_5'], ""))
df_a1.insert(87, 'f5_non_A12', np.where(np.logical_and(df_a1['peak_6']>= 3248.500000000000,df_a1['peak_6']<=3261.500000000000) , df_a1['peak_6'], ""))
		##f_f5_intact_noise##
df_a1.insert(88, 'f_non_A13', np.where(np.logical_and(df_a1['peak_1']>= 5100.800000000000,df_a1['peak_1']<=5121.200000000000) , df_a1['peak_1'], ""))
df_a1.insert(89, 'f_non_A14', np.where(np.logical_and(df_a1['peak_2']>= 5100.800000000000,df_a1['peak_2']<=5121.200000000000) , df_a1['peak_2'], ""))
df_a1.insert(90, 'f_non_A15', np.where(np.logical_and(df_a1['peak_3']>= 5100.800000000000,df_a1['peak_3']<=5121.200000000000) , df_a1['peak_3'], ""))
df_a1.insert(91, 'f_non_A16', np.where(np.logical_and(df_a1['peak_4']>= 5100.800000000000,df_a1['peak_4']<=5121.200000000000) , df_a1['peak_4'], ""))
df_a1.insert(92, 'f_non_A17', np.where(np.logical_and(df_a1['peak_5']>= 5100.800000000000,df_a1['peak_5']<=5121.200000000000) , df_a1['peak_5'], ""))
df_a1.insert(93, 'f_non_A18', np.where(np.logical_and(df_a1['peak_6']>= 5100.800000000000,df_a1['peak_6']<=5121.200000000000) , df_a1['peak_6'], ""))

df_a2 = df_a1.drop(['test','peak_1','peak_2','peak_3','peak_4','peak_5','peak_6'], axis=1)
df_a2.set_index('date', inplace=True)
print(df_a2)
df_a2.to_csv("a_df.txt", sep="\t")

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
df_aa = pd.read_csv(a_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','LC1','LC2','LC3','LC4','LC5','LC6','HC1','HC2','HC3','HC4','HC5','HC6','Intact1','Intact2','Intact3','Intact4','Intact5','Intact6','b_non_A1','b_non_A2','b_non_A3','b_non_A4','b_non_A5','b_non_A6','b_non_A7','b_non_A8','b_non_A9','b_non_A10','b_non_A11','b_non_A12','b_non_A13','b_non_A14','b_non_A15','b_non_A16','b_non_A17','b_non_A18','e_non_A1','e_non_A2','e_non_A3','e_non_A4','e_non_A5','e_non_A6','e_non_A7','e_non_A8','e_non_A9','e_non_A10','e_non_A11','e_non_A12','e_non_A13','e_non_A14','e_non_A15','e_non_A16','e_non_A17','e_non_A18','f_non_A1','f_non_A2','f_non_A3','f_non_A4','f_non_A5','f_non_A6','f_non_A7','f_non_A8','f_non_A9','f_non_A10','f_non_A11','f_non_A12','f5_non_A1','f5_non_A2','f5_non_A3','f5_non_A4','f5_non_A5','f5_non_A6','f5_non_A7','f5_non_A8','f5_non_A9','f5_non_A10','f5_non_A11','f5_non_A12','f_non_A13','f_non_A14','f_non_A15','f_non_A16','f_non_A17','f_non_A18'])
print(df_aa)

df_aa.dropna(axis=1, how="all", inplace=True)
print(df_aa)

		#######################
		# formatting A chains #
		#######################
df_aa.columns = df_aa.columns.str.replace('^LC\d+', 'LC_A', regex=True).str.replace('^HC\d+', 'HC_A', regex=True).str.replace('^Intact\d+', 'Intact_A', regex=True).str.replace('b_non_a\d+', 'B_non_A', regex=True)
s = df_aa.stack()
df_aa = s.unstack()
df_aa.columns = df_aa.columns.str.replace('^HC\d+', 'HC_A', regex=True)
s2 = df_aa.stack()
df_aa = s2.unstack()
df_aa.columns = df_aa.columns.str.replace('^Intact\d+', 'Intact_A', regex=True)
s3 = df_aa.stack()
df_aa = s3.unstack()
df_aa.columns = df_aa.columns.str.replace('b_non_A\d+', 'B_non_A', regex=True)
#df_aa.columns = df_aa.columns.str.replace('b_non_a1|b_non_a2|b_non_a3|b_non_a4|b_non_a5|b_non_a6|b_non_a7|b_non_a8|b_non_a9|b_non_a10|b_non_a11|b_non_a12|b_non_a13| \
#b_non_a14|b_non_a15|b_non_a16|b_non_a17|b_non_a18', 'B_non_A', regex=True)
s4 = df_aa.stack()
df_aa = s4.unstack()
#df_aa.columns = df_aa.columns.str.replace('e_non_A\d+', 'E_non_A', regex=True)
#s5 = df_aa.stack()
#df_aa = s5.unstack()
df_aa.columns = df_aa.columns.str.replace('f_non_A\d+|f5_non_A\d+', 'F_non_A', regex=True)
s6 = df_aa.stack()
df_aa = s6.unstack()

cols = df_aa.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_A')))
cols.insert(4, cols.pop(cols.index('HC_A')))
cols.insert(5, cols.pop(cols.index('Intact_A')))
df_aa = df_aa.reindex(columns=cols)

df_aa1 = df_aa.drop(df_aa.index[0])
print(df_aa1)
df_aa1.to_csv("a_final_df.txt", sep="\t")


df_final = df_aa1[::2]
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


df_final_1 = df_final.reset_index(drop=True).style.applymap(highlight_1, subset=pd.IndexSlice[:, ['Peak_1_A','Peak_2_A','Intact_A']])
print(df_final_1)
df_final_1.to_excel("noise_reference.xlsx", index=False)

df_final_2 = df_final[['date','plate','bot_id','LC_A','HC_A','Intact_A']]
df_final_2.columns = ['date','plate','bot_id','Peak_1_A','Peak_2_A','Intact_A']
df_final_2 = df_final_2.sort_values(['date', 'plate', 'bot_id'])
df_final_2 = df_final_2.reset_index(drop=True).style.applymap(highlight_1, subset=pd.IndexSlice[:, ['Peak_1_A','Peak_2_A','Intact_A']])
print(df_final_2)
df_final_2.to_excel("endopep_peak_list_n.xlsx", index=False)
