# A simple example for python calling fortran codes in MPI

Main program is in python, where we call fortran subroutines from the main program.

## Run an example

This example call subroutines in fmath.f90 from the program hello.py.
That is, we combine hello.py and fortran subroutines.
We have two files setcomm.py and m_comm.py, which are keys to combine them.

To run example,

Step 1. Generate ecaljF.so from fortran source codes.  
$ mpif90 -shared -fPIC -o ecaljF.so *.f90  
  or  
$ mpif90 -c -fPIC m_comm.f90 -o m_comm.o  
$ mpif90 -c -fPIC  fmath.f90 -o fmath.o  
$ mpif90 -shared ecaljF.so m_comm.o fmath.o

Step 2. Call hellop.py in the usual manner.  
$ mpiexec -n 4 python3 ./hello.py

## How this sample works?

1. We can run fortran subrouines successively in hello.py. We can supply only logical,integer, and real(8) when we call a fortran subrouine. No return values from fortran.
2. All the fortran codes can know rank,size, and comm in m_comm module. Let fortran main programs to be subroutines without arguments but with bind(C). See fmath.f90.
3. See our main program hello.py. We init MPI by mpi4py in setcomm.py.

## How we will modify fortran code?

In the techniques in this sample, we can easily use a python code as the main routine. We call fortran programs
(subroutines now) successively. Look into hello.py.
Since fortran subroutines are conneced python code, we can keep data in modules
even when we call nexr fortran subroutine in python.
This is as if we keep data in module even when we have finished fortran main program!

## NOTE

1. compilar option -fpic - non-position-dependent code.
2. Evvensubroutine foobar bind(C) is Global, even when you define foobar bind(C) in a module, it is global.
3. subroutines in module is global from python. Thus we can call subroutine hello2, without specifing use foobar.

## Thanks

This code is inspired by discussion with Atsushi Togo and NAKANO Kosuke in NIMS. And I read
<https://mnakao.net/data/2018/HPFPC.pdf>.
