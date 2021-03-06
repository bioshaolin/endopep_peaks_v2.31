#######################
#                     #
# ENDOPEP_PEAKS_v2.31 #
#                     #
#######################

    *********************
### Download and set path ############################################

git clone https://github.com/bioshaolin/endopep_peaks_v2.31.git

External:\
. endopep_peaks_v2.31/endopep_peaks/scripts/init_bash_dir/set_path.sh\
CDC:\
. endopep_peaks_v2.31/endopep_peaks/scripts/init_bash_dir/set_path_cdc.sh\
source .bashrc\
init_cdc

#########################################################

#########################################################

    *********************
### vid tutorial download ###

endopep_peaks -vids

    ******
### Summary ###

Endopep_peaks is a dataframing application that aims to generate user friendly outputs for interpreting results of
BoNT endopeptide mass spectrometry. The standard Bruker corporation flex analysis software allows for the exporting of
multi-sheet excel files, however given the procedural specificity of peptide mass spectrometry in contrast to
organism identification, this data form becomes disadvantageous. Endopep_peaks enables the production of option-based outputs
to meet the needs of differing interpretation methods.

    ***************
### Future versions ###

Currently this application is developed to only asses BoNT mass spec bruker data. Future versions may include an option
allowing the user to specify a threshold series of m/z by mode of command input or secondary input file.
(The threshold series maximum would remain 4 but could be manipulated to include greater peak variations similar to
extracellular metabolite combinations)

    *****
### USAGE ###

usage: endopep_peaks [-h] [-read] [-dep] [-init INIT] [-vid_mods]
                     [-tutorial TUTORIAL] [-type TYPE] [-n] [-b] [-c] [-clear]
                     [-visual]

################################
## generate human readable mass spec data from a standard Bruker output ##
 m/z = (mass)/(charged # of ions)\
 sn = signal to noise value\

## help arguments:
  -h, --help            show this help message and exit\
  -read, --read         Show Read.me\
  -dep, --dependencies  List the program dependencies for endopep_peaks\
  -init INIT            [initialize:HPC] or install dependencies\
                        (cdc/external) only if prev. run in 24hr

## tutorials:
  -vids, --modules  Download tutorial modules (required for tutorial)\
  -tutorial TUTORIAL    Prompt tutorial modules\
                        (all/intro/run/type/output/vis)

## required arguments:
  -type TYPE            Specify which serotypes are being assesed\
                        (all/a/b/e/f)

## output arguments:
  -n, --noise           Generate a separate noise output (NO sn)\
  -b, --boolean         Generate a boolean value output (NO sn) (NO m/z)\
  -c, --clia            Generate a standard output (m/z)(sn)\

## optional arguments:
  -clear, --clear_all   Clear previous outputs from current input directory\
  -visual, --visual     Generate a visual to compare against reference data\
                        (Yes:-c | NO:-b,-n)

################################\
Development: E.W. Getz, 2020\
Version: v2.31\
Source: https://github.com/bioshaolin/endopep_peaks_v2.31 \
CDC/ DDID/ NCEZID/ DFWED/ EDLB/\

    ************
### Dependencies ###

BASH:\
GNU bash v5.0.3 or later\
gnumeric v1.12.45\
ffmpeg v4.1.1-1build2\

PYTHON:\
Python 3.6.8\
numpy 1.16.2\
pandas 0.24.2\
argparse 1.1\
markdown-textwrap-0.2.1\
matplotlib 3.0.3\
jinja2 (included with most >= Python 3)\
gdown (preset in use of -vid_mods)\

