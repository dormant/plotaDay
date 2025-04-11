#!/usr/bin/bash
#

d=2022-09-22
while [ "$d" != 2023-06-20 ]; do
  echo $d
  ./plotaDay.py --date $d --sta AIRS --net MC --cha BLZ
  ./plotaDay.py --date $d --sta OLV1 --net MC --cha BLZ

  d=$(date -I -d "$d + 1 day")
done
