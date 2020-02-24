#!/bin/bash

cd endopep_peaks_v2.30
mv -f endopep_peaks ~
cd ~
rm -f endopep_peaks_v2.30

echo  "alias endopep_peaks='python ~/endopep_peaks/scripts/endopep.py'" >> ~/.bashrc
