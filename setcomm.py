# This version allow only integer:: real(8):: logical:: can be passed to fortran. No return.
# This should be easily replaced by fortran code.
#mpif90 -shared -fPIC -o ecaljF.so *.f90
#mpiexec -n 4 python3 ./hello.py | sort
from ctypes import (CDLL, POINTER, c_int32, c_double, c_bool,
                    c_char, ARRAY, byref, create_string_buffer)
import numpy as np
from mpi4py import MPI
import ctypes

def setcomm(fortranso,mkl):
    ''' Pass communicator to module m_comm.f90 
        Setcomm requires a shared library libfoobar.so, generaged by
        >mpif90 -shared -fPIC -o ecaljF.so m_comm.f90 fmath.f90'''
    comm = MPI.COMM_WORLD
    commi = comm.py2f()
    CDLL(mkl, mode=ctypes.RTLD_GLOBAL)
    flib = np.ctypeslib.load_library(fortranso,".")
    flib.setcomm.argtypes = [ POINTER(c_int32) ]
    flib.setcomm(c_int32(commi))
    rank = comm.Get_rank()
    size = comm.Get_size()
    return flib,rank,size,comm

def callF(foobar,arguments=[]):
    '''Equivalent to 'call foobar(a,b,c,...)' in fortran, where we supply arguments=[a,b,c,...]. 
       a,b,c,... are integer,logical, or real(8) in this version of callF.'''
    MAXSTRLEN=512
    c_char_array = ARRAY(c_char,MAXSTRLEN)
    argtypess=[]
    data=[]
    for ii in arguments:
        #print(ii,type(ii))
        #NOTE: PI42=POINTER(c_int)(c_int(42)): 42 is converted to binary represenation in C. and Its pointer is PI42
        if(type(ii)==type(1)):  
            argtypess.append( POINTER(c_int32) ) # data type
            data.append(c_int32(ii))             # data 
        elif(type(ii)==type(1.0)):  
            argtypess.append( POINTER(c_double) )
            data.append(c_double(ii))
        elif(type(ii)==type(True)):
            argtypess.append( POINTER(c_bool) )
            data.append(c_bool(ii))
        elif(type(ii)==type('a')): #Not working well, because bind(C) in fortran allows only char(1)::aaa(:)
            argtypess.append( POINTER(c_char_array) )
            data.append(byref(create_string_buffer(ii.encode(),MAXSTRLEN)))
        #print(f' outputargs=',argtypess)
        #print(f' data=',data)
    foobar.argtypes= argtypess
    if(len(argtypess)==0):
        foobar()
    else:
        foobar(*data)
    #print(f' enddddddddd')
    return
