"""test ashraesky against weather file
compare outputs against weather data from clear sky days."""

import sys
sys.path.append('/Users/santosh/Documents/coolshadow/sunpath/spapyrex')

import spabase
import calendar
import clearskyrad
from datetime import datetime

# phoenix Arizona
spadict = {}
spadict['year'] = 1975 
spadict['month'] = 2
spadict['day'] = 16
spadict['hour'] = 14
spadict['minute'] = 00
spadict['second'] = 00
spadict['timezone'] = -7.0
spadict['delta_t'] = 67
spadict['longitude'] = -112.066
spadict['latitude'] = 33.43
spadict['elevation'] = 339.14
spadict['pressure'] = 820
spadict['temperature'] = 11
spadict['slope'] = 0
spadict['azm_rotation'] = 0
spadict['atmos_refract'] = 0.5667

statfilename = './weatherfiles/USA_AZ_Phoenix/USA_AZ_Phoenix.722780_TMY2.stat'
taubs, tauds = clearskyrad.tau(open(statfilename))

# for m in range(1, 13):
for m in range(1, 13):
    # for d in range(1, calendar.monthrange(spadict['year'], m)[1]):
    for d in range(1, 25):
        for h in range(1, 25):
            spadict['month'] = m
            spadict['day'] = d
            spadict['hour'] = h
            try:
                sun = spabase.spacalc(spadict)
                alt = 90 - sun['zenith']
                taub, taud = taubs[m -1], tauds[m -1]
                thedate = datetime(spadict['year'], m, d)
                if alt <= 0:
                    Eb = 0
                    Ed = 0
                else:
                    Eb = clearskyrad.directnormal(taub, taud, alt, thedate=thedate)
                    Ed = clearskyrad.diffusehorizontal(taub, taud, alt, thedate=thedate)
                print m, d, h, alt, Eb, Ed
                # print m, d, h, 90 - sun['zenith']
                # print sun
            except spabase.UnknownError:
                raise spabase.DataError
