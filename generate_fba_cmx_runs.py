import numpy as np

def print_run(flavor='science', tilera=0.0, tiledec=0.0, numberingid=1, base_numbering=0):
    cmx_exec = '~/fiberassign/bin/./fba_cmx'
    flavor_number = {"dithlost":0,
                     "dithprec":1,
                     "starfaint":2,
                     "scidark":3,
                     "scibright":4,
                     "focus":5}
    
    
    tileid = (80000+base_numbering) + numberingid

    run =  '{} --dr dr9m --dtver 0.45.1 --rundate 2020-03-06T00:00:00 --seed 77 '.format(cmx_exec)
    run += ' --tilera {} ' .format(tilera)
    run += ' --tiledec {} ' .format(tiledec)
    run += ' --tileid {} '.format(tileid)
    run += ' --faflavor {} '.format(flavor)
    run += ' --outdir ./tiles_cmx_20201212/{:06d} &'.format(tileid)
    return run

data = np.loadtxt('cmx_dithprec_list_2.txt')
flavors = ['dithprec']

tileids = np.int_(data[:,0])
ra = data[:,1]
dec = data[:,2]
numberingid = 0
for i in range(len(tileids)):
 #   if ra[i] < 250.0 and np.abs(dec[i]-30)<20:
    tileid = tileids[i]
    for flavor in flavors:
        run = print_run(flavor=flavor, tilera=ra[i], tiledec=dec[i],
                            numberingid=numberingid, base_numbering=332)
        numberingid += 13
        print(run)

