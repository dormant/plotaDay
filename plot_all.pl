#!/usr/bin/perl
#

use DateTime;   

my $start = DateTime->new(
    year       => 2018,
    month      => 4,
    day        => 1,
    hour       => 0,
    minute     => 0,
    second     => 0,
    nanosecond => 0,
    time_zone  => 'UTC',
);
my $stop = DateTime->new(
    year       => 2018,
    month      => 9,
    day        => 1,
    hour       => 0,
    minute     => 0,
    second     => 0,
    nanosecond => 0,
    time_zone  => 'UTC',
);

while ($start <= $stop) {
    #$cmd = join( ' ', './plotaDay.py --date', $start->ymd, ' --net MC --sta OLV1 --cha BLZ' );
    #print $cmd, "\n";
    #system( $cmd );
    #$cmd = join( ' ', './plotaDay.py --date', $start->ymd, ' --net MC --sta TRNT --cha BLZ' );
    #print $cmd, "\n";
    #system( $cmd );
    $cmd = join( ' ', './plotaDay.py --date', $start->ymd, ' --net MC --sta AIRS --cha BLZ' );
    print $cmd, "\n";
    system( $cmd );
    $start->add(days => 1);
}

