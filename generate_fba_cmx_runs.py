import numpy as np

def print_run(flavor='science', obscon='dark', intileid=307):
    cmx_exec = '~/fiberassign/bin/./fba_cmx'
    tileid = intileid

    run =  '{} --dr dr8 --dtver 0.43.0 --rundate 2020-03-06T00:00:00 --seed 77 '.format(cmx_exec)
    run += ' --intileid {} ' .format(intileid)
    run += ' --tileid {} '.format(tileid)
    run += ' --obscon {} '.format(obscon)
    run += ' --flavor {} '.format(flavor)
    run += ' --outdir ./cmx_fiberassign/{:06d}_{}_{}'.format(tileid, obscon, flavor)
    return run

data = np.loadtxt('cmx_tile_list.txt')
flavors = ['science', 'dithprec', 'dithlost']
obscons = ['dark', 'bright']

tileids = np.int_(data[:,0])
for flavor in flavors:
    for obscon in obscons:
        for tileid in tileids:
            run = print_run(obscon=obscon, flavor=flavor, intileid=tileid)
            print(run)

