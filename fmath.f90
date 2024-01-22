module m_testx
  use m_comm,only: size,rank
  !include "mpif.h"
  integer,protected:: iii,n
  logical:: init=.true.
  real(8):: a=3.21
  complex(8),allocatable:: ccc(:,:)
contains
  subroutine hello() bind(C)
    implicit none
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

