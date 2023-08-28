#Task 1
'''
string = "Courage was what it takes to stand up and speak; courage was also what it takes to sit down and listen."
print(string.replace("was" , "is"))
'''

#task 2
'''

n_1 = float(input("Number 1: "))
n_2 = float(input("Number 2: "))

def sum(n_1,n_2):
   sum_ = n_1 + n_2
   print("sum_:" , sum_)
sum(n_1,n_2)

def diff(n_1,_2):
   diff = n_1 - n_2
   print("diff:" , diff)
diff(n_1,n_2)

def product(n_1,n_2):
   product = n_1 * n_2
   print("product:" , product)
product(n_1,n_2)

def average_(n_1,n_2):
    average_ = (n_1 + n_2)/2
    print("average:" , average_)
average_(n_1,n_2)

def maximum(n_1,n_2):
    if (n_1 > n_2):
        print("maximum:" , n_1)
    else:
        print("maximum:" , n_2)
maximum(n_1,n_2)

def minimum(n_1,n_2):
    if (n_1 < n_2):
        print("minimum:" , n_1)
    else:
        print("minimum:" , n_2)
minimum(n_1,n_2)

'''

#task 3
'''
drletter = str(input("drive letter: "))
path =  str(input("the path: "))
filename = str(input("the file name: "))
extension = str(input("the extension: "))
print(drletter + ":\\" + path + "\\" + filename + "." + extension)
'''

#task 4
'''
print("*   *\n*   *\n*****\n*   *\n*   *\n")
print("H\nE\nL\nO\nO")
'''


#TASK 5
'''
str_1 = input("enter first string with even length: ")
str_2 = input("enter second string with a odd lenght: ")
first_1 = print("initals of even string:",str_1[0])
first_2 = print("initial of odd string:"str_2[0])
even = [len(str_1) - 1]
odd = [len(str_2) - 1]
last_1 = print(str_2[even])
last_2 = print(str_2[odd])
'''


#task 7
'''
a = str(input("enter a string: "))
print(a[::-1])
'''

#task 9
'''
lenght = float(input("enter the length of rectangle:"))
width = float(input("enter the width of rectangle:"))
print("area of rectangle = " , lenght*width)
print("perimeter of rectangle = " , 2*(length+width))
'''

#task 10
'''
msg = input("message: ")
print(msg * 20)
'''











    
