# plotaDay

## ~/src/plotaDay

Scripts for plotting strain and VLP data for *seismic_plot_viewer* from *miniseed* data.


## plotaDay.py, plotaStrain.sh

* Creates day-long plot of CALIPSO strain data.
* sh script sets up proper conda environment.
* Runs once an hour as cron job on *opsproc3*.
* Plot stored on *mvofls2*.

## plotaDayCatchup.pl, plotaStrainCatchUp.sh

* Runs *plotaDay.pl* in a date loop.
* sh script sets up proper conda environment.
* Used to catchup missing data.

## plotaVlp.py, plotaVlp.sh

* Create day-long plot of VLP data derived from broadband seismic data.
* Runs once a day as cron job on opsproc3.
* Plot stored on *mvofls2*.

## plotDays.py

* Create multi-day plot of strain data.
* Plot generated in current directory.

### Usage

*plotDays.py <--date> <--dir_mseed> <--days >*

* --date: start date of plot (default yesterday).
* --dir_mseed: Directory with miniseed data (default */mnt/mvohvs3/MVOSeisD6/mseed*).
* --days: Number of days to plot (default 1).

## plotsomeVlp.py

* Obsolete script to plot one day of VLP data.

## Author

Roderick Stewart, Dormant Services Ltd

rod@dormant.org

https://services.dormant.org/

## Version History

* 1.0-dev
    * Working version

## License

This project is the property of Montserrat Volcano Observatory.
