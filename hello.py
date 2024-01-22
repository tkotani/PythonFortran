#mpif90 -shared -fPIC -o fmath.so *.f90
#mpiexec -n 4 python3 ./hello.py | sort
from ctypes import *
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
comm = comm.py2f()
fmath = np.ctypeslib.load_library("fmath.so",".")
fmath.setcomm.argtypes = [ POINTER(c_int32) ]
fmath.setcomm.restype  = c_void_p
fmath.setcomm(c_int32(comm))

fmath.hello()
fmath.hello()
fmath.hello2()
