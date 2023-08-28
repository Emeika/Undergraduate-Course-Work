#list

#task 1

'''
num =[]
def replace():
    for i in range(3):
        num.append(int(input("enter a num: ")))
    for x in range(3):
        if num[x]%2==0:
            num[x]='hello'
    print(num)
replace()
'''

#task 2
'''
def reverse():
    values =[19,62,83,43,53,46,5,9]
    print(values[::-1])
reverse()
'''

#task 3

'''
a = []
for i in range(21):
    a.append(i)
print(a)
'''

#task 4

'''
import random
a_list = []
for i in range(10):
    a_list.append(random.randrange(1,101))
print(a_list)

'''

#task 5

'''
def multiply(num):
    total = 1
    for x in num:
        total *= x
    return total
print(multiply((8,3,5,7)))
'''

#dictionariess


#task 1

'''
n = str(input("enter a value:"))
dict_1 = {"a": 1,"b": 2,"c": 3}
if n in dict_1:
   print("present")
else :
   dict_1[n]=4
   print ("not present so added   :"  ,dict_1)
'''

#task 2
'''
list1= {1:2,2:5}
print(list1)

list2= {3:4, 5:6, 7:8}
list1.update(list2)
print(list1)
'''
#task 3
'''

num= int(input("enter number:"))
dic = {}
for x in range(1, num+1):
    dic[x] = x*x
print(dic)
'''

#task 4

'''
a_dictionary = {1:'a' ,2:'b', 3:'c', 4:'d'}
for key, value in a_dictionary.items():
    print(key, value)

'''































    
