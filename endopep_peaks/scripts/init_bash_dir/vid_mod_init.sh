#!/bin/bash
read -p "are you accessing internal or external?
(i = internal, e = external)   " choice
if [ "$choice" == 'e' ] ; then
	pip install gdown
	cd ~/endopep_peaks/scripts/py_dir/vid_dir
	gdown --id 1rN8IbZQouXgzkGVsgdwu_IFjZAWpIzZU --output vid_tutorials_dir.tar.gz
	tar -xvf vid_tutorials_dir.tar.gz
	mv -f desktop/vid_tutorials_dir/* .
	rm -fr desktop
	rm -f vid_tutorials_dir.tar.gz
	cd ~
elif [ "$choice" == 'i' ] ; then
	echo "Follow shared drive link to download video modules:"
	echo "
https://drive.google.com/open?id=1rN8IbZQouXgzkGVsgdwu_IFjZAWpIzZU"
echo "
Once downloaded move modules to:"
tput setaf 2; echo "~/endopep_peaks/scripts/py_dir/vid_dir"; tput sgr 0
echo "
You can now delete the download manager directory (desktop/vid_tutorials_dir)"
fi
