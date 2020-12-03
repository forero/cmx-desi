import numpy as np
import glob
import matplotlib.pyplot as plt
import fitsio
from astropy.table import Table

files = glob.glob("tiles_cmx_20201203/08*/fiberassign-*.fits.gz")
tileid = []
tilera = []
tiledec = []
for f in files:
    h = fitsio.read_header(f)
    tileid.append(h['TILEID'])
    tilera.append(h['TILERA'])
    tiledec.append(h['TILEDEC'])

fsize= 7
plt.figure()
plt.scatter(tilera, tiledec)
inra = []
indec = []
for i in range(len(tilera)):
    if (tilera[i] in inra) and (tiledec[i] in indec):
        plt.text(tilera[i]+5, tiledec[i]-5, str(tileid[i]), fontsize=fsize)
    else:
        plt.text(tilera[i]+5, tiledec[i], str(tileid[i]), fontsize=fsize)
    inra.append(tilera[i])
    indec.append(tiledec[i])
    
plt.title("CMX_DITHLOST")
plt.xlim([200,0])
plt.ylim([-30,90])
plt.xlabel("RA [deg]")
plt.ylabel("Dec. [deg]")
plt.savefig("tiles_cmx_20201203/tile_summary.png")
    

