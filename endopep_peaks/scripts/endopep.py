import os
import sys
import argparse
import subprocess
import re
import glob
import shlex
import operator
import textwrap
from collections import defaultdict
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(prog='endopep_peaks',\
formatter_class=argparse.RawDescriptionHelpFormatter,\
description='''################################\n\
## generate human readable mass spec data from a standard Bruker output ##\n \
m/z = (mass)/(charged # of ions)\n \
sn = signal to noise value''',\
epilog = textwrap.dedent('''\
################################
Development: E.W. Getz, 2020
Version: v2.30
Source: https://github.com/bioshaolin/endopep_peaks_v2.30
CDC/ DDID/ NCEZID/ DFWED/ EDLB/
'''))
tutorial = parser.add_argument_group('## tutorials')
required = parser.add_argument_group('## required arguments')
output = parser.add_argument_group('## output arguments')
optional = parser.add_argument_group('## optional arguments')
parser.add_argument('-read', '--read', help="Show Read.me", action="store_true")
parser.add_argument('-dep', '--dependencies', help="List the program dependencies for endopep_peaks", action="store_true")
parser.add_argument('-init', help='[initialize:HPC] or install dependencies (cdc/external)')
tutorial.add_argument('-vids', '--modules', help="Download tutorial modules (required for tutorial)", action="store_true")
tutorial.add_argument('-tutorial', help="Prompt tutorial modules (all/intro/run/type/output/vis)")
required.add_argument('-type',help="Specify which serotypes are being assesed (all/a/b/e/f)")
output.add_argument('-n' , '--noise' , help="Generate a separate noise output (NO sn)", action="store_true")
output.add_argument('-b', '--boolean', help="Generate a boolean value output (NO sn) (NO m/z)", action="store_true")
output.add_argument('-c', '--clia', help="Generate a standard output (m/z)(sn)", action="store_true")
optional.add_argument('-clear', '--clear_all', help="Clear previous outputs from current input directory", action="store_true")
optional.add_argument('-visual', '--visual', help="Generate a visual to compare against reference data (Yes:-c | NO:-b,-n)", action="store_true")
parser._optionals.title="## help arguments"
args = parser.parse_args()


if args.clia and args.boolean and args.clear_all and args.visual:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0bvclear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0bvclear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0bvclear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0bvclear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0bvclear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0bvclear_v2.1.sh", shell=True)
elif args.clia and args.boolean and args.visual:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0bv_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0bv_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0bv_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0bv_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0bv_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0bv_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0bv_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0bv_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0bv_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0bv_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0bv_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0bv_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0bv_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0bv_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0bv_v2.1.sh", shell=True)
elif args.clia and args.boolean and args.clear_all:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0bclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0bclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0bclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0bclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0bclear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0bclear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0bclear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0bclear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0bclear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0bclear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0bclear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0bclear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0bclear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0bclear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0bclear_v2.1.sh", shell=True)
elif args.boolean and args.clia:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0b_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0b_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0b_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0b_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0b_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0b_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0b_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0b_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0b_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0b_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0b_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0b_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0b_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0b_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0b_v2.1.sh", shell=True)
elif args.clia and args.noise and args.clear_all and args.visual:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0nvclear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0nvclear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0nvclear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0nvclear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0nvclear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0nvclear_v2.1.sh", shell=True)
elif args.clia and args.noise and args.visual:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0nv_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0nv_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0nv_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0nv_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0nv_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0nv_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0nv_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0nv_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0nv_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0nv_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0nv_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0nv_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0nv_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0nv_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0nv_v2.1.sh", shell=True)
elif args.clia and args.noise and args.clear_all:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0nclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0nclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0nclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0nclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0nclear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0nclear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0nclear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0nclear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0nclear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0nclear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0nclear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0nclear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0nclear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0nclear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0nclear_v2.1.sh", shell=True)
elif args.clia and args.noise:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0n_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0n_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0n_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0n_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0n_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0n_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0n_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0n_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0n_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0n_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0n_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0n_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0n_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0n_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0n_v2.1.sh", shell=True)
elif args.clia and args.clear_all and args.visual:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0vclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0vclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0vclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0vclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0vclear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0vclear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0vclear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0vclear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0vclear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0vclear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0vclear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0vclear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0vclear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0vclear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0vclear_v2.1.sh", shell=True)
elif args.clia and args.visual:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0v_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0v_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0v_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0v_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0v_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0v_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0v_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0v_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0v_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0v_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0v_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0v_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0v_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0v_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0v_v2.1.sh", shell=True)
elif args.clia and args.clear_all:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0clear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0clear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0clear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0clear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0clear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0clear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0clear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0clear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0clear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0clear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0clear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0clear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0clear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0clear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0clear_v2.1.sh", shell=True)
elif args.clia:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_0_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_0_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_0_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_0_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_0_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_0_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_0_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_0_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_0_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_0_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_0_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_0_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_0_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_0_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_0_v2.1.sh", shell=True)
elif args.boolean and args.noise and args.clear_all:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_nbclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_nbclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_nbclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_nbclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_nbclear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_nbclear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_nbclear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_nbclear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_nbclear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_nbclear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_nbclear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_nbclear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_nbclear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_nbclear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_nbclear_v2.1.sh", shell=True)
elif args.boolean and args.noise:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_nb_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_nb_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_nb_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_nb_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_nb_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_nb_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_nb_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_nb_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_nb_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_nb_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_nb_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_nb_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_nb_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_nb_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_nb_v2.1.sh", shell=True)
elif args.boolean and args.clear_all:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_bclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_bclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_bclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_bclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_bclear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_bclear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_bclear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_bclear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_bclear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_bclear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_bclear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_bclear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_bclear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_bclear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_bclear_v2.1.sh", shell=True)
elif args.boolean:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_b_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_b_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_b_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_b_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_b_v2.1.sh", shell=True)
elif args.noise and args.clear_all:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_nclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_nclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_nclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_nclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_nclear_v2.1.sh", shell=True)
elif args.noise:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_n_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_n_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_n_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_n_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_n_v2.1.sh", shell=True)
elif args.clear_all and args.visual:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_vclear_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_vclear_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_vclear_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_vclear_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_vclear_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_vclear_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_vclear_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_vclear_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_vclear_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_vclear_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_vclear_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_vclear_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_vclear_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_vclear_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_vclear_v2.1.sh", shell=True)
elif args.visual:
	if args.type == 'all':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/all_dir/endopep_get_peaks_v_v2.1.sh", shell=True)
	elif args.type == 'a':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/a_dir/endopep_get_peaks_a_v_v2.1.sh", shell=True)
	elif args.type == 'b':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/b_dir/endopep_get_peaks_b_v_v2.1.sh", shell=True)
	elif args.type == 'e':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/e_dir/endopep_get_peaks_e_v_v2.1.sh", shell=True)
	elif args.type == 'f':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/f_dir/endopep_get_peaks_f_v_v2.1.sh", shell=True)
	elif args.type == 'ab' or args.type == 'ba':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ab_dir/endopep_get_peaks_ab_v_v2.1.sh", shell=True)
	elif args.type == 'ae' or args.type == 'ea':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ae_dir/endopep_get_peaks_ae_v_v2.1.sh", shell=True)
	elif args.type == 'af' or args.type == 'fa':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/af_dir/endopep_get_peaks_af_v_v2.1.sh", shell=True)
	elif args.type == 'be' or args.type == 'eb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/be_dir/endopep_get_peaks_be_v_v2.1.sh", shell=True)
	elif args.type == 'bf' or args.type == 'fb':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bf_dir/endopep_get_peaks_bf_v_v2.1.sh", shell=True)
	elif args.type == 'ef' or args.type == 'fe':
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/ef_dir/endopep_get_peaks_ef_v_v2.1.sh", shell=True)
	elif args.type in {'abe','aeb','bae','bea','eab','eba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abe_dir/endopep_get_peaks_abe_v_v2.1.sh", shell=True)
	elif args.type in {'abf','afb','baf','bfa','fab','fba'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/abf_dir/endopep_get_peaks_abf_v_v2.1.sh", shell=True)
	elif args.type in {'aef','afe','eaf','efa','fae','fea'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/aef_dir/endopep_get_peaks_aef_v_v2.1.sh", shell=True)
	elif args.type in {'bef','bfe','ebf','efb','fbe','feb'}:
		subprocess.call("bash ~/endopep_peaks/scripts/bash_dir/bef_dir/endopep_get_peaks_bef_v_v2.1.sh", shell=True)
elif args.tutorial:
	if args.tutorial == 'all':
		subprocess.call("python ~/endopep_peaks/scripts/py_dir/vid_dir/vid_tut_all.py", shell=True)
	elif args.tutorial == 'intro':
		subprocess.call("python ~/endopep_peaks/scripts/py_dir/vid_dir/vid_tut_intro.py", shell=True)
	elif args.tutorial == 'run':
		subprocess.call("python ~/endopep_peaks/scripts/py_dir/vid_dir/vid_tut_run.py", shell=True)
	elif args.tutorial == 'type':
		subprocess.call("python ~/endopep_peaks/scripts/py_dir/vid_dir/vid_tut_type.py", shell=True)
	elif args.tutorial == 'output':
		subprocess.call("python ~/endopep_peaks/scripts/py_dir/vid_dir/vid_tut_output.py", shell=True)
	elif args.tutorial == 'vis' or args.tutorial == 'visual':
		subprocess.call("python ~/endopep_peaks/scripts/py_dir/vid_dir/vid_tut_visual.py", shell=True)
	else:
		pass
elif args.modules:
	subprocess.call("bash ~/endopep_peaks/scripts/init_bash_dir/vid_mod_init.sh", shell=True)
elif args.read:
	subprocess.call("cat ~/endopep_peaks/Read.me", shell=True)
elif args.dependencies:
	subprocess.call("cat ~/endopep_peaks/Read.me | tail -15", shell=True)
elif args.init:
	if args.init == 'cdc':
		subprocess.call("bash ~/endopep_peaks/scripts/init_bash_dir/hpc_biolinux_module_init.sh", shell=True)
	elif args.init == 'external':
		subprocess.call("bash ~/endopep_peaks/scripts/init_bash_dir/external_dep_install.sh", shell=True)
elif len(sys.argv[1:]) == 0:
	parser.print_help()
	parser.exit()
