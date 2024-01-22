#mpif90 -shared -fPIC -o ecaljfortran.so *.f90
#mpiexec -n 4 python3 ./hello.py | sort
from ctypes import *
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
comm = comm.py2f()
ecaljfortran = np.ctypeslib.load_library("ecaljfortran.so",".")
ecaljfortran.setcomm.argtypes = [ POINTER(c_int32) ]
ecaljfortran.setcomm.restype  = c_void_p
ecaljfortran.setcomm(c_int32(comm))
