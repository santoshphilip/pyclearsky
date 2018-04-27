from pyclearsky import clearskyrad
fname = "./original_code/weatherfiles/USA_AZ_Phoenix/USA_AZ_Phoenix.722780_TMY2.stat"
fhandle = open(fname, 'r')
tau = clearskyrad.tau(fhandle)

tau = (
[0.306, 0.317, 0.339, 0.366, 0.419, 0.465, 0.588, 0.547, 0.456, 0.393, 0.318, 0.298],
[2.534, 2.463, 2.351, 2.229, 2.044, 1.91, 1.653, 1.763, 1.978, 2.116, 2.487, 2.592])

taub, taud = tau

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
# from https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html


from datetime import datetime
clearskyrad.directnormal(0.306, 2.534, 35.97, thedate=datetime(2018, 1, 21))

for month in range(1, 13):
    print clearskyrad.directnormal(taub[month-1], taud[month-1],
        alts[month], thedate=datetime(2018, month, 21))
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

for month in range(1, 13):
    print clearskyrad.diffusehorizontal(taub[month-1], taud[month-1],
        alts[month], thedate=datetime(2018, month, 21))
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

from stat file:
 - Monthly Solar Irradiance Wh/m² (noon on 21st of month)
 	               ib (beam)	  915	  937	  938	  920	  870	  827	  727	  750	  807	  833	  891	  907
 	            id (diffuse)	   89	  102	  121	  141	  170	  194	  250	  220	  171	  140	   92	   81

 	                      ib	= Clear Sky Noon Beam Normal Irradiance on 21st Day
 	                      id	= Clear Sky Noon Diffuse Horizontal Irradiance on 21st Day





alts_s = {1:35.7,
2:44.3,
3:55.1,
4:67.2,
5:75.5,
6:78.1,
7:75.1,
8:67.6,
9:56.6,
10:45.3,
11:36.4,
12:32.8,}
# from Stephen

for month in range(1, 13):
    print clearskyrad.directnormal(taub[month-1], taud[month-1],
        alts_s[month], thedate=datetime(2018, month, 21))
910.564755737
933.191565419
934.580166545
919.307428925
869.203078094
825.040526974
724.272569755
748.741260105
807.903016258
836.392010126
892.711740092
904.04138393

for month in range(1, 13):
    print clearskyrad.diffusehorizontal(taub[month-1], taud[month-1],
        alts_s[month], thedate=datetime(2018, month, 21))
88.0570734495
101.383099948
120.003211847
140.375385554
170.140644242
193.790876698
248.594402121
219.469253713
171.139950675
140.544012026
92.1182534007
80.6806617141

from stat file:
 - Monthly Solar Irradiance Wh/m² (noon on 21st of month)
 	               ib (beam)	  915	  937	  938	  920	  870	  827	  727	  750	  807	  833	  891	  907
 	            id (diffuse)	   89	  102	  121	  141	  170	  194	  250	  220	  171	  140	   92	   81

 	                      ib	= Clear Sky Noon Beam Normal Irradiance on 21st Day
 	                      id	= Clear Sky Noon Diffuse Horizontal Irradiance on 21st Day
