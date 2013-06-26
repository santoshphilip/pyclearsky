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

"""get data from weather.stat file"""

def getlocation(fhandle):
    """get the location from the weather stat file"""
    for line in fhandle:
        line = line.strip()
        if line.startswith('Location'):
            location = line.split('--')[-1]
            location = location.strip()
            break
    line = fhandle.next()
    lat, lng, tz = locationdatastrings(line)
    lat = longlat(lat)
    lng = longlat(lng)
    tz = timezone(tz)
    return location, lat, lng, tz
    
            
def longlat(txt):
    """convert N 33° 30' into +33.5
    W 33° 30' into -33.5
    expects the format to be exactly N 33° 30' """
    txt = txt.strip()
    words = txt.split()
    deg = words[1].split('°')[0]
    deg = float(deg)
    try:
        minutes = words[2].split("'")[0]
        minutes = float(minutes)/60.
    except IndexError, e:
        minutes = 0
    angle = deg + minutes
    cardinal = words[0].strip()
    if cardinal == 'S' or cardinal == 'W':
        angle = angle * -1.
    return angle
    
def timezone(txt):
    """from GMT -7.0 Hours return -7.0"""
    txt = txt.strip()
    words = txt.split()
    return float(words[1])
    
def locationdatastrings(txt):
    """return the location data string snippets: lat, lonlngg, tz"""
    txt = txt.strip()
    words = txt.split('}')
    lat = words[0]
    lat = lat.split('{')[-1]
    lng = words[1]
    lng = lng.split('{')[-1]
    tz = words[2]
    tz = tz.split('{')[-1]
    return lat, lng, tz
    
    