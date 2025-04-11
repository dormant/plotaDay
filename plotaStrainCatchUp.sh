#!/usr/bin/bash

#eval "$(conda shell.bash hook)"
source /home/seisan/anaconda3/etc/profile.d/conda.sh
conda activate obspy

cd /home/seisan/src/plotaDay
./plotaDay.py --date 2024-12-07 --sta AIRS --net MC --cha BLZ
./plotaDay.py --date 2024-12-07 --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date 2024-12-07 --sta TRNT --net MC --cha BLZ
./plotaDay.py --date 2024-12-06 --sta AIRS --net MC --cha BLZ
./plotaDay.py --date 2024-12-06 --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date 2024-12-06 --sta TRNT --net MC --cha BLZ
./plotaDay.py --date 2024-12-05 --sta AIRS --net MC --cha BLZ
./plotaDay.py --date 2024-12-05 --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date 2024-12-05 --sta TRNT --net MC --cha BLZ
./plotaDay.py --date 2024-12-04 --sta AIRS --net MC --cha BLZ
./plotaDay.py --date 2024-12-04 --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date 2024-12-04 --sta TRNT --net MC --cha BLZ
./plotaDay.py --date 2024-12-03 --sta AIRS --net MC --cha BLZ
./plotaDay.py --date 2024-12-03 --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date 2024-12-03 --sta TRNT --net MC --cha BLZ
./plotaDay.py --date 2024-12-02 --sta AIRS --net MC --cha BLZ
./plotaDay.py --date 2024-12-02 --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date 2024-12-02 --sta TRNT --net MC --cha BLZ
./plotaDay.py --date 2024-12-01 --sta AIRS --net MC --cha BLZ
./plotaDay.py --date 2024-12-01 --sta OLV1 --net MC --cha BLZ
./plotaDay.py --date 2024-12-01 --sta TRNT --net MC --cha BLZ
mv *.png /mnt/mvofls2/Seismic_Data/monitoring_data/strain_plots/2024/
