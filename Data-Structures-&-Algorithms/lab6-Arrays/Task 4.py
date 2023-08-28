# TASK 4
# Use standard control structures to compute the sum of all numbers in an n × n data set,
# represented as a list of lists. Then describe how the built-in sum function can be
# combined with Python’s comprehension syntax to compute the sum of all numbers in an
# n × n data set, represented as a list of lists.


int_list = [[3,2,4,1,5,7,2,3],[3,55,77,3,2,97,343,]]
s = 0
for c in int_list:
    for r in c:
        s += r
print(int_list)
print(s)

s2 = sum([sum(j) for j in int_list])
print(s2)