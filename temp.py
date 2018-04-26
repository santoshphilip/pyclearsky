from pyclearsky import clearskyrad
fname = "./original_code/weatherfiles/USA_AZ_Phoenix/USA_AZ_Phoenix.722780_TMY2.stat"
fhandle = open(fname, 'r')
tau = clearskyrad.tau(fhandle)

tau = (
[0.306, 0.317, 0.339, 0.366, 0.419, 0.465, 0.588, 0.547, 0.456, 0.393, 0.318, 0.298], 
[2.534, 2.463, 2.351, 2.229, 2.044, 1.91, 1.653, 1.763, 1.978, 2.116, 2.487, 2.592])

taub = [0.306, 0.317, 0.339, 0.366, 0.419, 0.465, 0.588, 0.547, 0.456, 0.393, 0.318, 0.298]
taud = [2.534, 2.463, 2.351, 2.229, 2.044, 1.91, 1.653, 1.763, 1.978, 2.116, 2.487, 2.592]

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


directnormal(taub, taud, alt, daynum=None, thedate=None)[source]
from datetime import datetime
clearskyrad.directnormal(0.306, 2.534, 35.97, thedate=datetime(2018, 1, 21))

for month in range(1, 13):
    print clearskyrad.directnormal(0.306, 2.534, 
        alts[month], thedate=datetime(2018, month, 21))
912.281856828
950.942463339
974.4352538
981.296535599
976.475063103
969.999437456
967.738951618
967.637367419
961.559843158
941.573622317
909.076142793
891.352884087

for month in range(1, 13):
    print clearskyrad.diffusehorizontal(0.306, 2.534, 
        alts[month], thedate=datetime(2018, month, 21))
88.3239665087
95.3195918214
100.83177663
103.952635891
104.490819595
104.01032188
103.460998131
102.441506612
99.6712881382
94.5397103815
88.1948025288
85.1142770506

from stat file:
 - Monthly Solar Irradiance Wh/m² (noon on 21st of month)
 	               ib (beam)	  915	  937	  938	  920	  870	  827	  727	  750	  807	  833	  891	  907	
 	            id (diffuse)	   89	  102	  121	  141	  170	  194	  250	  220	  171	  140	   92	   81	

 	                      ib	= Clear Sky Noon Beam Normal Irradiance on 21st Day
 	                      id	= Clear Sky Noon Diffuse Horizontal Irradiance on 21st Day
