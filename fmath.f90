module m_test1
  use m_comm,only: size,rank
  !include "mpif.h"
  integer,protected:: iii,n
  logical:: init=.true.
  real(8):: a=3.21
  complex(8),allocatable:: ccc(:,:)
  private
  !public hello
contains
  subroutine hello() bind(C)
    implicit none
    complex(8):: cc
    if(init) then
       print *,'rank/size=',rank,size, "Hello World111init"
       init=.false.
       a=1.23d0
       n=1000
       cc=rank
       allocate(ccc(n,n),source=cc)
    else
      print *,'rank/size=',rank,size, "Hello World111",a,sum(ccc)/n/n
    endif
  end subroutine hello
end module m_test1

subroutine hello2() bind(C)
  use m_comm,only: comm,size,rank
  implicit none
  include "mpif.h"
  integer :: ierr
  call MPI_barrier(comm,ierr)
  print *,'rank/size=',rank,size, "Hello World222"
end subroutine hello2

module m_test2
  contains
! subroutine hello3(lll,intx,r1,r2,aaa) bind(C)
 subroutine hello3(lll,intx,r1,r2) bind(C)
   use m_comm,only: comm,size,rank
   implicit none
   include "mpif.h"
   integer :: ierr,intx
   logical:: lll
   real(8):: r1,r2
!   character(1):: aaa(:)
   call MPI_barrier(comm,ierr)
   if(mod(rank,2)==0) print *,'rank/size=',rank,size, "Hello World333 even", lll,intx,'sum=',r1+r2
   if(mod(rank,2)==1) print *,'rank/size=',rank,size, "Hello World333 odd ", lll,intx,'sum=',r1+r2
 end subroutine hello3
end module m_test2
