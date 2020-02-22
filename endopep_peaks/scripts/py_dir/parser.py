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

f = open("df_input_1.txt", "r")
a_out = open("a_out.txt", "w")
b_out = open("b_out.txt", "w")
e_out = open("e_out.txt", "w")
f_out = open("f_out.txt", "w")
for line in f.readlines():
	if line.startswith("#"):
		pass
	else:
#		print(line)
		tabs = line.split("\t")
		run_date = tabs[0]
		plate_id = tabs[1]
		bot_id = tabs[2]
		test = tabs[3]
		print(test)
#		peaks = tabs[5]

		if test == "A":
			print(line)
			a_out.write(line)
		elif test == "B":
			print(line)
			b_out.write(line)
		elif test == "E":
			print(line)
			e_out.write(line)
		elif test == "F":
			print(line)
			f_out.write(line)
		else:
			pass
