#mpif90 -shared -fPIC -o fmath.so fmath.f90
#mpiexec -n 4 python3 ./hello.py | sort
from ctypes import *
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
comm = comm.py2f()

fmath = np.ctypeslib.load_library("fmath.so",".")
fmath.hello.argtypes = [ POINTER(c_int32) ]
fmath.hello.restype  = c_void_p
fmath.hello2.argtypes = [ POINTER(c_int32) ]
fmath.hello2.restype  = c_void_p

fmath.hello(c_int32(comm))
fmath.hello(c_int32(comm))
fmath.hello2(c_int32(comm))
