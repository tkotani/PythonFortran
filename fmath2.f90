subroutine hello2(comm) bind(C)
  implicit none
  include "mpif.h"
  integer(4) :: comm, size, rank, ierr
  call MPI_Comm_size(comm, size, ierr)
  call MPI_Comm_rank(comm, rank, ierr)
  print *, "Hello World222 at rank ", rank, "/", size
end subroutine hello2
