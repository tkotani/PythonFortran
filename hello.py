#!/usr/bin/env python3
#> mpif90 -shared -fPIC -o ecaljF.so *.f90  
#> mpirun -np 4 hello.py
from setcomm import callF,setcomm
from mpi4py import MPI
import ctypes
import sys
'''An example to run MPI-fortran codes successively.
   To get ecaljF.so, run >mpif90 -j -shared -fPIC -o ecaljfortran.so *.f90'''
print(*sys.argv[1:])

# load ecalj and MKL libraries. Return ecalj.foobar and communicator
ecaljF,comm = setcomm("ecaljF.so", '/usr/lib/x86_64-linux-gnu/libmkl_rt.so')

# MPI check
rank = comm.Get_rank()
size = comm.Get_size()
print("Hello World at rank {0}/{1}".format(rank, size))

# Run fortran code
callF( ecaljF.hello )
callF( ecaljF.hello )
comm.barrier()
if(rank==0): print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
if(rank==3):
    callF( ecaljF.hello3, [True, 34, 18.2, 9.3] )
else:
    callF( ecaljF.hello3, [True, 135, 8.6, 9.3] )
