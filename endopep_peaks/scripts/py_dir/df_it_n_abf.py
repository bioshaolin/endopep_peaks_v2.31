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
b = open("b_out.txt", "r")
f = open("f_out.txt", "r")

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

#######
#  B  #
#######

	############
	# read_csv #
	############

df_b = pd.read_csv(b, sep="\t", header=None, names=['date','plate','bot_id','test','peak_1','peak_2','peak_3','peak_4','peak_5','peak_6'])
print(df_b)
df_b1 = df_b.round(decimals=12)

		##light_chain##
df_b1.insert(10, 'LC1', np.where(np.logical_and(df_b1['peak_1']>= 1756.500000000000,df_b1['peak_1']<=1763.700000000000) , df_b1['peak_1'], ""))
df_b1.insert(11, 'LC2', np.where(np.logical_and(df_b1['peak_2']>= 1756.500000000000,df_b1['peak_2']<=1763.700000000000) , df_b1['peak_2'], ""))
df_b1.insert(12, 'LC3', np.where(np.logical_and(df_b1['peak_3']>= 1756.500000000000,df_b1['peak_3']<=1763.700000000000) , df_b1['peak_3'], ""))
df_b1.insert(13, 'LC4', np.where(np.logical_and(df_b1['peak_4']>= 1756.500000000000,df_b1['peak_4']<=1763.700000000000) , df_b1['peak_4'], ""))
df_b1.insert(14, 'LC5', np.where(np.logical_and(df_b1['peak_5']>= 1756.500000000000,df_b1['peak_5']<=1763.700000000000) , df_b1['peak_5'], ""))
df_b1.insert(15, 'LC6', np.where(np.logical_and(df_b1['peak_6']>= 1756.500000000000,df_b1['peak_6']<=1763.700000000000) , df_b1['peak_6'], ""))
		##heavy_chain##
df_b1.insert(16, 'HC1', np.where(np.logical_and(df_b1['peak_1']>= 2277.700000000000,df_b1['peak_1']<=2286.900000000000) , df_b1['peak_1'], ""))
df_b1.insert(17, 'HC2', np.where(np.logical_and(df_b1['peak_2']>= 2277.700000000000,df_b1['peak_2']<=2286.900000000000) , df_b1['peak_2'], ""))
df_b1.insert(18, 'HC3', np.where(np.logical_and(df_b1['peak_3']>= 2277.700000000000,df_b1['peak_3']<=2286.900000000000) , df_b1['peak_3'], ""))
df_b1.insert(19, 'HC4', np.where(np.logical_and(df_b1['peak_4']>= 2277.700000000000,df_b1['peak_4']<=2286.900000000000) , df_b1['peak_4'], ""))
df_b1.insert(20, 'HC5', np.where(np.logical_and(df_b1['peak_5']>= 2277.700000000000,df_b1['peak_5']<=2286.900000000000) , df_b1['peak_5'], ""))
df_b1.insert(21, 'HC6', np.where(np.logical_and(df_b1['peak_6']>= 2277.700000000000,df_b1['peak_6']<=2286.900000000000) , df_b1['peak_6'], ""))
		##intact##
df_b1.insert(22, 'Intact1', np.where(np.logical_and(df_b1['peak_1']>= 4018.400000000000,df_b1['peak_1']<=4034.600000000000) , df_b1['peak_1'], ""))
df_b1.insert(23, 'Intact2', np.where(np.logical_and(df_b1['peak_2']>= 4018.400000000000,df_b1['peak_2']<=4034.600000000000) , df_b1['peak_2'], ""))
df_b1.insert(24, 'Intact3', np.where(np.logical_and(df_b1['peak_3']>= 4018.400000000000,df_b1['peak_3']<=4034.600000000000) , df_b1['peak_3'], ""))
df_b1.insert(25, 'Intact4', np.where(np.logical_and(df_b1['peak_4']>= 4018.400000000000,df_b1['peak_4']<=4034.600000000000) , df_b1['peak_4'], ""))
df_b1.insert(26, 'Intact5', np.where(np.logical_and(df_b1['peak_5']>= 4018.400000000000,df_b1['peak_5']<=4034.600000000000) , df_b1['peak_5'], ""))
df_b1.insert(27, 'Intact6', np.where(np.logical_and(df_b1['peak_6']>= 4018.400000000000,df_b1['peak_6']<=4034.600000000000) , df_b1['peak_6'], ""))
		###a_lc_noise###
df_b1.insert(28, 'a_non_b1', np.where(np.logical_and(df_b1['peak_1']>= 0996.800000000000,df_b1['peak_1']<=1000.800000000000) , df_b1['peak_1'], ""))
df_b1.insert(29, 'a_non_b2', np.where(np.logical_and(df_b1['peak_2']>= 0996.800000000000,df_b1['peak_2']<=1000.800000000000) , df_b1['peak_2'], ""))
df_b1.insert(30, 'a_non_b3', np.where(np.logical_and(df_b1['peak_3']>= 0996.800000000000,df_b1['peak_3']<=1000.800000000000) , df_b1['peak_3'], ""))
df_b1.insert(31, 'a_non_b4', np.where(np.logical_and(df_b1['peak_4']>= 0996.800000000000,df_b1['peak_4']<=1000.800000000000) , df_b1['peak_4'], ""))
df_b1.insert(32, 'a_non_b5', np.where(np.logical_and(df_b1['peak_5']>= 0996.800000000000,df_b1['peak_5']<=1000.800000000000) , df_b1['peak_5'], ""))
df_b1.insert(33, 'a_non_b6', np.where(np.logical_and(df_b1['peak_6']>= 0996.800000000000,df_b1['peak_6']<=1000.800000000000) , df_b1['peak_6'], ""))
		##a_hc_noise##
df_b1.insert(34, 'a_non_b7', np.where(np.logical_and(df_b1['peak_1']>= 2302.900000000000,df_b1['peak_1']<=2312.100000000000) , df_b1['peak_1'], ""))
df_b1.insert(35, 'a_non_b8', np.where(np.logical_and(df_b1['peak_2']>= 2302.900000000000,df_b1['peak_2']<=2312.100000000000) , df_b1['peak_2'], ""))
df_b1.insert(36, 'a_non_b9', np.where(np.logical_and(df_b1['peak_3']>= 2302.900000000000,df_b1['peak_3']<=2312.100000000000) , df_b1['peak_3'], ""))
df_b1.insert(37, 'a_non_b10', np.where(np.logical_and(df_b1['peak_4']>= 2302.900000000000,df_b1['peak_4']<=2312.100000000000) , df_b1['peak_4'], ""))
df_b1.insert(38, 'a_non_b11', np.where(np.logical_and(df_b1['peak_5']>= 2302.900000000000,df_b1['peak_5']<=2312.100000000000) , df_b1['peak_5'], ""))
df_b1.insert(39, 'a_non_b12', np.where(np.logical_and(df_b1['peak_6']>= 2302.900000000000,df_b1['peak_6']<=2312.100000000000) , df_b1['peak_6'], ""))
		##a_intact_noise##
df_b1.insert(40, 'a_non_b13', np.where(np.logical_and(df_b1['peak_1']>= 3280.700000000000,df_b1['peak_1']<=3293.700000000000) , df_b1['peak_1'], ""))
df_b1.insert(41, 'a_non_b14', np.where(np.logical_and(df_b1['peak_2']>= 3280.700000000000,df_b1['peak_2']<=3293.700000000000) , df_b1['peak_2'], ""))
df_b1.insert(42, 'a_non_b15', np.where(np.logical_and(df_b1['peak_3']>= 3280.700000000000,df_b1['peak_3']<=3293.700000000000) , df_b1['peak_3'], ""))
df_b1.insert(43, 'a_non_b16', np.where(np.logical_and(df_b1['peak_4']>= 3280.700000000000,df_b1['peak_4']<=3293.700000000000) , df_b1['peak_4'], ""))
df_b1.insert(44, 'a_non_b17', np.where(np.logical_and(df_b1['peak_5']>= 3280.700000000000,df_b1['peak_5']<=3293.700000000000) , df_b1['peak_5'], ""))
df_b1.insert(45, 'a_non_b18', np.where(np.logical_and(df_b1['peak_6']>= 3280.700000000000,df_b1['peak_6']<=3293.700000000000) , df_b1['peak_6'], ""))
		##e_lc_noise##
df_b1.insert(46, 'e_non_b1', np.where(np.logical_and(df_b1['peak_1']>= 1129.200000000000,df_b1['peak_1']<=1133.800000000000) , df_b1['peak_1'], ""))
df_b1.insert(47, 'e_non_b2', np.where(np.logical_and(df_b1['peak_2']>= 1129.200000000000,df_b1['peak_2']<=1133.800000000000) , df_b1['peak_2'], ""))
df_b1.insert(48, 'e_non_b3', np.where(np.logical_and(df_b1['peak_3']>= 1129.200000000000,df_b1['peak_3']<=1133.800000000000) , df_b1['peak_3'], ""))
df_b1.insert(49, 'e_non_b4', np.where(np.logical_and(df_b1['peak_4']>= 1129.200000000000,df_b1['peak_4']<=1133.800000000000) , df_b1['peak_4'], ""))
df_b1.insert(50, 'e_non_b5', np.where(np.logical_and(df_b1['peak_5']>= 1129.200000000000,df_b1['peak_5']<=1133.800000000000) , df_b1['peak_5'], ""))
df_b1.insert(51, 'e_non_b6', np.where(np.logical_and(df_b1['peak_6']>= 1129.200000000000,df_b1['peak_6']<=1133.800000000000) , df_b1['peak_6'], ""))
		##e_hc_noise##
df_b1.insert(52, 'e_non_b7', np.where(np.logical_and(df_b1['peak_1']>= 2493.600000000000,df_b1['peak_1']<=2503.600000000000) , df_b1['peak_1'], ""))
df_b1.insert(53, 'e_non_b8', np.where(np.logical_and(df_b1['peak_2']>= 2493.600000000000,df_b1['peak_2']<=2503.600000000000) , df_b1['peak_2'], ""))
df_b1.insert(54, 'e_non_b9', np.where(np.logical_and(df_b1['peak_3']>= 2493.600000000000,df_b1['peak_3']<=2503.600000000000) , df_b1['peak_3'], ""))
df_b1.insert(55, 'e_non_b10', np.where(np.logical_and(df_b1['peak_4']>= 2493.600000000000,df_b1['peak_4']<=2503.600000000000) , df_b1['peak_4'], ""))
df_b1.insert(56, 'e_non_b11', np.where(np.logical_and(df_b1['peak_5']>= 2493.600000000000,df_b1['peak_5']<=2503.600000000000) , df_b1['peak_5'], ""))
df_b1.insert(57, 'e_non_b12', np.where(np.logical_and(df_b1['peak_6']>= 2493.600000000000,df_b1['peak_6']<=2503.600000000000) , df_b1['peak_6'], ""))
		##e_intact_noise##
df_b1.insert(58, 'e_non_b13', np.where(np.logical_and(df_b1['peak_1']>= 3607.800000000000,df_b1['peak_1']<=3622.200000000000) , df_b1['peak_1'], ""))
df_b1.insert(59, 'e_non_b14', np.where(np.logical_and(df_b1['peak_2']>= 3607.800000000000,df_b1['peak_2']<=3622.200000000000) , df_b1['peak_2'], ""))
df_b1.insert(60, 'e_non_b15', np.where(np.logical_and(df_b1['peak_3']>= 3607.800000000000,df_b1['peak_3']<=3622.200000000000) , df_b1['peak_3'], ""))
df_b1.insert(61, 'e_non_b16', np.where(np.logical_and(df_b1['peak_4']>= 3607.800000000000,df_b1['peak_4']<=3622.200000000000) , df_b1['peak_4'], ""))
df_b1.insert(62, 'e_non_b17', np.where(np.logical_and(df_b1['peak_5']>= 3607.800000000000,df_b1['peak_5']<=3622.200000000000) , df_b1['peak_5'], ""))
df_b1.insert(63, 'e_non_b18', np.where(np.logical_and(df_b1['peak_6']>= 3607.800000000000,df_b1['peak_6']<=3622.200000000000) , df_b1['peak_6'], ""))
		##f_lc_noise##
df_b1.insert(64, 'f_non_b1', np.where(np.logical_and(df_b1['peak_1']>= 1342.500000000000,df_b1['peak_1']<=1347.900000000000) , df_b1['peak_1'], ""))
df_b1.insert(65, 'f_non_b2', np.where(np.logical_and(df_b1['peak_2']>= 1342.500000000000,df_b1['peak_2']<=1347.900000000000) , df_b1['peak_2'], ""))
df_b1.insert(66, 'f_non_b3', np.where(np.logical_and(df_b1['peak_3']>= 1342.500000000000,df_b1['peak_3']<=1347.900000000000) , df_b1['peak_3'], ""))
df_b1.insert(67, 'f_non_b4', np.where(np.logical_and(df_b1['peak_4']>= 1342.500000000000,df_b1['peak_4']<=1347.900000000000) , df_b1['peak_4'], ""))
df_b1.insert(68, 'f_non_b5', np.where(np.logical_and(df_b1['peak_5']>= 1342.500000000000,df_b1['peak_5']<=1347.900000000000) , df_b1['peak_5'], ""))
df_b1.insert(69, 'f_non_b6', np.where(np.logical_and(df_b1['peak_6']>= 1342.500000000000,df_b1['peak_6']<=1347.900000000000) , df_b1['peak_6'], ""))
		##f_hc_noise##
df_b1.insert(70, 'f_non_b7', np.where(np.logical_and(df_b1['peak_1']>= 3777.300000000000,df_b1['peak_1']<=3792.500000000000) , df_b1['peak_1'], ""))
df_b1.insert(71, 'f_non_b8', np.where(np.logical_and(df_b1['peak_2']>= 3777.300000000000,df_b1['peak_2']<=3792.500000000000) , df_b1['peak_2'], ""))
df_b1.insert(72, 'f_non_b9', np.where(np.logical_and(df_b1['peak_3']>= 3777.300000000000,df_b1['peak_3']<=3792.500000000000) , df_b1['peak_3'], ""))
df_b1.insert(73, 'f_non_b10', np.where(np.logical_and(df_b1['peak_4']>= 3777.300000000000,df_b1['peak_4']<=3792.500000000000) , df_b1['peak_4'], ""))
df_b1.insert(74, 'f_non_b11', np.where(np.logical_and(df_b1['peak_5']>= 3777.300000000000,df_b1['peak_5']<=3792.500000000000) , df_b1['peak_5'], ""))
df_b1.insert(75, 'f_non_b12', np.where(np.logical_and(df_b1['peak_6']>= 3777.300000000000,df_b1['peak_6']<=3792.500000000000) , df_b1['peak_6'], ""))
		##f5_lc_noise##
df_b1.insert(76, 'f5_non_b1', np.where(np.logical_and(df_b1['peak_1']>= 1870.300000000000,df_b1['peak_1']<=1877.700000000000) , df_b1['peak_1'], ""))
df_b1.insert(77, 'f5_non_b2', np.where(np.logical_and(df_b1['peak_2']>= 1870.300000000000,df_b1['peak_2']<=1877.700000000000) , df_b1['peak_2'], ""))
df_b1.insert(78, 'f5_non_b3', np.where(np.logical_and(df_b1['peak_3']>= 1870.300000000000,df_b1['peak_3']<=1877.700000000000) , df_b1['peak_3'], ""))
df_b1.insert(79, 'f5_non_b4', np.where(np.logical_and(df_b1['peak_4']>= 1870.300000000000,df_b1['peak_4']<=1877.700000000000) , df_b1['peak_4'], ""))
df_b1.insert(80, 'f5_non_b5', np.where(np.logical_and(df_b1['peak_5']>= 1870.300000000000,df_b1['peak_5']<=1877.700000000000) , df_b1['peak_5'], ""))
df_b1.insert(81, 'f5_non_b6', np.where(np.logical_and(df_b1['peak_6']>= 1870.300000000000,df_b1['peak_6']<=1877.700000000000) , df_b1['peak_6'], ""))
		##f5_hc_noise##
df_b1.insert(82, 'f5_non_b7', np.where(np.logical_and(df_b1['peak_1']>= 3248.500000000000,df_b1['peak_1']<=3261.500000000000) , df_b1['peak_1'], ""))
df_b1.insert(83, 'f5_non_b8', np.where(np.logical_and(df_b1['peak_2']>= 3248.500000000000,df_b1['peak_2']<=3261.500000000000) , df_b1['peak_2'], ""))
df_b1.insert(84, 'f5_non_b9', np.where(np.logical_and(df_b1['peak_3']>= 3248.500000000000,df_b1['peak_3']<=3261.500000000000) , df_b1['peak_3'], ""))
df_b1.insert(85, 'f5_non_b10', np.where(np.logical_and(df_b1['peak_4']>= 3248.500000000000,df_b1['peak_4']<=3261.500000000000) , df_b1['peak_4'], ""))
df_b1.insert(86, 'f5_non_b11', np.where(np.logical_and(df_b1['peak_5']>= 3248.500000000000,df_b1['peak_5']<=3261.500000000000) , df_b1['peak_5'], ""))
df_b1.insert(87, 'f5_non_b12', np.where(np.logical_and(df_b1['peak_6']>= 3248.500000000000,df_b1['peak_6']<=3261.500000000000) , df_b1['peak_6'], ""))
		##f_f5_intact_noise##
df_b1.insert(88, 'f_non_b13', np.where(np.logical_and(df_b1['peak_1']>= 5100.800000000000,df_b1['peak_1']<=5121.200000000000) , df_b1['peak_1'], ""))
df_b1.insert(89, 'f_non_b14', np.where(np.logical_and(df_b1['peak_2']>= 5100.800000000000,df_b1['peak_2']<=5121.200000000000) , df_b1['peak_2'], ""))
df_b1.insert(90, 'f_non_b15', np.where(np.logical_and(df_b1['peak_3']>= 5100.800000000000,df_b1['peak_3']<=5121.200000000000) , df_b1['peak_3'], ""))
df_b1.insert(91, 'f_non_b16', np.where(np.logical_and(df_b1['peak_4']>= 5100.800000000000,df_b1['peak_4']<=5121.200000000000) , df_b1['peak_4'], ""))
df_b1.insert(92, 'f_non_b17', np.where(np.logical_and(df_b1['peak_5']>= 5100.800000000000,df_b1['peak_5']<=5121.200000000000) , df_b1['peak_5'], ""))
df_b1.insert(93, 'f_non_b18', np.where(np.logical_and(df_b1['peak_6']>= 5100.800000000000,df_b1['peak_6']<=5121.200000000000) , df_b1['peak_6'], ""))

df_b2 = df_b1.drop(['test','peak_1','peak_2','peak_3','peak_4','peak_5','peak_6'], axis=1)
df_b2.set_index('date', inplace=True)
print(df_b2)
df_b2.to_csv("b_df.txt", sep="\t")

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

a_df = open("a_df.txt", "r")
b_df = open("b_df.txt", "r")
f_df = open("f_df.txt", "r")

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

#######
#  B  #
#######

		############
		# read_csv #
		############
df_ba = pd.read_csv(b_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','LC1','LC2','LC3','LC4','LC5','LC6','HC1','HC2','HC3','HC4','HC5','HC6','Intact1','Intact2','Intact3','Intact4','Intact5','Intact6','a_non_b1','a_non_b2','a_non_b3','a_non_b4','a_non_b5','a_non_b6','a_non_b7','a_non_b8','a_non_b9','a_non_b10','a_non_b11','a_non_b12','a_non_b13','a_non_b14','a_non_b15','a_non_b16','a_non_b17','a_non_b18','e_non_b1','e_non_b2','e_non_b3','e_non_b4','e_non_b5','e_non_b6','e_non_b7','e_non_b8','e_non_b9','e_non_b10','e_non_b11','e_non_b12','e_non_b13','e_non_b14','e_non_b15','e_non_b16','e_non_b17','e_non_b18','f_non_b1','f_non_b2','f_non_b3','f_non_b4','f_non_b5','f_non_b6','f_non_b7','f_non_b8','f_non_b9','f_non_b10','f_non_b11','f_non_b12','f5_non_b1','f5_non_b2','f5_non_b3','f5_non_b4','f5_non_b5','f5_non_b6','f5_non_b7','f5_non_b8','f5_non_b9','f5_non_b10','f5_non_b11','f5_non_b12','f_non_b13','f_non_b14','f_non_b15','f_non_b16','f_non_b17','f_non_b18'])
print(df_ba)

df_ba.dropna(axis=1, how="all", inplace=True)
print(df_ba)

		#######################
		# formatting B chains #
		#######################
df_ba.columns = df_ba.columns.str.replace('^LC\d+', 'LC_B', regex=True)
s = df_ba.stack()
df_ba = s.unstack()
df_ba.columns = df_ba.columns.str.replace('^HC\d+', 'HC_B', regex=True)
s2 = df_ba.stack()
df_ba = s2.unstack()
df_ba.columns = df_ba.columns.str.replace('^Intact\d+', 'Intact_B', regex=True)
s3 = df_ba.stack()
df_ba = s3.unstack()
df_ba.columns = df_ba.columns.str.replace('a_non_b\d+', 'A_non_B', regex=True)
s4 = df_ba.stack()
df_ba = s4.unstack()
df_ba.columns = df_ba.columns.str.replace('e_non_b\d+', 'E_non_B', regex=True)
s5 = df_ba.stack()
df_ba = s5.unstack()
df_ba.columns = df_ba.columns.str.replace('f_non_b\d+|f5_non_b\d+', 'F_non_B', regex=True)
s6 = df_ba.stack()
df_ba = s6.unstack()

cols = df_ba.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_B')))
cols.insert(4, cols.pop(cols.index('HC_B')))
cols.insert(5, cols.pop(cols.index('Intact_B')))
df_ba = df_ba.reindex(columns=cols)

df_ba1 = df_ba.drop(df_ba.index[0])
print(df_ba1)
df_ba1.to_csv("b_final_df.txt", sep="\t")

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

##############################
# COMPILE CHAIN DATA BY TYPE #
##############################

a_df_fin = open("a_final_df.txt", "r")
b_df_fin = open("b_final_df.txt", "r")
f_df_fin = open("f_final_df.txt", "r")

df_ab = pd.read_csv(a_df_fin,sep="\t")
df_ab.to_csv("test.csv", sep="\t")
print(df_ab.columns)
df_bb = pd.read_csv(b_df_fin, sep="\t")
print(df_bb.columns)
df_fb = pd.read_csv(f_df_fin, sep="\t")
print(df_fb.columns)


##### Below is two line changes to merge 3 dfs as oppossed to option all for 4 #####

df_fin1 = pd.merge(pd.merge(df_ab,df_bb,on=['date','plate','bot_id']),df_fb,on=['date','plate','bot_id'])
df_final = df_fin1.groupby(['date','plate','bot_id']).head(2)

#####################################################################################

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


df_final_1 = df_final.reset_index(drop=True).style.applymap(highlight_1, subset=pd.IndexSlice[:, ['Peak_1_A','Peak_2_A','Intact_A']]) \
.applymap(highlight_2, subset=pd.IndexSlice[:, ['Peak_1_B', 'Peak_2_B','Intact_B']]) \
.applymap(highlight_4, subset=pd.IndexSlice[:, ['Peak_1_F','Peak_2_F','Peak_1_F5','Peak_2_F5','Intact_F']])
print(df_final_1)
df_final_1.to_excel("noise_reference.xlsx", index=False)

df_final_2 = df_final[['date','plate','bot_id','LC_A','HC_A','Intact_A','LC_B','HC_B','Intact_B',\
'LC_F','HC_F','LC_F5','HC_F5','Intact_F']]
df_final_2.columns = ['date','plate','bot_id','Peak_1_A','Peak_2_A','Intact_A','Peak_1_B','Peak_2_B',\
'Intact_B','Peak_1_F','Peak_2_F','Peak_1_F5','Peak_2_F5','Intact_F']
df_final_2 = df_final_2.sort_values(['date', 'plate', 'bot_id'])
df_final_2 = df_final_2.reset_index(drop=True).style.applymap(highlight_1, subset=pd.IndexSlice[:, ['Peak_1_A','Peak_2_A','Intact_A']]) \
.applymap(highlight_2, subset=pd.IndexSlice[:, ['Peak_1_B', 'Peak_2_B','Intact_B']]) \
.applymap(highlight_4, subset=pd.IndexSlice[:, ['Peak_1_F','Peak_2_F','Peak_1_F5','Peak_2_F5','Intact_F']])
print(df_final_2)
df_final_2.to_excel("endopep_peak_list_n.xlsx", index=False)
