#!/usr/bin/bash

#eval "$(conda shell.bash hook)"
source /home/seisan/anaconda3/etc/profile.d/conda.sh
conda activate obspy

cd /home/seisan/Dropbox/STUFF/src/plotaDay
./plotaVlp.py
