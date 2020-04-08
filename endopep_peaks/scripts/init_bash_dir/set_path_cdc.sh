#!/bin/bash

cd endopep_peaks_v2.30
mv -f endopep_peaks ~
cd ~
rm -fr endopep_peaks_v2.30

echo  "alias endopep_peaks='python ~/endopep_peaks/scripts/endopep.py'" >> ~/.bashrc
echo "alias init_cdc='source ~/endopep_peaks/scripts/init_bash_dir/hpc_biolinux_module_init.sh'" >>~/.bashrc
