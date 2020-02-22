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
name_dict = defaultdict(list)


for line in f.readlines():
	if line.startswith("\n"):
		pass
	elif line.startswith('"Spec"'):
		name_dict[line] = line
	elif line.startswith(('0','1','2','3','4','5','6','7','8','9')):
		print(line)
