#!/usr/bin/env python
# plot_vlp.py
#
# Plots a 24-hour waveform plot of integrated broad-band data.
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

    parser = argparse.ArgumentParser(description="Generate 24-hour integrated waveform plot")
    parser.add_argument("--date", default="yesterday", help="Date")
    parser.add_argument("--dir_mseed", default="/mnt/mvohvs3/MVOSeisD6/mseed/MV/", help="Directory with miniseed files")

    args = parser.parse_args()

    datePlot = args.date
    print( 'Plot date:   ' + datePlot )

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
    #print( 'Plot date:   ' + plotDate.strftime("%Y-%m-%d") + plotDate.strftime("  (%Y.%j)") )

    yearday = plotDate.strftime( "%Y.%j" )
    year = plotDate.strftime( "%Y" )

    stationsV = ["MBFR", "MBLY", "MBLG", "MBGH", "MBFL", "MBWH"]

    st = []

    for sta in stationsV:

        globber = "%s%s/%s.MV.%s*[BH]HZ.mseed" % (dirMseed, sta, yearday, sta)
        filesMseed = glob.glob( globber )

        if filesMseed:
            for fileMseed in filesMseed:
                if not st:
                    st = obspy.read( fileMseed )
                else:
                    st += obspy.read( fileMseed )


    if st:

        st.detrend("simple")

        for t in range(len(st)):
            tr = st[t].copy()
            tr.filter( "bandpass", freqmax=0.1, freqmin=0.003 )
            tr.decimate( 200, no_filter=True )
            tr.integrate
            tr.stats.channel="VLP"
            st.append(tr)

        file_plot = "/mnt/mvofls2/Seismic_Data/monitoring_data/vlp_plots/%s/VLP.V.%s.png" % ( year, plotDate.strftime( "%Y%m%d") )
        st.plot( equal_scale=False, size=(1600,800), outfile=file_plot )


    stations3C = ["MBLY", "MBLG", "MBFL"]

    st = []

    for sta in stations3C:

        globber = "%s%s/%s.MV.%s*[BH]H*.mseed" % (dirMseed, sta, yearday, sta)
        filesMseed = glob.glob( globber )

        if filesMseed:
            for fileMseed in filesMseed:
                if not st:
                    st = obspy.read( fileMseed )
                else:
                    st += obspy.read( fileMseed )


    if st:

        st.detrend("simple")
        st.filter( "bandpass", freqmax=0.1, freqmin=0.003 )
        st.decimate( 200, no_filter=True )
        st.integrate
        file_plot = "/mnt/mvofls2/Seismic_Data/monitoring_data/vlp_plots/%s/VLP.3C.%s.png" % ( year, plotDate.strftime( "%Y%m%d") )
        st.plot( equal_scale=True, size=(1600,800), outfile=file_plot )


if __name__ == "__main__":
    main()


