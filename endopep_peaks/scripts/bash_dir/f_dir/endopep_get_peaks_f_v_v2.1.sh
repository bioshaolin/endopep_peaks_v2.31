#!/bin/bash
cd ~/endopep_peaks
tput setaf 2 ; echo "




............"; tput sgr 0
tput setaf 2 ; echo "............"; tput sgr 0
tput setaf 2 ; echo "Verify Input Directory has been placed in ~/endopep_peaks"; tput sgr 0
tput setaf 2 ; echo "............"; tput sgr 0
tput setaf 2 ; echo "............"; tput sgr 0
echo "


## NOTE: when running '-visual' as singular output verify
endopep_peak_list_0_(date) is set to current date. ##"
read -p "


Input Directory?   " choice
chmod 777 $choice
cd ~/endopep_peaks/$choice

rm -f temp_1.csv
rm -f temp_1.txt
rm -f temp_2.txt
rm -f temp_3.txt
rm -f temp_4.txt
rm -f temp_5.txt
rm -f temp_6.txt
rm -f temp_7.txt
rm -f temp_8.txt
rm -f temp_9.txt
rm -f temp_10.txt
rm -f *.xlsx.csv

rm -f *_out.txt
rm -f *_df.txt
rm -f df_input_1.txt
rm -f test.csv
rm -f test2.csv
rm -f test3.csv
rm -f compile.csv

ssconvert endopep_peak_list_0_$(date +%m.%d.%Y).xlsx endo.csv 2>/dev/null
python ~/endopep_peaks/scripts/py_dir/vis_dir/stack_visual_f
.py
rm -f endo.csv

chmod 777 endopep_peak_list_0_$(date +%m.%d.%Y).xlsx
chmod 777 Peak_Values_$(date +%m.%d.%Y).png
chmod 777 SN_Gradient_Legend_$(date +%m.%d.%Y).png
echo "............................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
........ !                                              ! ........
........                                                  ........
........                                                  ........
........                                                  ........
........                                                  ........
........                                                  ........
........ !                                              ! ........
..................................................................
..................................................................


"
read -p "Keep peak list and figures in input directory or specify a path? (k/s)
(Keep = k, specify = s)   " choice2
if [ "$choice2"  == 'k' ] ; then
	cd ~
	mv -f ~/endopep_peaks/endopep_peak_list_0_$(date +%m.%d.%Y).xlsx ~/endopep_peaks/$choice
	mv -f ~/endopep_peaks/Peak_Values_$(date +%m.%d.%Y).png ~/endopep_peaks/$choice
	mv -f ~/endopep_peaks/SN_Gradient_Legend_$(date +%m.%d.%Y).png ~/endopep_peaks/$choice
	echo "..........................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
..................................................................
........ !                                              ! ........
........   ####  #    #  ###   ####  #####  ####  #####   ........
........   #     # #  #  #  #  #  #  #   #  #     #   #   ........
........   ###   #  # #  #  #  #  #  #####  ###   #####   ........
........   #     #   ##  #  #  #  #  #      #     #       ........
........   ####  #    #  ###   ####  #      ####  #       ........
........ !                                              ! ........
..................................................................
.................................................................."
elif [ "$choice2" = 's' ] ; then
	tput setaf 2 ; echo "




............"; tput sgr 0
	tput setaf 2 ; echo "............"; tput sgr 0
	tput setaf 2 ; echo "home(~) is your current directory"; tput sgr 0
	tput setaf 2 ; echo "An example path would be:"; tput sgr 0; echo "data/clia/2019"
	tput setaf 2 ; echo "............"; tput sgr 0
	tput setaf 2 ; echo "............"; tput sgr 0
	read -p "Path for endopep_peak_list to be stored?   " choice3
	if [ "$choice3" == $choice3 ] ; then
		cd ~
		mv -f ~/endopep_peaks/endopep_peak_list_0_$(date +%m.%d.%Y).xlsx $choice3
		mv -f ~/endopep_peaks/Peak_Values_$(date +%m.%d.%Y).png $choice3
		mv -f ~/endopep_peaks/SN_Gradient_Legend_$(date +%m.%d.%Y).png $choice3
		echo "..........................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	..................................................................
	........ !                                              ! ........
	........   ####  #    #  ###   ####  #####  ####  #####   ........
	........   #     # #  #  #  #  #  #  #   #  #     #   #   ........
	........   ###   #  # #  #  #  #  #  #####  ###   #####   ........
	........   #     #   ##  #  #  #  #  #      #     #       ........
	........   ####  #    #  ###   ####  #      ####  #       ........
	........ !                                              ! ........
	..................................................................
	.................................................................."
	fi
fi
