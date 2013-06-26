#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Santosh Philip

# This file is part of pyclearsky.

# pyclearsky is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pyclearsky is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pyclearsky.  If not, see <http://www.gnu.org/licenses/>.

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