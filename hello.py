# Run MPI fortran codes successively when no arguments are exchanged.
# See setcomm.py

from setcomm import *
import os

#os.system('mpif90 -j -shared -fPIC -o ecaljfortran.so *.f90')
ecaljF = setcomm("ecaljF.so")
callF( ecaljF.hello )
callF( ecaljF.hello )
callF( ecaljF.hello3, [True, 34, 8.2, 9.3] )
