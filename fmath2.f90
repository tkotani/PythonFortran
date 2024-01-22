subroutine hello2() bind(C)
  use m_comm,only: comm,size,rank
  implicit none
  include "mpif.h"
  integer(4) :: ierr
  call MPI_barrier(comm,ierr)
  print *, "Hello World222 at rank ", rank, "/", size
end subroutine hello2

module mmmx
  contains
 subroutine hello3(lll,intx,r1,r2) bind(C)
   use m_comm,only: comm,size,rank
   implicit none
   include "mpif.h"
   integer :: ierr,intx
   logical:: lll
   real(8):: r1,r2
   call MPI_barrier(comm,ierr)
   print *, "Hello World222 xxx at rank ", rank, "/", size,lll,intx, 'sum=',r1+r2
 end subroutine hello3
end module mmmx
