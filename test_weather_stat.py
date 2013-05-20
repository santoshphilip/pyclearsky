#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""py.test for weather_stat"""
import weather_stats
from StringIO import StringIO

# getlocation
def test_getlocation():
    """py.test for getlocation"""
    data = ((""" Statistics for USA_AZ_Phoenix.722780_TMY2
 Location -- PHOENIX AZ USA  
      # {N 33° 30'} {W 112°  30'} {GMT -7.0 Hours}
""", ("PHOENIX AZ USA", 33.5, -112.5, -7.0)), # stattxt, location
    )
    for stattxt, location in data:
        fhandle = StringIO(stattxt)
        result = weather_stats.getlocation(fhandle)
        assert result == location

def test_longlat():
    """py.test for longlat"""
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # data = (("""N 33\xc2\xb0 25'""", 33.5), # txt, ang
    data = (("""N 33° 30'""", 33.5), # txt, ang
    ("""E 33° 30'""", 33.5), # txt, ang
    ("""S 33° 30'""", -33.5), # txt, ang
    ("""W 33° 30'""", -33.5), # txt, ang
    ("""E 33° """, 33.0), # txt, ang
    )
    for txt, ang in data:
        result = weather_stats.longlat(txt)
        assert result == ang
        
def test_timezone():
    """py.test for timezone"""
    data = (("GMT -7.0 Hours", -7.0), # txt, tz
    )
    for txt, tz in data:
        result = weather_stats.timezone(txt)
        assert result == tz
        
def test_locationdatastrings():
    """py.test locationdatastrings"""
    data = (("      {N 33° 25'} {W 112°  1'} {GMT -7.0 Hours}",
        "N 33° 25'", "W 112°  1'", "GMT -7.0 Hours"), # txt, lat, lng, tz
    )
    for txt, lat, lng, tz in data:
        result = weather_stats.locationdatastrings(txt)
        assert result == (lat, lng, tz)