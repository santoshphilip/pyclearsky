pyclearsky
==========


.. image:: https://img.shields.io/pypi/v/pyclearsky.svg
        :target: https://pypi.python.org/pypi/pyclearsky

.. image:: https://img.shields.io/travis/santoshphilip/pyclearsky.svg
        :target: https://travis-ci.org/santoshphilip/pyclearsky

.. image:: https://readthedocs.org/projects/pyclearsky/badge/?version=latest
        :target: https://pyclearsky.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




implements the equations from Ashrae Fundamentals 2009 for clear sky in Python


* Free software: Mozilla Public License Version 2.0
* Documentation: https://pyclearsky.readthedocs.io.


Features
--------

Implements the following equation of ASHRAE Fundamentals 2009, chapter 14

- Equation (4) from page 14.7
- Equation (16) from page 14.9
- Equation (17) from page 14.9
- Equation (18) from page 14.9
- Equation (19) from page 14.9
- Equation (20) from page 14.9

Purpose of pyclearsky
---------------------

**What does pyclearsky do ?**

- pyclearsky calculates the radiation from a clear sky.
- The weather files do not always have this data, since they include cloud cover

**Why would you want to calculate the radiation from a clear sky ?**

- Cloud cover in the weather files do not always reflect reality.
- Sometimes you want to simulate an exteme condtion and you want to assume there is no cloud cover
- This may needed when you estimate the reflected sunlight from a water body or an adjacent building
- You are likely to want to calculate this without cloud cover
- pyclearsky will let you do that

**How does pyclearsky do this calculation ?**

- Chapter 14 in ASHRAE Fundamentals 2009 describes the equations that calculate the radiations from a clear sky
- the `latest weather files`_ come with three file types. They are `*.epw`, `*.ddy` and `*.stat`
- The raw data needed to do this calculation is in the weather file. Specifically in the `*.stat` file

**A demonstration of pycleasky**

Let us use the Phoenix AZ weather file as a way of exploring pyclearsky. And let us look into the `*.stat` file. The `*.stat` file has the following lines (at around line 37)::

     - Monthly Solar Irradiance Wh/m² (noon on 21st of month)
     	               ib (beam)	  915	  937	  938	  920	  870	  827	  727	  750	  807	  833	  891	  907
     	            id (diffuse)	   89	  102	  121	  141	  170	  194	  250	  220	  171	  140	   92	   81

     	                      ib	= Clear Sky Noon Beam Normal Irradiance on 21st Day
     	                      id	= Clear Sky Noon Diffuse Horizontal Irradiance on 21st Day

This is the clear sky radiation on the 21st of every month. Let us try to use pyclearsky to calculate the same results::

    from io import open # to work with python2 and python3
    from pyclearsky import clearskyrad
    fname = "./original_code/weatherfiles/USA_AZ_Phoenix/USA_AZ_Phoenix.722780_TMY2.stat"
    fhandle = open(fname, 'r', encoding='latin1')
    tau = clearskyrad.tau(fhandle)
    taub, taud = tau

    print taub
    [0.306,
     0.317,
     0.339,
     0.366,
     0.419,
     0.465,
     0.588,
     0.547,
     0.456,
     0.393,
     0.318,
     0.298]

    print taud
    [0.306,
     0.317,
     0.339,
     0.366,
     0.419,
     0.465,
     0.588,
     0.547,
     0.456,
     0.393,
     0.318,
     0.298]

clearskyrad.tau(fhandle) reads the *taub* and *taud* values from the `*.stat` file (around line 28)::

     - Displaying Monthly Design Conditions "Climate Design Data 2009 ASHRAE Handbook"
     - Monthly Optical Sky Depth Beam (taub) and Diffuse (taud)
     	                        	Jan	Feb	Mar	Apr	May	Jun	Jul	Aug	Sep	Oct	Nov	Dec
     	             taub (beam)	0.306	0.317	0.339	0.366	0.419	0.465	0.588	0.547	0.456	0.393	0.318	0.298
     	          taud (diffuse)	2.534	2.463	2.351	2.229	2.044	 1.91	1.653	1.763	1.978	2.116	2.487	2.592

     	                    taub	= Clear Sky Optical Depth for Beam Irradiance
     	                    taud	= Clear Sky Optical Depth for Diffuse Irradiance


To calculate the radiation, we need the altitude of the sun. Let us find the altitude of the sun at noon on the 21st of each month. We can do this by going to the web site  https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html ::

    alts = {1:35.97,
    2:45.09,
    3:55.99,
    4:67.74,
    5:75.74,
    6:78.02,
    7:74.83,
    8:67.34,
    9:56.7,
    10:45.59,
    11:36.46,
    12:32.8}
    # month:altitude
    # calculated from https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html

Now we are ready to calculate the clear sky radiation. Starting with direct normal ::

    from datetime import datetime

    for month in range(1, 13):
        print clearskyrad.directnormal(taub[month-1], taud[month-1],
            alts[month], thedate=datetime(2018, month, 21))

the direct normal results are ::

    912.281856828
    936.707585623
    937.22435687
    920.279543442
    869.489603714
    824.956794153
    723.86104248
    748.144302441
    808.247171807
    837.874397967
    893.090953721
    904.04138393


And for diffuse horizontal ::

    for month in range(1, 13):
        print clearskyrad.diffusehorizontal(taub[month-1], taud[month-1],
            alts[month], thedate=datetime(2018, month, 21))

The diffuse horizontal results are ::


    88.3239665087
    102.034946163
    120.595369428
    140.632493558
    170.230386996
    193.761516975
    248.413566492
    219.237360391
    171.24339381
    140.903362551
    92.1795686764
    80.6806617141

Close enough to the values in the `*.stat` file ::

     - Monthly Solar Irradiance Wh/m² (noon on 21st of month)
     	               ib (beam)	  915	  937	  938	  920	  870	  827	  727	  750	  807	  833	  891	  907
     	            id (diffuse)	   89	  102	  121	  141	  170	  194	  250	  220	  171	  140	   92	   81

     	                      ib	= Clear Sky Noon Beam Normal Irradiance on 21st Day
     	                      id	= Clear Sky Noon Diffuse Horizontal Irradiance on 21st Day


If you ever need to calculate the clears sky radiation, that is how you do it.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`latest weather files`: https://energyplus.net/weather
