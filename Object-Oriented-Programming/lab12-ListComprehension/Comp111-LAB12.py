# Hafsah Shahbaz
# 251684784

#Task 1

from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
fib = fib(8)
print(fib)

# Task 3

fib_square = list(map(lambda x: x**2, fib))
print(fib_square)

#Task 2

x = lambda num : 1 if num <= 1 else num*x(num-1)

print(x(5))

#Task 4

string = 'Hafsah Shahbaz'
print(list(filter(lambda x : x not in 'aeiouAEIOU', string)))

