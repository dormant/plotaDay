#!/usr/bin/bash

#eval "$(conda shell.bash hook)"
source /home/seisan/anaconda3/etc/profile.d/conda.sh
conda activate obspy

cd /home/seisan/src/plotaDay
./plotaDay.py --date today --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date yesterday --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date today --sta AIRS --net MC --cha BLZ
./plotaDay.py --date yesterday --sta AIRS --net MC --cha BLZ
./plotaDay.py --date today --sta TRNT --net MC --cha BLZ
./plotaDay.py --date yesterday --sta TRNT --net MC --cha BLZ
mv *.png /mnt/mvofls2/Seismic_Data/monitoring_data/strain_plots/2025/
