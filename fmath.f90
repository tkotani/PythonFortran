module m_comm
  integer,protected:: comm,size,rank
contains
  subroutine setcomm(commin) bind(C)
    implicit none
    include "mpif.h"
    integer(4) :: ierr,n,commin
    call MPI_Comm_size(commin, size, ierr)
    call MPI_Comm_rank(commin, rank, ierr)
    comm=commin
  end subroutine setcomm
end module m_comm

module m_testx
  use m_comm,only: size,rank
  integer,protected:: iii,n
  logical:: init=.true.
  real(8):: a=3.21
  complex(8),allocatable:: ccc(:,:)
contains
  subroutine hello() bind(C)
    implicit none
    include "mpif.h"
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

