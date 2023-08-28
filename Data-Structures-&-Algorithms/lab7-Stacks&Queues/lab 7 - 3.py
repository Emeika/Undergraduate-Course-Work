# Question 3: [Weightage: 15%]
# Write a python program that reverses a string using stack.

from Stack import Stack

inp = input('Enter a string: ')

stackobj = Stack()

for i in inp:
    stackobj.push(i)

rev = []
l = stackobj.__len__()
for i in range(l):
    rev.append(stackobj.pop())

for x in rev:
    print(x, end ='')




