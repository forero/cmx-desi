import glob
import fitsio
import numpy as np
from astropy.table import Table

tilefiles = np.sort(glob.glob("tiles_cmx_20201125/fiberassign-08*.fits"))
print(tilefiles)

rows = []
for tilefile in tilefiles:
    print(tilefile)
    #citls, 
    h = fitsio.read_header(tilefile)
    data =fitsio.read(tilefile, ext='FIBERASSIGN')
    targets = fitsio.read(tilefile, ext='TARGETS')
  
    max_flux = data['FLUX_R'].max()
    if max_flux < 1E-2:
        INDESI = 0
    else:
        INDESI = 1
    INDESI = 1
    print(max_flux, len(data), len(targets), INDESI)
    RA = h['TILERA']
    DEC = h['TILEDEC']
    TILEID = h['TILEID']
    ii = np.argmax(targets['GAIA_PHOT_G_MEAN_MAG'])
    BRIGHTRA = targets['RA'][ii] 
    BRIGHTDEC = targets['DEC'][ii]
    BRIGHTVTMAG = targets['GAIA_PHOT_G_MEAN_MAG'][ii] 
    EBV_MED =  np.median(data['EBV'])
    STAR_DENSITY =  len(targets)/8
    IN_DESI = 1
  
    rows.append((RA, DEC, TILEID, BRIGHTRA, BRIGHTDEC, BRIGHTVTMAG, EBV_MED, STAR_DENSITY, IN_DESI, 'CMX'))
t = Table(rows = rows, names=['RA', 'DEC', 'TILEID', 'BRIGHTRA', 'BRIGHTDEC', 'BRIGHTVTMAG', 'EBV_MED', 'STAR_DENSITY', 'IN_DESI', 'PROGRAM'])

t.write('summary_tiles.fits', overwrite=True)
    
   
    
 #   print('H', h['TILEID'], data['FLUX_R'].max())
    
#    TILEID  =                81593 / 
#TILERA  =     29.1873560998107 / 



#TILEDEC =    0.574227370375913 / 
#FIELDROT

    