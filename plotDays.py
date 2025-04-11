#!/usr/bin/env python
# plotDays.py
#
# Plots a multi-day waveform plot of strain data.
#
# R.C. Stewart, 7-Apr-2023
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

    parser = argparse.ArgumentParser(description="Generate multi-day waveform plot")
    parser.add_argument("--date", default="yesterday", help="Date")
    parser.add_argument("--dir_mseed", default="/mnt/mvohvs3/MVOSeisD6/mseed", help="Directory with miniseed files")
    parser.add_argument("--days", type=int, default=1, help="number of days" )

    args = parser.parse_args()

    datePlot = args.date
    print( 'Plot date:   ' + datePlot )

    daysPlot = args.days
    print( 'Plot days:   ' + str( daysPlot ) )

    dirMseed = args.dir_mseed
    print( 'Mseed directory:   ' + dirMseed )


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

    st = []
    st2 = []


    codeNet = 'MC'
    codeCha = 'BLZ';

    for iday in range( daysPlot ):

        dataDate = plotDate + timedelta(days=iday)
        yearday = dataDate.strftime( "%Y.%j" )
        year = dataDate.strftime( "%Y" )

        codeSta = 'AIRS'
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
                tr.decimate(50, strict_length=False, no_filter=True)
                st2.append(tr)

        codeSta = 'OLV1'
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
                tr.decimate(50, strict_length=False, no_filter=True)
                st2.append(tr)


        file_plot = "%s--MC.AIRS..BLZ-MC.OLV1..BLZ.png" % ( plotDate.strftime( "%Y%m%d") )
        plotBeg = UTCDateTime( plotDate )
        plotEnd = plotBeg + daysPlot*secInDay
        st.plot( equal_scale=False, size=(1600,800), outfile=file_plot, linewidth=0.2, starttime=plotBeg, endtime=plotEnd )



if __name__ == "__main__":
    main()


