# task 1

'''
#global function created to take string  and strng 2
def print_left_right(s1,s2):
    #finding the length of each string
    len1 = len(s1)
    len2 = len(s2)
    #subtract the lengths of both strings with the total number of characters in a line which is 50 to find the number of dots needed
    #concatinate the first string with the dots and second string
    print(s1 + "." * int(50-len1-len2) + s2)
#call the fuction and give both strings to s1 and s2
print_left_right("hello","world")

'''

#task 2

'''
#function to take the values of string 1 and string 2
def compare1_2(str1,str2):
    #lenghts of both strings
    len1 = len(str1)
    len2 = len(str2)
    valid = "true"
    #if string1 is longer than string 2 then returns true
    if len1 > len2:
        print(valid)
    #otherwise it returns the opposite of true which is false
    else:
        print(not(valid))
#function call to give variables to str1 and str2
compare1_2("hello","hi")
    
'''

#task 3

'''
#function defined for if the full string in p occurs in q or vice versa return true else false
def isIn(p,q):
    if p in q or q in p:
        isIn = True
    else:
        isIn = False
    print(isIn)
#call function isIn to give p and q, two strings
isIn("apple","zoo")

'''


#task 4

'''
letter = input("enter an alphabet: ")
strlen = len(letter)
#taking the length of the letter to check if its a single letter or not and giving an error message if it is
if strlen > 1 or not(letter.isalpha):
    print("InValid Entry! Enter a single letter")
#using the in operator to check for vowel
elif letter in ('a','e','i','o','u') or letter in ('A', 'E', 'I', 'O', 'U'):
    print("This is a vowel")
#if the entered letter does not exist in the the list of vowels then print its a consonant
else:
    print("This is a consonant")
        
'''

#task 5

'''

#taking input from user and making sure its within the range else it propmts user to enter again till its within range
number = int(input("Enter a number upto 3,999: "))
while number > 3999 or number < 0:
    number = input("Invalid! , Enter again")
# creating list of unit, tens, hundreds and thousands in roman form
O = ["", "I" , "II" , "III" , "IV" , "V" , "VI" , "VII" , "VIII" , "IX"]
L = ["", "X" , "XX" , "XXX" , "XL" , "L" , "LX" , "LXX" , "LXXX" , "XC"]
C = ["", "C" , "CC" ,"CCC" ,"CD" , "D" , "DC" , "DCC" ,"DCCC" , "CM"]
M = ["", "M" , "MM" , "MMM"]
th = M[number // 1000]
hu = C[(number % 1000) // 100]
ten = L[(number % 100) // 10]
un = O[number % 10]
roman = (th + hu + ten + un)
print(roman)
                   
'''

#task 6

'''
import random
j = 0
word = input("Enter any word: ")
for i in range(len(word)):
    i = random.randint(0,len(word)-2)
#to make sure that j is greater than i
    while(j<=i):
        j= random.randint(0,len(word)-1)
#first part of the string till position i
first = word[:i]
#middle from i to j
mid = word[i+1:j]
#last from j to last
last = word[j+1:]
word = first + word[j] + mid + word[i] + last
print(word)
'''

#task 7
'''

#taking input from user and coverting to integer
sidelen = int(input("Enter the side length: "))
#printing asterisk according to the lenght
for x in range(sidelen):
#printing the first and the second line with filled asterisks
    if x == 0 or x == (sidelen - 1):
        print("*" * sidelen + "  " + "*" * sidelen)
#printing the middle with hollow asterisks
    else:
        print("*" * sidelen + "  " + "*" + " " * (sidelen-2) + "*" )
    print()

'''

#task 8

'''
altersum = 0
altermul = 0
mulsum = 0
ccnum= input("Enter the eight digit card number: ")
while len(ccnum) != 8:
    ccnum= input("Invalid! Enter again, the eight digit card number: ")
#sum of every other digit, starting from the last
for x in range (7,-1,-2):
    altersum = altersum + int(ccnum[x])
#double the remaining digits and adding each sepearte digit from the last
for y in range (6,-1,-2):
    altermul = str(int(ccnum[y]) * 2)
    if len(altermul) == 2:
        mulsum = mulsum + int(altermul[0]) + int(altermul[1])
    elif len(altermul) == 1:
        mulsum = mulsum + int(altermul)
#adding both the sums 
total = mulsum + altersum
remainder = total % 10
#if total come to zero then the check digit is correct
if remainder == 0:
    print("valid")
else:
    lastdigit = int(ccnum[-1])
    if lastdigit - remainder < 0:
        checkdigit = lastdigit + (10 - remainder)
    else:
        checkdigit = lastdigit - remainder
    print(" Invalid!" , checkdigit , "is the check digit ")
#checking the correct check digit

'''
                   

    
#task 9

'''
#if the remainder is zero then its not prime otherwise prime which means its not divisible by any number
def is_prime(num):
    for i in range(1,num+1):
        if (num % i) == 0:
            return False
        return True
def all_primes(num):
    for n in range(1,num+1):
        if is_prime(n) is True:
            print(n)
num = int(input("Enter an integer: "))
primes = all_primes(num)


'''

#ask mam how to do with nested if


