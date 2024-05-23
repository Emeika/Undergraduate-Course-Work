from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# define the array on the root process
if rank == 0:
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
else:
    data = None

# scatter sub-arrays to all processes
sub_array = comm.scatter(data, root=0)

# each process computes the sum of its sub-array
sub_sum = sum(sub_array)

# gather all sub-array sums to the root process
combine_sum = comm.gather(sub_sum, root=0)

if rank == 0:
    print(f'Array With Sums: {combine_sum}')
