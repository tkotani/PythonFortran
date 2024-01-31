#!/usr/bin/env python3 
#>mpirun -np 4 pysample
from setcomm import callF,setcomm
from mpi4py import MPI
import ctypes
import sys
# print(*sys.argv[1:])
# load ecalj and MKL libraries. Return ecalj.foobar and communicator
ecaljF,rank,size,comm= setcomm("ecaljF.so", '/usr/lib/x86_64-linux-gnu/libmkl_rt.so')
print("Hello World at rank {0}/{1}".format(rank, size))

# Run fortran codes
callF( ecaljF.hello   )
callF( ecaljF.hello2, [3429] )
comm.barrier()
if(rank==0):print('barrier test end xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
if(rank==3):
    callF( ecaljF.hello3, [True, 34, 18.2, 9.3] )
else:
    callF( ecaljF.hello3, [True, 135, 8.6, 9.3] )

text='123xabcdefc  afdafa adfa456'
print (f'sending text to fortran=',text)
callF(ecaljF.hello4, [text,len(text)])
