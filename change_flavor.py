from argparse                      import ArgumentParser
import fitsio
import os

parser = ArgumentParser()
parser.add_argument('--infile',  help='input file',type=str,default=None,required=True, metavar='INFILE')
args     = parser.parse_args()

filenamein = args.infile
filenameout = 'tmp_'+filenamein
if os.path.isfile(filenameout):
    os.remove(filenameout)

print('reading file {}'.format(filenamein))
print('writing file {}'.format(filenameout))

filein =  fitsio.FITS(filenamein,'r')
fileout = fitsio.FITS(filenameout, 'rw')

for i in range(len(filein)):
    extname = filein[i].get_extname()
    header=filein[i].read_header()
    data = filein[i].read()
    header_keys = header.keys()
    print('processing ', extname)
    if 'FLAVOR' in header_keys:
        print('changing EXTNAME', extname)
        header['FAFLAVOR'] = header['FLAVOR']
        header.delete('FLAVOR')
        header_keys = header.keys()
        print(header_keys)
    
    if (extname=='PRIMARY'):
        fileout.write(None, header=header, extname=extname)
    else:
        fileout.write(data, header=header, extname=extname)
    
filein.close()
fileout.close()
os.replace(filenameout, filenamein)