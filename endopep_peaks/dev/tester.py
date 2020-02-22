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

f = open("temp_SN_2.txt", "r")
f1 = open("peak_2.csv", "r")
peak_dict = defaultdict(list)
peak2_dict = defaultdict(list)
o = open("output.txt", "w")

for line in f.readlines():
	if line.startswith("\t"):
		pass
	elif line.startswith("m/z"):
		pass
	elif line.startswith('"Spectr"'):
		pass
	else:
		tabs = line.split("\t")
		peak = tabs[0]
		sn = tabs[1]
#		print(sn)
		peak_dict[peak] = peak + "," + sn
#		print(peak_dict[peak])

for line in f1.readlines():
	if line.startswith("###"):
		pass
	else:
		tabs = line.split("\t")
		date = tabs[0]
		plate = tabs[1]
		bot_id = tabs[2]
		peaks1 = tabs[3]
		peaks2 = tabs[4]
		peaks3 = tabs[5]
#		print(peaks)
		peak2_dict[peaks1] = peaks1
		peak2_dict[peaks2] = peaks2
		peak2_dict[peaks3] = peaks3

		f1_dict = defaultdict(list)
		f2_dict = defaultdict(list)
		f3_dict = defaultdict(list)
for key in peak_dict.keys():
	print(key)
	if key == peak2_dict[peaks1]:
		f1_dict[key] = peak_dict[peak]
	elif key == peak2_dict[peaks2]:
		f2_dict[key] = peak_dict[peak]
	elif key == peak2_dict[peaks3]:
		f3_dict[key] = peak_dict[peak]
#	elif key == peak2_dict[peaks2]:
#	elif key == peak2_dict[peaks3]:
#		f3_dict[peaks3] = peak_dict[peak]
#	print(key)
	o.write(str(f1_dict[key]) + "\t" + str(f2_dict[key]) + "\t" + str(f3_dict[key]))
#+ "\t" + f2_dict[peaks2] + "\t" + f3_dict[peaks3])
