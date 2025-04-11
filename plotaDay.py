#!/usr/bin/env python
# plot_vlp.py
#
# Plots a 24-hour waveform plot of seismic or strain data.
#
# R.C. Stewart, 28-Jan-2022
#
import os
import sys
import glob
import argparse
import re
import obspy
from datetime import datetime, date, timedelta
from dateutil import parser as dparser
from obspy.core import UTCDateTime, Stream


def main():

    # Arguments

    parser = argparse.ArgumentParser(description="Generate 24-hour waveform plot")
    parser.add_argument("--date", default="yesterday", help="Date")
    parser.add_argument("--dir_mseed", default="/mnt/mvohvs3/MVOSeisD6/mseed", help="Directory with miniseed files")
    parser.add_argument("--net", default="MV", help="Network code")
    parser.add_argument("--sta", default="MBLY", help="Station code")
    parser.add_argument("--cha", default="HHZ", help="Channel code")

    args = parser.parse_args()

    datePlot = args.date
    print( 'Plot date:   ' + datePlot )

    dirMseed = args.dir_mseed
    print( 'Mseed directory:   ' + dirMseed )

    codeNet = args.net
    print( 'Network code:   ' + codeNet )

    codeSta = args.sta
    print( 'Station code:   ' + codeSta )

    codeCha = args.cha
    print( 'Channel code:   ' + codeCha )


    # Constants

    secInDay = 60*60*24
    filenameSeparator = "."
    dirnameSeparator = "/"
    today = datetime.utcnow().date()


    # Try and sort out dates

    if datePlot == 'yesterday':
        plotDate = UTCDateTime( today.year, today.month, today.day ) - secInDay
    elif datePlot == 'today':
        plotDate = UTCDateTime( today.year, today.month, today.day )
    else:
        plotDate = dparser.parse( datePlot )
    print( 'Plot date:   ' + plotDate.strftime("%Y-%m-%d") + plotDate.strftime("  (%Y.%j)") )

    yearday = plotDate.strftime( "%Y.%j" )
    year = plotDate.strftime( "%Y" )

    st = []


    globber = "%s/%s/%s/%s.%s.%s*%s.mseed" % (dirMseed, codeNet, codeSta, yearday, codeNet, codeSta, codeCha)
    filesMseed = glob.glob( globber )

    if filesMseed:
        for fileMseed in filesMseed:
            if not st:
                st = obspy.read( fileMseed )
            else:
                st += obspy.read( fileMseed )


    if st:


        for t in range(len(st)):
            tr = st[t].copy()
            tr.detrend("simple")
            tr.filter( "lowpass", freq=0.1 )
            tr.stats.channel="Lowpass filter 0.1Hz"
            tr.decimate(50, strict_length=False, no_filter=True)
            st.append(tr)

        file_plot = "%s.%s.%s.%s.png" % ( plotDate.strftime( "%Y%m%d"), codeNet, codeSta, codeCha )
        plotBeg = UTCDateTime( plotDate )
        plotEnd = plotBeg + secInDay
        st.plot( equal_scale=False, size=(1600,800), outfile=file_plot, linewidth=0.2, starttime=plotBeg, endtime=plotEnd )



if __name__ == "__main__":
    main()


