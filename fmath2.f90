subroutine hello2() bind(C)
  use m_comm,only: comm,size,rank
  implicit none
  include "mpif.h"
  integer(4) :: ierr
  call MPI_barrier(comm,ierr)
  print *, "Hello World222 at rank ", rank, "/", size
end subroutine hello2
