This is a test for python calling fortran codes in f90.

>mpif90 -shared -fPIC -o fmath.so fmath.f90 fmath2.f90
>mpiexec -n 4 python3 ./hello.py 

