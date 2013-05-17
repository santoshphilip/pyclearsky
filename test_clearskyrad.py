"""py.test for clearskyrad.py"""
import clearskyrad
from pytest_helpers import almostequal

def test_degcos():
    """py.test for degcos"""
    data = ((60, 0.5), # deg, thecos
    )
    for deg, thecos in data:
        result = clearskyrad.degcos(deg)
        assert almostequal(result, thecos) == True
    
def test_degsin():
    """py.test for degcos"""
    data = ((30, 0.5), # deg, thesin
    )
    for deg, thesin in data:
        result = clearskyrad.degsin(deg)
        assert almostequal(result, thesin) == True
    
    
def test_ETradiation():
    """py.test for ETradiation"""
    data = ((21, 1410), # daynum, radiation
    (52, 1397), # daynum, radiation
    (80, 1378), # daynum, radiation
    (111, 1354), # daynum, radiation
    (141, 1334), # daynum, radiation
    (172, 1323), # daynum, radiation
    (202, 1324), # daynum, radiation
    (233, 1336), # daynum, radiation
    (264, 1357), # daynum, radiation
    (294, 1380), # daynum, radiation
    (325, 1400), # daynum, radiation
    (355, 1411), # daynum, radiation
    )
    for daynum, radiation in data:
        result = clearskyrad.ETradiation(daynum=daynum)
        assert almostequal(result, radiation, places=0) == True
    from datetime import datetime as dt
    data = ((dt(2013, 1, 21), 1410), # thedate, radiation
    (dt(2013, 2, 21), 1397), # thedate, radiation
    (dt(2013, 3, 21), 1378), # thedate, radiation
    (dt(2013, 4, 21), 1354), # thedate, radiations
    (dt(2013, 5, 21), 1334), # thedate, radiation
    (dt(2013, 6, 21), 1323), # thedate, radiation
    (dt(2013, 7, 21), 1324), # thedate, radiation
    (dt(2013, 8, 21), 1336), # thedate, radiation
    (dt(2013, 9, 21), 1357), # thedate, radiation
    (dt(2013, 10, 21), 1380), # thedate, radiation
    (dt(2013, 11, 21), 1400), # thedate, radiation
    (dt(2013, 12, 21), 1411), # thedate, radiation
    )
    for thedate, radiation in data:
        result = clearskyrad.ETradiation(thedate=thedate)
        # print result, radiation
        assert almostequal(result, radiation, places=0) == True

def test_airmass():
    """py.test for airmass"""
    data = ((30, 1.9942928525), # alt, theairmass
    (45, 1.412595252), # alt, theairmass
    (60, 1.1539922334), # alt, theairmass
    (90, 0.9997119919), # alt, theairmass
    )
    for alt, theairmass in data:
        result = clearskyrad.airmass(alt)
        assert almostequal(result, theairmass)

def test_tau():
    """py.test for tau"""
    data = ((""" - Displaying Monthly Design Conditions "Climate Design Data 2009 ASHRAE Handbook"
 - Monthly Optical Sky Depth Beam (taub) and Diffuse (taud)
 	                        	Jan	Feb	Mar	Apr	May	Jun	Jul	Aug	Sep	Oct	Nov	Dec	
 	             taub (beam)	0.289	 0.29	0.325	0.351	0.377	 0.37	0.362	0.352	0.343	0.323	0.302	0.289	
 	          taud (diffuse)	2.641	2.681	2.392	2.292	2.224	2.361	2.489	2.561	2.539	2.534	2.618	2.633	

 	                    taub	= Clear Sky Optical Depth for Beam Irradiance
 	                    taud	= Clear Sky Optical Depth for Diffuse Irradiance

""",
[0.289, 0.29, 0.325, 0.351, 0.377, 0.37, 
0.362, 0.352, 0.343, 0.323, 0.302, 0.289],
[2.641, 2.681, 2.392, 2.292, 2.224, 2.361, 
2.489, 2.561, 2.539, 2.534, 2.618, 2.633]), # txt, taub, taud
    )  
    for txt, taub, taud in data:
        import StringIO
        fhandle = StringIO.StringIO(txt)
        result = clearskyrad.tau(fhandle)
        assert result == (taub, taud)
        
def test_getab():
    """py.test for getab"""
    data = ((0.289, 2.641, 0.652079204), # taub, taud, theab
    )        
    for taub, taud, theab in data:
        result = clearskyrad.getab(taub, taud)
        assert almostequal(result, theab)
        
def test_getad():
    """py.test for getad"""
    data = ((0.289, 2.641, -0.335194893), # taub, taud, thead
)        
    for taub, taud, thead in data:
        result = clearskyrad.getad(taub, taud)
        assert almostequal(result, thead)
        
def test_directnormal_inner():
    """py.test for directnormal_inner"""
    data = ((1409.962705, 0.289, 0.999711992, 
    0.652079204, 1056.136599), # E0, taub,  m, ab, Eb
    )
    for E0, taub,  m, ab, Eb in data:
        result = clearskyrad.directnormal_inner(E0, taub, m, ab)
        assert almostequal(result, Eb, places=6)

def test_diffhoriz_inner():
    """py.test for diffhoriz_inner"""
    data = ((1409.962705, 2.641, 0.999711992, 
    -0.335194893, 100.490533,), # E0, taud, m, ad, Ed
    )
    for E0, taud, m, ad, Ed in data:
        result = clearskyrad.diffhoriz_inner(E0, taud, m, ad)
        assert almostequal(result, Ed,  places=6)

def test_directnormal():
    """py.test for directnormal"""
    data = ((0.289, 2.641, 90, 21, 1056.136599), # taub, taud, alt, daynum, Eb
    )
    for taub, taud, alt, daynum, Eb in data:
        result = clearskyrad.directnormal(taub, taud, alt, daynum)
        assert almostequal(result, Eb, places=5)

def test_diffusehorizontal():
    """py.test for diffusehorizontal"""
    data = ((0.289, 2.641, 90, 21, 100.490533), # taub, taud, alt, daynum, Eb
    )
    for taub, taud, alt, daynum, Eb in data:
        result = clearskyrad.diffusehorizontal(taub, taud, alt, daynum=daynum)
        assert almostequal(result, Eb)
