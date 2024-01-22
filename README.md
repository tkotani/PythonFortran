# A simple example for python calling fortran codes in MPI.

## How to controll fortran (MPI) by python?

1. We can run fortran subrouines (without arguments) successively in hello.py.
2. All the fortran codes need to get rank,size, and comm in m_comm module. Modify fortran main programs to be subroutines without arguments but with bind(C).
   See fmath.f90 and fmath2.f90.
2. See our main program hello.py. We init MPI by mpi4py in setcomm.py.

## Usage of example
To run example,o

$ mpif90 -shared -fPIC -o ecaljfortran.so *.f90

$ mpiexec -n 4 python3 ./hello.py 

### Our code is inspired by https://mnakao.net/data/2018/HPFPC.pdf

-fpic - 位置に依存しないコードを生成します。

* subroutine foobar bind(C) is Global!
Even when you define foobar bind(C) in a module, it is global.
