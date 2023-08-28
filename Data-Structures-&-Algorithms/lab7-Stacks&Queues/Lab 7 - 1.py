# Task 1
# Question 1: [Weightage: 10%]
# Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, and 10
# pop operations, 3 of which raised Empty errors that were caught and ignored. What is the current size of S?
import random
from Stack import Stack

stackobj = Stack()

for i in range(25):
    stackobj.push(random.randint(0, 10))

for i in range(12):
    stackobj.top()

for i in range(10):
    stackobj.pop()

print(stackobj.__len__())
