"""calcs for clearsky radiation from Ashrae fundamentals 2009. page 14.9"""

import math



def degcos(theta):
    """return cos(theta) when theta is in degrees"""
    theta = math.radians(theta)
    return math.cos(theta)
    
def degsin(theta):
    """docstring for degsin"""
    theta = math.radians(theta)
    return math.sin(theta)


def ETradiation(daynum=None, thedate=None):
    """extraterrestrial radiation for specific day
    Equation 4.
    E0 = Esc (1 + 0.033 * cos(360 * (n - 3) / 365))"""
    if daynum:
        pass
    else:
        daynum = thedate.timetuple().tm_yday
    Esc = 1367.
    # print Esc
    # print 360. * (daynum - 3) / 365.
    # print math.radians(360. * (daynum - 3) / 365.)
    # print degcos(360. * (daynum - 3) / 365.)
    E0 = Esc * (1 + 0.033 * degcos(360. * (daynum - 3) / 365.))
    # print E0
    return E0
    
def airmass(alt):
    """return the airmass
    Equation 16
    m = 1 / [sin(b) + 0.50572 * power(6.07995 + b, -1.6364)]"""
    b = alt
    m = 1 / (degsin(b) + 0.50572 * math.pow(6.07995 + b, -1.6364))
    return m
    
def tau(fhandle):
    """return tau_b, tau_d for each month of year"""
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
    """return ab in equation 19
    """
    v1 = 1.219
    v2 = 0.043 * taub
    v3 = 0.151 * taud
    v4 = 0.204 * taub * taud
    return v1 - v2 - v3 - v4
        
def getad(taub, taud):
    """return ad in equation 20
    """
    v1 = 0.202
    v2 = 0.852 * taub
    v3 = 0.007 * taud
    v4 = 0.357 * taub * taud
    return v1 - v2 - v3 - v4
        

def directnormal_inner(E0, taub, m, ab):
    """return the direct normal radiation
    equation 17
    Eb = E0 * exp( - taub * power(m, ab) )
    """ 
    # Eb args = E0, taub, m, ab
    # E0 = ETradiation(daynum=None, thedate=None)
    # taub
    # m = airmass(alt)
    # ab = ab(taub, taud)
    Eb = E0 * math.exp(-taub * math.pow(m, ab))
    return Eb
    
def diffhoriz_inner(E0, taud, m, ad):
    """return diffuse horizontal radiation
    equation 18
    Ed = E0 * exp(-taud * power(m, ad))"""
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