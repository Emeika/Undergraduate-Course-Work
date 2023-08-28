# task1
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = list(filter(lambda x: x%2 == 0, num))
print("\nEven numbers:")
print(even_num)

odd_num = list(filter(lambda x: x%2 != 0, num))
print("\nOdd numbers:")
print(odd_num)

#task2

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nEven numbers:",list(map(lambda x: x%2 == 0, num)))

print("\nEven numbers:",list(map(lambda x: x%2 != 0, num)))

#task3

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print("\ncommon numbers:\n",list(filter(lambda x: x in a,b)))

#task4
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print("\ncommon numbers:\n", [x for x in a if x in b])
