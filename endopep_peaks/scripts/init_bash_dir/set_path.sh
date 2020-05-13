#!/bin/bash

cd endopep_peaks_v2.31
mv -f endopep_peaks ~
cd ~
rm -fr endopep_peaks_v2.31

echo  "alias endopep_peaks='python ~/endopep_peaks/scripts/endopep.py'" >> ~/.bashrc
