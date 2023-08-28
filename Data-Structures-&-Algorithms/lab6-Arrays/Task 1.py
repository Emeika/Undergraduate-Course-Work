# Question 1:


import sys # provides getsizeof function
data = [5,3,23,5,6,23,5,1]
n = len(data)
for k in range(n): # NOTE: must fix choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.pop() # decrease length by one

