#mpif90 -shared -fPIC -o ecaljfortran.so *.f90
#mpiexec -n 4 python3 ./hello.py | sort
from ctypes import *
import numpy as np
from mpi4py import MPI

def setcomm(aaa):
    comm = MPI.COMM_WORLD
    comm = comm.py2f()
    eee = np.ctypeslib.load_library(aaa,".")
    eee.setcomm.argtypes = [ POINTER(c_int32) ]
    #eee.setcomm.restype  = c_void_p
    eee.setcomm(c_int32(comm))
    return eee

def callF(eee,mmm=[]):
    argtypess=[]
    data=[]
    for ii in  mmm:
        print(ii,type(ii))
        if(type(ii)==type(1)): 
            argtypess.append( POINTER(c_int32) )
            data.append(c_int32(ii))
        elif(type(ii)==type(1.0)):
            argtypess.append( POINTER(c_double) )
            data.append(c_double(ii))
        elif(type(ii)==type(True)):
            argtypess.append( POINTER(c_bool) )
            data.append(c_bool(ii))
    print(f' outputargs=',argtypess)
    eee.argtypes= argtypess
    if(len(argtypess)==0):
        eee()
    else:
        eee(*data)
    return
