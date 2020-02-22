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

df_f = pd.read_csv(f, sep="\t", header=None, names=['date','plate','bot_id','test','peak_1','sn_1','peak_2','sn_2','peak_3','sn_3',\
'peak_4','sn_4','peak_5','sn_5','peak_6','sn_6'])
print(df_f)
df_f1 = df_f.round(decimals=12)

		##light_chain##
df_f1.insert(16, 'f_LC1', np.where(np.logical_and(df_f1['peak_1']>=1342.500000000000,df_f1['peak_1']<=1347.900000000000) , df_f1['peak_1'], ""))
df_f1.insert(17, 'sn_L_1', np.where(np.logical_and(df_f1['peak_1']>=1342.500000000000,df_f1['peak_1']<=1347.900000000000) , df_f1['sn_1'], ""))
df_f1.insert(18, 'f_LC2', np.where(np.logical_and(df_f1['peak_2']>=1342.500000000000,df_f1['peak_2']<=1347.900000000000) , df_f1['peak_2'], ""))
df_f1.insert(19, 'sn_L_2', np.where(np.logical_and(df_f1['peak_2']>=1342.500000000000,df_f1['peak_2']<=1347.900000000000) , df_f1['sn_2'], ""))
df_f1.insert(20, 'f_LC3', np.where(np.logical_and(df_f1['peak_3']>=1342.500000000000,df_f1['peak_3']<=1347.900000000000) , df_f1['peak_3'], ""))
df_f1.insert(21, 'sn_L_3', np.where(np.logical_and(df_f1['peak_3']>=1342.500000000000,df_f1['peak_3']<=1347.900000000000) , df_f1['sn_3'], ""))
df_f1.insert(22, 'f_LC4', np.where(np.logical_and(df_f1['peak_4']>=1342.500000000000,df_f1['peak_4']<=1347.900000000000) , df_f1['peak_4'], ""))
df_f1.insert(23, 'sn_L_4', np.where(np.logical_and(df_f1['peak_4']>=1342.500000000000,df_f1['peak_4']<=1347.900000000000) , df_f1['sn_4'], ""))
df_f1.insert(24, 'f_LC5', np.where(np.logical_and(df_f1['peak_5']>=1342.500000000000,df_f1['peak_5']<=1347.900000000000) , df_f1['peak_5'], ""))
df_f1.insert(25, 'sn_L_5', np.where(np.logical_and(df_f1['peak_5']>=1342.500000000000,df_f1['peak_5']<=1347.900000000000) , df_f1['sn_5'], ""))
df_f1.insert(26, 'f_LC6', np.where(np.logical_and(df_f1['peak_6']>=1342.500000000000,df_f1['peak_6']<=1347.900000000000) , df_f1['peak_6'], ""))
df_f1.insert(27, 'sn_L_6', np.where(np.logical_and(df_f1['peak_6']>=1342.500000000000,df_f1['peak_6']<=1347.900000000000) , df_f1['sn_6'], ""))
		##heavy_chain##
df_f1.insert(28, 'f_HC1', np.where(np.logical_and(df_f1['peak_1']>=3777.300000000000,df_f1['peak_1']<=3792.500000000000) , df_f1['peak_1'], ""))
df_f1.insert(29, 'sn_H_1', np.where(np.logical_and(df_f1['peak_1']>=3777.300000000000,df_f1['peak_1']<=3792.500000000000) , df_f1['sn_1'], ""))
df_f1.insert(30, 'f_HC2', np.where(np.logical_and(df_f1['peak_2']>=3777.300000000000,df_f1['peak_2']<=3792.500000000000) , df_f1['peak_2'], ""))
df_f1.insert(31, 'sn_H_2', np.where(np.logical_and(df_f1['peak_2']>=3777.300000000000,df_f1['peak_2']<=3792.500000000000) , df_f1['sn_2'], ""))
df_f1.insert(32, 'f_HC3', np.where(np.logical_and(df_f1['peak_3']>=3777.300000000000,df_f1['peak_3']<=3792.500000000000) , df_f1['peak_3'], ""))
df_f1.insert(33, 'sn_H_3', np.where(np.logical_and(df_f1['peak_3']>=3777.300000000000,df_f1['peak_3']<=3792.500000000000) , df_f1['sn_3'], ""))
df_f1.insert(34, 'f_HC4', np.where(np.logical_and(df_f1['peak_4']>=3777.300000000000,df_f1['peak_4']<=3792.500000000000) , df_f1['peak_4'], ""))
df_f1.insert(35, 'sn_H_4', np.where(np.logical_and(df_f1['peak_4']>=3777.300000000000,df_f1['peak_4']<=3792.500000000000) , df_f1['sn_4'], ""))
df_f1.insert(36, 'f_HC5', np.where(np.logical_and(df_f1['peak_5']>=3777.300000000000,df_f1['peak_5']<=3792.500000000000) , df_f1['peak_5'], ""))
df_f1.insert(37, 'sn_H_5', np.where(np.logical_and(df_f1['peak_5']>=3777.300000000000,df_f1['peak_5']<=3792.500000000000) , df_f1['sn_5'], ""))
df_f1.insert(38, 'f_HC6', np.where(np.logical_and(df_f1['peak_6']>=3777.300000000000,df_f1['peak_6']<=3792.500000000000) , df_f1['peak_6'], ""))
df_f1.insert(39, 'sn_H_6', np.where(np.logical_and(df_f1['peak_6']>=3777.300000000000,df_f1['peak_6']<=3792.500000000000) , df_f1['sn_6'], ""))
		##f5_light_chain##
df_f1.insert(40, 'f5_LC1', np.where(np.logical_and(df_f1['peak_1']>=1870.300000000000,df_f1['peak_1']<=1877.700000000000) , df_f1['peak_1'], ""))
df_f1.insert(41, 'sn_f5_L_1', np.where(np.logical_and(df_f1['peak_1']>=1870.300000000000,df_f1['peak_1']<=1877.700000000000) , df_f1['sn_1'], ""))
df_f1.insert(42, 'f5_LC2', np.where(np.logical_and(df_f1['peak_2']>=1870.300000000000,df_f1['peak_2']<=1877.700000000000) , df_f1['peak_2'], ""))
df_f1.insert(43, 'sn_f5_L_2', np.where(np.logical_and(df_f1['peak_2']>=1870.300000000000,df_f1['peak_2']<=1877.700000000000) , df_f1['sn_2'], ""))
df_f1.insert(44, 'f5_LC3', np.where(np.logical_and(df_f1['peak_3']>=1870.300000000000,df_f1['peak_3']<=1877.700000000000) , df_f1['peak_3'], ""))
df_f1.insert(45, 'sn_f5_L_3', np.where(np.logical_and(df_f1['peak_3']>=1870.300000000000,df_f1['peak_3']<=1877.700000000000) , df_f1['sn_3'], ""))
df_f1.insert(46, 'f5_LC4', np.where(np.logical_and(df_f1['peak_4']>=1870.300000000000,df_f1['peak_4']<=1877.700000000000) , df_f1['peak_4'], ""))
df_f1.insert(47, 'sn_f5_L_4', np.where(np.logical_and(df_f1['peak_4']>=1870.300000000000,df_f1['peak_4']<=1877.700000000000) , df_f1['sn_4'], ""))
df_f1.insert(48, 'f5_LC5', np.where(np.logical_and(df_f1['peak_5']>=1870.300000000000,df_f1['peak_5']<=1877.700000000000) , df_f1['peak_5'], ""))
df_f1.insert(49, 'sn_f5_L_5', np.where(np.logical_and(df_f1['peak_5']>=1870.300000000000,df_f1['peak_5']<=1877.700000000000) , df_f1['sn_5'], ""))
df_f1.insert(50, 'f5_LC6', np.where(np.logical_and(df_f1['peak_6']>=1870.300000000000,df_f1['peak_6']<=1877.700000000000) , df_f1['peak_6'], ""))
df_f1.insert(51, 'sn_f5_L_6', np.where(np.logical_and(df_f1['peak_6']>=1870.300000000000,df_f1['peak_6']<=1877.700000000000) , df_f1['sn_6'], ""))
		##f5_heavy_chain##
df_f1.insert(52, 'f5_HC1', np.where(np.logical_and(df_f1['peak_1']>=3248.500000000000,df_f1['peak_1']<=3261.500000000000) , df_f1['peak_1'], ""))
df_f1.insert(53, 'sn_f5_H_1', np.where(np.logical_and(df_f1['peak_1']>=3248.500000000000,df_f1['peak_1']<=3261.500000000000) , df_f1['sn_1'], ""))
df_f1.insert(54, 'f5_HC2', np.where(np.logical_and(df_f1['peak_2']>=3248.500000000000,df_f1['peak_2']<=3261.500000000000) , df_f1['peak_2'], ""))
df_f1.insert(55, 'sn_f5_H_2', np.where(np.logical_and(df_f1['peak_2']>=3248.500000000000,df_f1['peak_2']<=3261.500000000000) , df_f1['sn_2'], ""))
df_f1.insert(56, 'f5_HC3', np.where(np.logical_and(df_f1['peak_3']>=3248.500000000000,df_f1['peak_3']<=3261.500000000000) , df_f1['peak_3'], ""))
df_f1.insert(57, 'sn_f5_H_3', np.where(np.logical_and(df_f1['peak_3']>=3248.500000000000,df_f1['peak_3']<=3261.500000000000) , df_f1['sn_3'], ""))
df_f1.insert(58, 'f5_HC4', np.where(np.logical_and(df_f1['peak_4']>=3248.500000000000,df_f1['peak_4']<=3261.500000000000) , df_f1['peak_4'], ""))
df_f1.insert(59, 'sn_f5_H_4', np.where(np.logical_and(df_f1['peak_4']>=3248.500000000000,df_f1['peak_4']<=3261.500000000000) , df_f1['sn_4'], ""))
df_f1.insert(60, 'f5_HC5', np.where(np.logical_and(df_f1['peak_5']>=3248.500000000000,df_f1['peak_5']<=3261.500000000000) , df_f1['peak_5'], ""))
df_f1.insert(61, 'sn_f5_H_5', np.where(np.logical_and(df_f1['peak_5']>=3248.500000000000,df_f1['peak_5']<=3261.500000000000) , df_f1['sn_5'], ""))
df_f1.insert(62, 'f5_HC6', np.where(np.logical_and(df_f1['peak_6']>=3248.500000000000,df_f1['peak_6']<=3261.500000000000) , df_f1['peak_6'], ""))
df_f1.insert(63, 'sn_f5_H_6', np.where(np.logical_and(df_f1['peak_6']>=3248.500000000000,df_f1['peak_6']<=3261.500000000000) , df_f1['sn_6'], ""))
		##intact##
df_f1.insert(64, 'Intact1', np.where(np.logical_and(df_f1['peak_1']>=5100.800000000000,df_f1['peak_1']<=5121.200000000000) , df_f1['peak_1'], ""))
df_f1.insert(65, 'sn_I_1', np.where(np.logical_and(df_f1['peak_1']>=5100.800000000000,df_f1['peak_1']<=5121.200000000000) , df_f1['sn_1'], ""))
df_f1.insert(66, 'Intact2', np.where(np.logical_and(df_f1['peak_2']>=5100.800000000000,df_f1['peak_2']<=5121.200000000000) , df_f1['peak_2'], ""))
df_f1.insert(67, 'sn_I_2', np.where(np.logical_and(df_f1['peak_2']>=5100.800000000000,df_f1['peak_2']<=5121.200000000000) , df_f1['sn_2'], ""))
df_f1.insert(68, 'Intact3', np.where(np.logical_and(df_f1['peak_3']>=5100.800000000000,df_f1['peak_3']<=5121.200000000000) , df_f1['peak_3'], ""))
df_f1.insert(69, 'sn_I_3', np.where(np.logical_and(df_f1['peak_3']>=5100.800000000000,df_f1['peak_3']<=5121.200000000000) , df_f1['sn_3'], ""))
df_f1.insert(70, 'Intact4', np.where(np.logical_and(df_f1['peak_4']>=5100.800000000000,df_f1['peak_4']<=5121.200000000000) , df_f1['peak_4'], ""))
df_f1.insert(71, 'sn_I_4', np.where(np.logical_and(df_f1['peak_4']>=5100.800000000000,df_f1['peak_4']<=5121.200000000000) , df_f1['sn_4'], ""))
df_f1.insert(72, 'Intact5', np.where(np.logical_and(df_f1['peak_5']>=5100.800000000000,df_f1['peak_5']<=5121.200000000000) , df_f1['peak_5'], ""))
df_f1.insert(73, 'sn_I_5', np.where(np.logical_and(df_f1['peak_5']>=5100.800000000000,df_f1['peak_5']<=5121.200000000000) , df_f1['sn_5'], ""))
df_f1.insert(74, 'Intact6', np.where(np.logical_and(df_f1['peak_6']>=5100.800000000000,df_f1['peak_6']<=5121.200000000000) , df_f1['peak_6'], ""))
df_f1.insert(75, 'sn_I_6', np.where(np.logical_and(df_f1['peak_6']>=5100.800000000000,df_f1['peak_6']<=5121.200000000000) , df_f1['sn_6'], ""))
		###a_lc_noise###
df_f1.insert(76, 'a_non_F1', np.where(np.logical_and(df_f1['peak_1']>=0996.800000000000,df_f1['peak_1']<=1000.800000000000) , df_f1['peak_1'], ""))
df_f1.insert(77, 'sn_af_1', np.where(np.logical_and(df_f1['peak_1']>=0996.800000000000,df_f1['peak_1']<=1000.800000000000) , df_f1['sn_1'], ""))
df_f1.insert(78, 'a_non_F2', np.where(np.logical_and(df_f1['peak_2']>=0996.800000000000,df_f1['peak_2']<=1000.800000000000) , df_f1['peak_2'], ""))
df_f1.insert(79, 'sn_af_2', np.where(np.logical_and(df_f1['peak_2']>=0996.800000000000,df_f1['peak_2']<=1000.800000000000) , df_f1['sn_2'], ""))
df_f1.insert(80, 'a_non_F3', np.where(np.logical_and(df_f1['peak_3']>=0996.800000000000,df_f1['peak_3']<=1000.800000000000) , df_f1['peak_3'], ""))
df_f1.insert(81, 'sn_af_3', np.where(np.logical_and(df_f1['peak_3']>=0996.800000000000,df_f1['peak_3']<=1000.800000000000) , df_f1['sn_3'], ""))
df_f1.insert(82, 'a_non_F4', np.where(np.logical_and(df_f1['peak_4']>=0996.800000000000,df_f1['peak_4']<=1000.800000000000) , df_f1['peak_4'], ""))
df_f1.insert(83, 'sn_af_4', np.where(np.logical_and(df_f1['peak_4']>=0996.800000000000,df_f1['peak_4']<=1000.800000000000) , df_f1['sn_4'], ""))
df_f1.insert(84, 'a_non_F5', np.where(np.logical_and(df_f1['peak_5']>=0996.800000000000,df_f1['peak_5']<=1000.800000000000) , df_f1['peak_5'], ""))
df_f1.insert(85, 'sn_af_5', np.where(np.logical_and(df_f1['peak_5']>=0996.800000000000,df_f1['peak_5']<=1000.800000000000) , df_f1['sn_5'], ""))
df_f1.insert(86, 'a_non_F6', np.where(np.logical_and(df_f1['peak_6']>=0996.800000000000,df_f1['peak_6']<=1000.800000000000) , df_f1['peak_6'], ""))
df_f1.insert(87, 'sn_af_6', np.where(np.logical_and(df_f1['peak_6']>=0996.800000000000,df_f1['peak_6']<=1000.800000000000) , df_f1['sn_6'], ""))
		##a_hc_noise##
df_f1.insert(88, 'a_non_F7', np.where(np.logical_and(df_f1['peak_1']>=2302.900000000000,df_f1['peak_1']<=2312.100000000000) , df_f1['peak_1'], ""))
df_f1.insert(89, 'sn_af_7', np.where(np.logical_and(df_f1['peak_1']>=2302.900000000000,df_f1['peak_1']<=2312.100000000000) , df_f1['sn_1'], ""))
df_f1.insert(90, 'a_non_F8', np.where(np.logical_and(df_f1['peak_2']>=2302.900000000000,df_f1['peak_2']<=2312.100000000000) , df_f1['peak_2'], ""))
df_f1.insert(91, 'sn_af_8', np.where(np.logical_and(df_f1['peak_2']>=2302.900000000000,df_f1['peak_2']<=2312.100000000000) , df_f1['sn_2'], ""))
df_f1.insert(92, 'a_non_F9', np.where(np.logical_and(df_f1['peak_3']>=2302.900000000000,df_f1['peak_3']<=2312.100000000000) , df_f1['peak_3'], ""))
df_f1.insert(93, 'sn_af_9', np.where(np.logical_and(df_f1['peak_3']>=2302.900000000000,df_f1['peak_3']<=2312.100000000000) , df_f1['sn_3'], ""))
df_f1.insert(94, 'a_non_F10', np.where(np.logical_and(df_f1['peak_4']>=2302.900000000000,df_f1['peak_4']<=2312.100000000000) , df_f1['peak_4'], ""))
df_f1.insert(95, 'sn_af_10', np.where(np.logical_and(df_f1['peak_4']>=2302.900000000000,df_f1['peak_4']<=2312.100000000000) , df_f1['sn_4'], ""))
df_f1.insert(96, 'a_non_F11', np.where(np.logical_and(df_f1['peak_5']>=2302.900000000000,df_f1['peak_5']<=2312.100000000000) , df_f1['peak_5'], ""))
df_f1.insert(97, 'sn_af_11', np.where(np.logical_and(df_f1['peak_5']>=2302.900000000000,df_f1['peak_5']<=2312.100000000000) , df_f1['sn_5'], ""))
df_f1.insert(98, 'a_non_F12', np.where(np.logical_and(df_f1['peak_6']>=2302.900000000000,df_f1['peak_6']<=2312.100000000000) , df_f1['peak_6'], ""))
df_f1.insert(99, 'sn_af_12', np.where(np.logical_and(df_f1['peak_6']>=2302.900000000000,df_f1['peak_6']<=2312.100000000000) , df_f1['sn_6'], ""))
		##a_intact_noise##
df_f1.insert(100, 'a_non_F13', np.where(np.logical_and(df_f1['peak_1']>=3280.700000000000,df_f1['peak_1']<=3293.700000000000) , df_f1['peak_1'], ""))
df_f1.insert(101, 'sn_af_13', np.where(np.logical_and(df_f1['peak_1']>=3280.700000000000,df_f1['peak_1']<=3293.700000000000) , df_f1['sn_1'], ""))
df_f1.insert(102, 'a_non_F14', np.where(np.logical_and(df_f1['peak_2']>=3280.700000000000,df_f1['peak_2']<=3293.700000000000) , df_f1['peak_2'], ""))
df_f1.insert(103, 'sn_af_14', np.where(np.logical_and(df_f1['peak_2']>=3280.700000000000,df_f1['peak_2']<=3293.700000000000) , df_f1['sn_2'], ""))
df_f1.insert(104, 'a_non_F15', np.where(np.logical_and(df_f1['peak_3']>=3280.700000000000,df_f1['peak_3']<=3293.700000000000) , df_f1['peak_3'], ""))
df_f1.insert(105, 'sn_af_15', np.where(np.logical_and(df_f1['peak_3']>=3280.700000000000,df_f1['peak_3']<=3293.700000000000) , df_f1['sn_3'], ""))
df_f1.insert(106, 'a_non_F16', np.where(np.logical_and(df_f1['peak_4']>=3280.700000000000,df_f1['peak_4']<=3293.700000000000) , df_f1['peak_4'], ""))
df_f1.insert(107, 'sn_af_16', np.where(np.logical_and(df_f1['peak_4']>=3280.700000000000,df_f1['peak_4']<=3293.700000000000) , df_f1['sn_4'], ""))
df_f1.insert(108, 'a_non_F17', np.where(np.logical_and(df_f1['peak_5']>=3280.700000000000,df_f1['peak_5']<=3293.700000000000) , df_f1['peak_5'], ""))
df_f1.insert(109, 'sn_af_17', np.where(np.logical_and(df_f1['peak_5']>=3280.700000000000,df_f1['peak_5']<=3293.700000000000) , df_f1['sn_5'], ""))
df_f1.insert(110, 'a_non_F18', np.where(np.logical_and(df_f1['peak_6']>=3280.700000000000,df_f1['peak_6']<=3293.700000000000) , df_f1['peak_6'], ""))
df_f1.insert(111, 'sn_af_18', np.where(np.logical_and(df_f1['peak_6']>=3280.700000000000,df_f1['peak_6']<=3293.700000000000) , df_f1['sn_6'], ""))
		##b_lc_noise##
df_f1.insert(112, 'b_non_F1', np.where(np.logical_and(df_f1['peak_1']>=1756.500000000000,df_f1['peak_1']<=1763.700000000000) , df_f1['peak_1'], ""))
df_f1.insert(113, 'sn_bf_1', np.where(np.logical_and(df_f1['peak_1']>=1756.500000000000,df_f1['peak_1']<=1763.700000000000) , df_f1['sn_1'], ""))
df_f1.insert(114, 'b_non_F2', np.where(np.logical_and(df_f1['peak_2']>=1756.500000000000,df_f1['peak_2']<=1763.700000000000) , df_f1['peak_2'], ""))
df_f1.insert(115, 'sn_bf_2', np.where(np.logical_and(df_f1['peak_2']>=1756.500000000000,df_f1['peak_2']<=1763.700000000000) , df_f1['sn_2'], ""))
df_f1.insert(116, 'b_non_F3', np.where(np.logical_and(df_f1['peak_3']>=1756.500000000000,df_f1['peak_3']<=1763.700000000000) , df_f1['peak_3'], ""))
df_f1.insert(117, 'sn_bf_3', np.where(np.logical_and(df_f1['peak_3']>=1756.500000000000,df_f1['peak_3']<=1763.700000000000) , df_f1['sn_3'], ""))
df_f1.insert(118, 'b_non_F4', np.where(np.logical_and(df_f1['peak_4']>=1756.500000000000,df_f1['peak_4']<=1763.700000000000) , df_f1['peak_4'], ""))
df_f1.insert(119, 'sn_bf_4', np.where(np.logical_and(df_f1['peak_4']>=1756.500000000000,df_f1['peak_4']<=1763.700000000000) , df_f1['sn_4'], ""))
df_f1.insert(120, 'b_non_F5', np.where(np.logical_and(df_f1['peak_5']>=1756.500000000000,df_f1['peak_5']<=1763.700000000000) , df_f1['peak_5'], ""))
df_f1.insert(121, 'sn_bf_5', np.where(np.logical_and(df_f1['peak_5']>=1756.500000000000,df_f1['peak_5']<=1763.700000000000) , df_f1['sn_5'], ""))
df_f1.insert(122, 'b_non_F6', np.where(np.logical_and(df_f1['peak_6']>=1756.500000000000,df_f1['peak_6']<=1763.700000000000) , df_f1['peak_6'], ""))
df_f1.insert(123, 'sn_bf_6', np.where(np.logical_and(df_f1['peak_6']>=1756.500000000000,df_f1['peak_6']<=1763.700000000000) , df_f1['sn_6'], ""))
		##b_hc_noise##
df_f1.insert(124, 'b_non_F7', np.where(np.logical_and(df_f1['peak_1']>=2277.700000000000,df_f1['peak_1']<=2286.900000000000) , df_f1['peak_1'], ""))
df_f1.insert(125, 'sn_bf_7', np.where(np.logical_and(df_f1['peak_1']>=2277.700000000000,df_f1['peak_1']<=2286.900000000000) , df_f1['sn_1'], ""))
df_f1.insert(126, 'b_non_F8', np.where(np.logical_and(df_f1['peak_2']>=2277.700000000000,df_f1['peak_2']<=2286.900000000000) , df_f1['peak_2'], ""))
df_f1.insert(127, 'sn_bf_8', np.where(np.logical_and(df_f1['peak_2']>=2277.700000000000,df_f1['peak_2']<=2286.900000000000) , df_f1['sn_2'], ""))
df_f1.insert(128, 'b_non_F9', np.where(np.logical_and(df_f1['peak_3']>=2277.700000000000,df_f1['peak_3']<=2286.900000000000) , df_f1['peak_3'], ""))
df_f1.insert(129, 'sn_bf_9', np.where(np.logical_and(df_f1['peak_3']>=2277.700000000000,df_f1['peak_3']<=2286.900000000000) , df_f1['sn_3'], ""))
df_f1.insert(130, 'b_non_F10', np.where(np.logical_and(df_f1['peak_4']>=2277.700000000000,df_f1['peak_4']<=2286.900000000000) , df_f1['peak_4'], ""))
df_f1.insert(131, 'sn_bf_10', np.where(np.logical_and(df_f1['peak_4']>=2277.700000000000,df_f1['peak_4']<=2286.900000000000) , df_f1['sn_4'], ""))
df_f1.insert(132, 'b_non_F11', np.where(np.logical_and(df_f1['peak_5']>=2277.700000000000,df_f1['peak_5']<=2286.900000000000) , df_f1['peak_5'], ""))
df_f1.insert(133, 'sn_bf_11', np.where(np.logical_and(df_f1['peak_5']>=2277.700000000000,df_f1['peak_5']<=2286.900000000000) , df_f1['sn_5'], ""))
df_f1.insert(134, 'b_non_F12', np.where(np.logical_and(df_f1['peak_6']>=2277.700000000000,df_f1['peak_6']<=2286.900000000000) , df_f1['peak_6'], ""))
df_f1.insert(135, 'sn_bf_12', np.where(np.logical_and(df_f1['peak_6']>=2277.700000000000,df_f1['peak_6']<=2286.900000000000) , df_f1['sn_6'], ""))
		##b_intact_noise##
df_f1.insert(136, 'b_non_F13', np.where(np.logical_and(df_f1['peak_1']>=4018.400000000000,df_f1['peak_1']<=4034.600000000000) , df_f1['peak_1'], ""))
df_f1.insert(137, 'sn_bf_13', np.where(np.logical_and(df_f1['peak_1']>=4018.400000000000,df_f1['peak_1']<=4034.600000000000) , df_f1['sn_1'], ""))
df_f1.insert(138, 'b_non_F14', np.where(np.logical_and(df_f1['peak_2']>=4018.400000000000,df_f1['peak_2']<=4034.600000000000) , df_f1['peak_2'], ""))
df_f1.insert(139, 'sn_bf_14', np.where(np.logical_and(df_f1['peak_2']>=4018.400000000000,df_f1['peak_2']<=4034.600000000000) , df_f1['sn_2'], ""))
df_f1.insert(140, 'b_non_F15', np.where(np.logical_and(df_f1['peak_3']>=4018.400000000000,df_f1['peak_3']<=4034.600000000000) , df_f1['peak_3'], ""))
df_f1.insert(141, 'sn_bf_15', np.where(np.logical_and(df_f1['peak_3']>=4018.400000000000,df_f1['peak_3']<=4034.600000000000) , df_f1['sn_3'], ""))
df_f1.insert(142, 'b_non_F16', np.where(np.logical_and(df_f1['peak_4']>=4018.400000000000,df_f1['peak_4']<=4034.600000000000) , df_f1['peak_4'], ""))
df_f1.insert(143, 'sn_bf_16', np.where(np.logical_and(df_f1['peak_4']>=4018.400000000000,df_f1['peak_4']<=4034.600000000000) , df_f1['sn_4'], ""))
df_f1.insert(144, 'b_non_F17', np.where(np.logical_and(df_f1['peak_5']>=4018.400000000000,df_f1['peak_5']<=4034.600000000000) , df_f1['peak_5'], ""))
df_f1.insert(145, 'sn_bf_17', np.where(np.logical_and(df_f1['peak_5']>=4018.400000000000,df_f1['peak_5']<=4034.600000000000) , df_f1['sn_5'], ""))
df_f1.insert(146, 'b_non_F18', np.where(np.logical_and(df_f1['peak_6']>=4018.400000000000,df_f1['peak_6']<=4034.600000000000) , df_f1['peak_6'], ""))
df_f1.insert(147, 'sn_bf_18', np.where(np.logical_and(df_f1['peak_6']>=4018.400000000000,df_f1['peak_6']<=4034.600000000000) , df_f1['sn_6'], ""))
		##e_lc_noice##
df_f1.insert(148, 'e_non_F1', np.where(np.logical_and(df_f1['peak_1']>=1129.200000000000,df_f1['peak_1']<=1133.800000000000) , df_f1['peak_1'], ""))
df_f1.insert(149, 'sn_ef_1', np.where(np.logical_and(df_f1['peak_1']>=1129.200000000000,df_f1['peak_1']<=1133.800000000000) , df_f1['sn_1'], ""))
df_f1.insert(150, 'e_non_F2', np.where(np.logical_and(df_f1['peak_2']>=1129.200000000000,df_f1['peak_2']<=1133.800000000000) , df_f1['peak_2'], ""))
df_f1.insert(151, 'sn_ef_2', np.where(np.logical_and(df_f1['peak_2']>=1129.200000000000,df_f1['peak_2']<=1133.800000000000) , df_f1['sn_2'], ""))
df_f1.insert(152, 'e_non_F3', np.where(np.logical_and(df_f1['peak_3']>=1129.200000000000,df_f1['peak_3']<=1133.800000000000) , df_f1['peak_3'], ""))
df_f1.insert(153, 'sn_ef_3', np.where(np.logical_and(df_f1['peak_3']>=1129.200000000000,df_f1['peak_3']<=1133.800000000000) , df_f1['sn_3'], ""))
df_f1.insert(154, 'e_non_F4', np.where(np.logical_and(df_f1['peak_4']>=1129.200000000000,df_f1['peak_4']<=1133.800000000000) , df_f1['peak_4'], ""))
df_f1.insert(155, 'sn_ef_4', np.where(np.logical_and(df_f1['peak_4']>=1129.200000000000,df_f1['peak_4']<=1133.800000000000) , df_f1['sn_4'], ""))
df_f1.insert(156, 'e_non_F5', np.where(np.logical_and(df_f1['peak_5']>=1129.200000000000,df_f1['peak_5']<=1133.800000000000) , df_f1['peak_5'], ""))
df_f1.insert(157, 'sn_ef_5', np.where(np.logical_and(df_f1['peak_5']>=1129.200000000000,df_f1['peak_5']<=1133.800000000000) , df_f1['sn_5'], ""))
df_f1.insert(158, 'e_non_F6', np.where(np.logical_and(df_f1['peak_6']>=1129.200000000000,df_f1['peak_6']<=1133.800000000000) , df_f1['peak_6'], ""))
df_f1.insert(159, 'sn_ef_6', np.where(np.logical_and(df_f1['peak_6']>=1129.200000000000,df_f1['peak_6']<=1133.800000000000) , df_f1['sn_6'], ""))
		##e_hc_noise##
df_f1.insert(160, 'e_non_F7', np.where(np.logical_and(df_f1['peak_1']>=2493.600000000000,df_f1['peak_1']<=2503.600000000000) , df_f1['peak_1'], ""))
df_f1.insert(161, 'sn_ef_7', np.where(np.logical_and(df_f1['peak_1']>=2493.600000000000,df_f1['peak_1']<=2503.600000000000) , df_f1['sn_1'], ""))
df_f1.insert(162, 'e_non_F8', np.where(np.logical_and(df_f1['peak_2']>=2493.600000000000,df_f1['peak_2']<=2503.600000000000) , df_f1['peak_2'], ""))
df_f1.insert(163, 'sn_ef_8', np.where(np.logical_and(df_f1['peak_2']>=2493.600000000000,df_f1['peak_2']<=2503.600000000000) , df_f1['sn_2'], ""))
df_f1.insert(164, 'e_non_F9', np.where(np.logical_and(df_f1['peak_3']>=2493.600000000000,df_f1['peak_3']<=2503.600000000000) , df_f1['peak_3'], ""))
df_f1.insert(165, 'sn_ef_9', np.where(np.logical_and(df_f1['peak_3']>=2493.600000000000,df_f1['peak_3']<=2503.600000000000) , df_f1['sn_3'], ""))
df_f1.insert(166, 'e_non_F10', np.where(np.logical_and(df_f1['peak_4']>=2493.600000000000,df_f1['peak_4']<=2503.600000000000) , df_f1['peak_4'], ""))
df_f1.insert(167, 'sn_ef_10', np.where(np.logical_and(df_f1['peak_4']>=2493.600000000000,df_f1['peak_4']<=2503.600000000000) , df_f1['sn_4'], ""))
df_f1.insert(168, 'e_non_F11', np.where(np.logical_and(df_f1['peak_5']>=2493.600000000000,df_f1['peak_5']<=2503.600000000000) , df_f1['peak_5'], ""))
df_f1.insert(169, 'sn_ef_11', np.where(np.logical_and(df_f1['peak_5']>=2493.600000000000,df_f1['peak_5']<=2503.600000000000) , df_f1['sn_5'], ""))
df_f1.insert(170, 'e_non_F12', np.where(np.logical_and(df_f1['peak_6']>=2493.600000000000,df_f1['peak_6']<=2503.600000000000) , df_f1['peak_6'], ""))
df_f1.insert(171, 'sn_ef_12', np.where(np.logical_and(df_f1['peak_6']>=2493.600000000000,df_f1['peak_6']<=2503.600000000000) , df_f1['sn_6'], ""))
		##e_intact_noise##
df_f1.insert(172, 'e_non_F13', np.where(np.logical_and(df_f1['peak_1']>=3607.800000000000,df_f1['peak_1']<=3622.200000000000) , df_f1['peak_1'], ""))
df_f1.insert(173, 'sn_ef_13', np.where(np.logical_and(df_f1['peak_1']>=3607.800000000000,df_f1['peak_1']<=3622.200000000000) , df_f1['sn_1'], ""))
df_f1.insert(174, 'e_non_F14', np.where(np.logical_and(df_f1['peak_2']>=3607.800000000000,df_f1['peak_2']<=3622.200000000000) , df_f1['peak_2'], ""))
df_f1.insert(175, 'sn_ef_14', np.where(np.logical_and(df_f1['peak_2']>=3607.800000000000,df_f1['peak_2']<=3622.200000000000) , df_f1['sn_2'], ""))
df_f1.insert(176, 'e_non_F15', np.where(np.logical_and(df_f1['peak_3']>=3607.800000000000,df_f1['peak_3']<=3622.200000000000) , df_f1['peak_3'], ""))
df_f1.insert(177, 'sn_ef_15', np.where(np.logical_and(df_f1['peak_3']>=3607.800000000000,df_f1['peak_3']<=3622.200000000000) , df_f1['sn_3'], ""))
df_f1.insert(178, 'e_non_F16', np.where(np.logical_and(df_f1['peak_4']>=3607.800000000000,df_f1['peak_4']<=3622.200000000000) , df_f1['peak_4'], ""))
df_f1.insert(179, 'sn_ef_16', np.where(np.logical_and(df_f1['peak_4']>=3607.800000000000,df_f1['peak_4']<=3622.200000000000) , df_f1['sn_4'], ""))
df_f1.insert(180, 'e_non_F17', np.where(np.logical_and(df_f1['peak_5']>=3607.800000000000,df_f1['peak_5']<=3622.200000000000) , df_f1['peak_5'], ""))
df_f1.insert(181, 'sn_ef_17', np.where(np.logical_and(df_f1['peak_5']>=3607.800000000000,df_f1['peak_5']<=3622.200000000000) , df_f1['sn_5'], ""))
df_f1.insert(182, 'e_non_F18', np.where(np.logical_and(df_f1['peak_6']>=3607.800000000000,df_f1['peak_6']<=3622.200000000000) , df_f1['peak_6'], ""))
df_f1.insert(183, 'sn_ef_18', np.where(np.logical_and(df_f1['peak_6']>=3607.800000000000,df_f1['peak_6']<=3622.200000000000) , df_f1['sn_6'], ""))

df_f2 = df_f1.drop(['test','peak_1','sn_1','peak_2','sn_2','peak_3','sn_3',\
'peak_4','sn_4','peak_5','sn_5','peak_6','sn_6'], axis=1)
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


df_final = df_fa1[::2]
df_final.to_csv("test3.csv", sep="\t")
print(df_final)
df_final = df_final.loc[:, ~df_final.columns.str.contains('^Unnamed')]
df_final = df_final.loc[:, ~df_final.columns.duplicated()]
#df_final.to_csv("test.csv", sep="\t")

df_final_2 = df_final[['date','plate','bot_id','LC_F','HC_F','Intact_F']]
df_final_2.columns = ['date','plate','bot_id','Peak_1_F','Peak_2_F','Intact_F']

df_final_3 = df_final_2.round(decimals=1)
df_final_3['Peak_1_F'].values[df_final_3['Peak_1_F'] > 0] = 1
df_final_3['Peak_2_F'].values[df_final_3['Peak_2_F'] > 0] = 1
df_final_3['Intact_F'].values[df_final_3['Intact_F'] > 0] = 1
df_final_3 = df_final_3.sort_values(['date', 'plate', 'bot_id']).fillna(0)

df_4 = df_final_3.copy()
df_4.drop_duplicates(subset=None,keep='first', inplace=True)

'''
df_4['A_bool'] = df_4['Peak_1_A'] != df_4['Peak_2_A']
df_4['B_bool'] = df_4['Peak_1_B'] != df_4['Peak_2_B']
df_4['E_bool'] = df_4['Peak_1_E'] != df_4['Peak_2_E']
df_4['F_bool'] = df_4['Peak_1_F'] != df_4['Peak_2_F']
print(df_4)
'''


df_4['Peak_1_F'] = np.where(np.logical_and(df_4['Peak_1_F']==0,df_4['Peak_2_F']==1) , -1 , df_4['Peak_1_F'])
df_4['Peak_2_F'] = np.where(np.logical_and(df_4['Peak_1_F']==1,df_4['Peak_2_F']==0) , -1 , df_4['Peak_2_F'])

def high_1(val):
	if val > 0:
		color = '#009933'
	elif val == -1:
		color = '#FFCC33'
	else:
		color = '#FF6666'
	return 'background-color: %s' % color

df_4 = df_4.reset_index(drop=True).style.applymap(high_1, subset=pd.IndexSlice[:, ['Peak_1_A','Peak_2_A','Intact_A','Peak_1_B','Peak_2_B','Intact_B',\
'Peak_1_E','Peak_2_E','Intact_E','Peak_1_F','Peak_2_F','Intact_F']])
df_4.to_excel("endopep_peak_list_b.xlsx", index=False)



print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
