#task 1

length= int(input("enter the side lenght: "))
for i in range(length+1):    
    print(" " * int(length-i),"*" * int(i+(i-1))," " * int(length-i))
 
for x in range(length-1,-1,-1):
    print(" " * int(length-x),"*" * int(x+(x-1))," " * int(length-x))



#task 2
n=3
w=2
s=1
e=4
pos_x=0
pos_y=0
import random
for y in range(100):
    steps= random.randint(1,4)

    if steps==e:
        pos_x=pos_x+1
    elif steps==w:
        pos_x=pos_x+1
    elif steps==n:
        pos_y=pos_y+1
    elif steps==s:
        pos_y=pos_y+1
print("position: " , pos_x, "," , pos_y)

#task 3


word= input("enter a word: ")
x= len(word)
for i in range(x): 
    print(word[i])
print(word[0:2])
print(word[-2:])
print(word)

    
    
