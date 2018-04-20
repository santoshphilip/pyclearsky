# Copyright (c) 2013, 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""calcs for clearsky radiation from Ashrae fundamentals 2009. page 14.9"""

import math


def func(arg1, arg2):
    """Summary line of func.

    Extended description of function. This is a Sample
    Function to show how the function documentation should be done.
    This is the numpy style documentation,
    will be formatted beautifully by sphinx-napoleon extension

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    """
    return True


def degcos(theta):
    """return cos(theta) where theta is in degrees

    Parameters
    ----------
    theta : float
        angle in degrees

    Returns
    -------
    float
        cosine value of the angle theta (theta is in degrees)

    """
    theta = math.radians(theta)
    return math.cos(theta)


def degsin(theta):
    """return sin(theta) where theta is in degrees

    Parameters
    ----------
    theta : float
        angle in degrees

    Returns
    -------
    float
        sine value of the angle theta (theta is in degrees)

    """
    theta = math.radians(theta)
    return math.sin(theta)


def ETradiation(daynum=None, thedate=None):
    """Calculates Extraterrestial Radiation for a specific day

    This is equation (4) from
    ASHRAE Fundamentals 2009, page 14.7.

    The equation is:

    - E0 = Esc (1 + 0.033 * cos(360 * (n - 3) / 365))
        - where n = daynum

    ETradiation takes *daynum* OR *thedate* as an input
        - daynum is the day of the year
            - (1 for January 1, 32 for February 1, etc)
        - thedate is a datetime.datetime object
            - ETradiation will calculate the daynum from the date


    Parameters
    ----------
    daynum : int
        daynum is the day of the year
    thedate : datetime.datetime()
        daynum is calulated ffrom the datetime object

    Returns
    -------
    float
        Extraterrestial Radiation for a specific day

"""
    if daynum:
        pass
    else:
        daynum = thedate.timetuple().tm_yday
    Esc = 1367.
    E0 = Esc * (1 + 0.033 * degcos(360. * (daynum - 3) / 365.))
    return E0


def airmass(alt):
    """Calculates the airmass

    This is equation (16) from
    ASHRAE Fundamentals 2009, page 14.9.

    The equation is:

    -  m = 1 / [sin(b) + 0.50572 * power(6.07995 + b, -1.6364)]
        - where b = solar altitude


    Parameters
    ----------
    alt : float
        solar altitude

    Returns
    -------
    float
        Air Mass

"""
    b = alt
    m = 1 / (degsin(b) + 0.50572 * math.pow(6.07995 + b, -1.6364))
    return m


def tau(fhandle):
    """return tau_b and tau_d for each month of the year

    These values are in the weather file with extension .stat

    Parameters
    ----------
    fhandle : filehandle
        fhandle is a file open for reading

    Returns
    -------
    taub : list
    taud : list
        return two lists with values of taub and taud

"""
    for line in fhandle:
        line = line.strip()
        if line.startswith("taub"):
            words = line.split()
            taub = words[-12:]
            taub = [float(word) for word in taub]
            break
    for line in fhandle:
        line = line.strip()
        if line.startswith("taud"):
            words = line.split()
            taud = words[-12:]
            taud = [float(word) for word in taud]
            break
    return taub, taud


def getab(taub, taud):
    """calculates value of ab in equation (19)

    Equation (19) in ASHRAE Fundamentals 2009 pg 14.9

    Parameters
    ----------
    taub : float
        value of taub in equation (19)
    taud : float
        value of taud in equation (19)

    Returns
    -------
    float
        the value of ab

    """
    v1 = 1.219
    v2 = 0.043 * taub
    v3 = 0.151 * taud
    v4 = 0.204 * taub * taud
    return v1 - v2 - v3 - v4


def getad(taub, taud):
    """calculates value of ad in equation (20)

    Equation (20) in ASHRAE Fundamentals 2009 pg 14.9

    Parameters
    ----------
    taub : float
        value of taub in equation (20)
    taud : float
        value of taud in equation (20)

    Returns
    -------
    float
        the value of ad

    """
    # """return ad in equation 20
    # """
    v1 = 0.202
    v2 = 0.852 * taub
    v3 = 0.007 * taud
    v4 = 0.357 * taub * taud
    # print v1, v2, v3, v4
    # return v1 - v2 - v3 - v4 # typo in the equation. Example is correct.
    return v1 + v2 - v3 - v4


def directnormal_inner(E0, taub, m, ab):
    """Calculates value of Eb in equation (17)

    Equation (17) in ASHRAE Fundamentals 2009 page 14.9

    The equation is
        - Eb = E0 * exp( - taub * power(m, ab) )

    Parameters
    ----------
    E0 : float
        Extraterrestrial normal irradiance [Equation (4)]
    taub : float
        beam optical depth
    m : float
        Air Mass Equation (16)
    ab : float
        beam air mass exponents

    Returns
    -------
    float
        Beam normal irradiance

    """
    # """return the direct normal radiation
    # equation 17
    # Eb = E0 * exp( - taub * power(m, ab) )
    # """
    Eb = E0 * math.exp(-taub * math.pow(m, ab))
    return Eb


def diffhoriz_inner(E0, taud, m, ad):
    """Calculates value of Ed in equation (18)

    Equation (18) in ASHRAE Fundamentals 2009 page 14.9

    The equation is
        - Ed = E0 * exp(-taud * power(m, ad))

    Parameters
    ----------
    E0 : float
        Extraterrestrial normal irradiance [Equation (4)]
    taud : float
        diffuse optical depth
    m : float
        Air Mass Equation (16)
    ad : float
        diffuse air mass exponents

    Returns
    -------
    float
        Diffuse horizontal irradiance

    """
    # """return diffuse horizontal radiation
    # equation 18
    # Ed = E0 * exp(-taud * power(m, ad))"""
    # print math.exp(-taud * math.pow(m, ad))
    Ed = E0 * math.exp(-taud * math.pow(m, ad))
    return Ed


def directnormal(taub, taud, alt, daynum=None, thedate=None):
    """return direct normal radiation
    see directnormal_inner for details"""
    E0 = ETradiation(daynum=daynum, thedate=thedate)
    m = airmass(alt)
    ab = getab(taub, taud)
    Eb = directnormal_inner(E0, taub, m, ab)
    return Eb


def diffusehorizontal(taub, taud, alt, daynum=None, thedate=None):
    """return the diffuce horizontal radiation
    see diffhoriz_inner for details"""
    E0 = ETradiation(daynum=daynum, thedate=thedate)
    m = airmass(alt)
    ad = getad(taub, taud)
    # print E0, taud, m, ad
    Ed = diffhoriz_inner(E0, taud, m, ad)
    return Ed
