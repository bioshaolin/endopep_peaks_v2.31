#!/bin/bash

pip install gdown
cd ~/endopep_peaks/scripts/py_dir/vid_dir
gdown --id 1rN8IbZQouXgzkGVsgdwu_IFjZAWpIzZU --output vid_tutorials_dir.tar.gz
tar -xvf vid_tutorials_dir.tar.gz
mv -f desktop/vid_tutorials_dir/* .
rm -fr desktop
rm -f vid_tutorials_dir.tar.gz
cd ~
