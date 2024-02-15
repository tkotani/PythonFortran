#!/usr/bin/env python3 
#>mpirun -np 4 pysample
from setcomm import callF,setcomm,ecaljF,rank,size,comm
from mpi4py import MPI
import ctypes
import sys

#scriptpath = os.path.dirname(os.path.realpath(__file__))+'/'
#arglist=' '.join(sys.argv[1:])
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
text='123xabcdefc  -afda fa adfa456'
print (f'sending text to fortran=',text)
callF(ecaljF.hello4, [text,len(text)])
