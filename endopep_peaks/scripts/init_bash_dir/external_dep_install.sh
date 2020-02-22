#!/bin/bash

echo "............................................................"
tput setaf 2 ; echo "Note: For use of endopep_peaks, accessibility to GNU bash commands
is required"; tput sgr 0

read -p "If you are using Windows OS abort here and install
a git bash agent before re-run. (a,c)
(a = abort, c = continue):   " choice
if [ "$choice" == 'a' ] ; then
	:
elif [ "$choice" == 'c' ] ; then
	read -p "Are you currently running >= Python3.6.8? (y/n)  " choice2
	if [ "$choice2"  == 'y' ] ; then
		pip install pandas
		pip install argparse
		pip install markdown-textwrap
		pip install matplotlib
		sudo apt-get install gnumeric
		sudo apt-get install ffmpeg
	elif [ "$choice2" == 'n' ] ; then
		tput setaf 1 ; echo "Update Python to v >= 3.6.8"; tput sgr 0
		echo "This can be set temporarily by creating a conda
environment with version control."
		echo "..............................."
		echo "..............................."
		echo "To create a version controlled environment run the following:

		Pre endopep_peaks run
		---------------------
		conda create --name py3 python=3.6.8
		conda activate py3

		Post endopep_peaks run
		----------------------
		conda deactivate"
	fi
fi
