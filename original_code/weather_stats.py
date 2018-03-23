# Copyright (c) 2013 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

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
    
    