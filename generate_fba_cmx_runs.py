import numpy as np

def print_run(flavor='science', intileid=307, numberingid=1, base_numbering=0):
    cmx_exec = '~/fiberassign/bin/./fba_cmx'
    flavor_number = {"dithlost":0,
                     "dithprec":1,
                     "starfaint":2,
                     "scidark":3,
                     "scibright":4,
                     "focus":5}
    
    
    tileid = (80000+base_numbering)+1000*flavor_number[flavor] + numberingid

    run =  '{} --dr dr9m --dtver 0.45.1 --rundate 2020-03-06T00:00:00 --seed 77 '.format(cmx_exec)
    run += ' --intileid {} ' .format(intileid)
    run += ' --tileid {} '.format(tileid)
    run += ' --flavor {} '.format(flavor)
    run += ' --outdir ./tiles_cmx_20201208/{:06d} &'.format(tileid)
    return run

data = np.loadtxt('dither_zero_list.txt')
flavors = ['dithlost']

tileids = np.int_(data[:,0])
ra = data[:,1]
dec = data[:,2]
indesi = data[:,-1]
numberingid = 0
for i in range(len(tileids)):
    if ra[i] < 250.0:
        tileid = tileids[i]
        for flavor in flavors:
            run = print_run(flavor=flavor, intileid=tileid, 
                            numberingid=numberingid, base_numbering=172)
            numberingid += 1
            print(run)

