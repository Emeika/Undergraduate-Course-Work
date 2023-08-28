#task 1

'''
for i in range(1,11):
    for x in range(1,11):
        print(i*x,"", end="")
    print("\n")
   
'''      


#task 2

'''
for j in range(0,21):
    print(2**j)

'''

#task 3
'''
sums = 0
in_1=input("enter a number: ")
x= len(str(in_1))
for i in range(x):
    digit=in_1[i]
    if int(digit) % 2 != 0:
        sums=sums+int(digit)
print("sum of all odd numbers : " , sums)

'''

#task 4

'''
LUCKYNUMBER = 7
for x in range(0,5):
    guess = int(input("enter the lucky number: "))
    if guess == LUCKYNUMBER:
        print("you win")
        break
    else:
        print("you lost")
     
'''           
           
    
    



              























