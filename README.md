# A simple example for python calling fortran codes in MPI.
Main program is in python, where we call fortran subroutines from the main program.

## Run an example
This example call subroutines in fmath.f90 from the program hello.py,
where we have setcomm.py and m_comm.py, so as to combine hello.py and fortran subroutines.

To run example, o

$ mpif90 -shared -fPIC -o ecaljF.so *.f90

$ mpiexec -n 4 python3 ./hello.py 


## How this sample works?

1. We can run fortran subrouines successively in hello.py. We can supply only logical,integer, and real(8) when we call a fortran subrouine. No return values from fortran. 
2. All the fortran codes can know rank,size, and comm in m_comm module. Let fortran main programs to be subroutines without arguments but with bind(C). See fmath.f90.
3. See our main program hello.py. We init MPI by mpi4py in setcomm.py.

## How we will modify fortran code?
In the techniques in this sample, we can easily use a python code as the main routine. Then we call fortran programs 
(subroutines now) successively.
Since fortran programs are runned as a library, we can keep what is in modules even when we call nexr fortran code.
This implies we can keep what we got in modules in the next call of fortran program.


## NOTE
1. compilar option -fpic - non-position-dependent code.
2. Evvensubroutine foobar bind(C) is Global, even when you define foobar bind(C) in a module, it is global.
3. Thanks. This sample is inspired by discussion with A.Togo and Nakano in NIMS. And I saw
https://mnakao.net/data/2018/HPFPC.pdf.
4. subroutines in module is global from python. Thus we can call subroutine hello2, without specifing use foobar.
