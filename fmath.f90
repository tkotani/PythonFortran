module m_testx
  integer,protected:: iii
  logical:: init=.true.
  real(8):: a=3.21
  complex(8),allocatable:: ccc(:,:)
contains
  subroutine hello(comm) bind(C)
    implicit none
    include "mpif.h"
    integer(4) :: comm, size, rank, ierr,n

    call MPI_Comm_size(comm, size, ierr)
    call MPI_Comm_rank(comm, rank, ierr)
    
    if(init) then
       print *, "Hello World at rank ", rank, "/", size,a
       init=.false.
       a=1.23
       n=1000
       allocate(ccc(n,n),source=(1d0,2d0))
    else
       print *, "Hello111 World at rank ", rank, "/", size,a
       print *,'sum(ccc)=',sum(ccc)
    endif
  end subroutine hello
end module m_testx

