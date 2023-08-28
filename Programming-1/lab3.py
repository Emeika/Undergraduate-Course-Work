#task 1

def fav_movie():
    movie= input("Please enter your favourite movie name: ")
    if movie=="":
       print("Spider Man")
    else:
        print(movie)
fav_movie()



#task 2


def sums(number1,number2):
    a= number1 + number2
    return(a)

def sub(number1,number2):        
    b= number1 - number2
    return(b)

def mul(number1,number2):
    c= number1 * number2
    return(c)

def divide(number1,number2):
    d= number1/number2
    return(d)


def calculator():
    number1= int(input("enter the first number: "))
    number2= int(input("enter the second number: "))
    adds = sums(number1,number2)
    print("the sum is:",adds)
    subs= sub(number1,number2)
    print("the difference is:",subs)
    muls= mul(number1,number2)
    print("the product is:",muls)
    divides= divide(number1,number2)
    print("the division is:",divides)
calculator()



#task 3


def repeater():
    a=input("enter a string:")
    print(a * 20)
repeater()


#task 4

def word():
    a=input("enter a sentance:")
    x=input("count of a particular word:")
    b=a.split(",")
    print(b)
    c=a.count(x)
    print(c)
word()



#task 5


def last_remove(a,n):
    word= len(a)-n
    print(a[0:word])
    return
last_remove("bye",5)







                   
                   
                 






