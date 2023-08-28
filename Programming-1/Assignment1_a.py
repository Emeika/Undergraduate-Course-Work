#task 1

'''
#outpput in s single coloumn
print("1\n2\n3\n4")

'''

#task 2

'''
#giving input
in_1= "abcd"
#and taking the first letter and changing to capital letter, concatinating it with the third digit
out_1= in_1[0].upper()+in_1[2]
print(out_1)


in_2= "9"
#taking input as 9 and changing it to 57 so add 48 to 9
out_2=int(in_2)+48
print(str(out_2))

in_3= "PythonAssignment"
#concatinating 'to' to the 7th letter in the input word
out_3= "to"+in_3[6]
print(out_3)

#printing the first 9 letters and reversing it uptill the 3rd letter
print(in_3[:9:1][:1:-1])

#printing the 12th letter as capital and concatinating it with the 13th letter
print(in_3[12].upper()+in_3[13])

'''

#task 3


'''

#declaring string variables to hold two kind of patterns and comb pattern 3 times in coloums 
comb= ("+--+--+--+\n|"" "" ""|"" "" ""|"" "" ""|\n")*3
bottomline= "+--+--+--+"
#printing both patterns, and the comb pattern without moving to the next line
print(comb, end="")
print(bottomline)
'''


#task 4

'''
#taking the number of ingredients
chicken= input("Enter the no. of chicken meat pieces: ")
lettuce= input("Enter the no. of lettuce leaves: ")
tomato= input("Enter the no. of tomato slices: ")
#integer division with the number of ingredients needed to make one burger
nchicken = int(chicken)//1
nlettuce = int(lettuce)//3
ntomato = int(tomato)//6
#using min to find lowest ingredient 
print("Number of burgers that can be made = ", min(nchicken, nlettuce, ntomato))

'''


#task 5

'''

a= "     Programming is fun :-)"
#using a predefined fuction to remove the begening white spaces from the input word
a= a.lstrip()
print(a)

'''


#task 6
'''

#prompt input from user
t_1= input("enter the first time in military form: ")
t_2= input("enter the second time in military form: ")

#take first 2 digits of the times provided
p = int(t_1[0:2])
q = int(t_2[0:2])

#subtract to get difference in hours
time_1 = int(q - p)

#take last 2 digits of the times provided
x = int(t_1[2:4])
y = int(t_2[2:4])

#subtact to get differnce in minutes
time_2= int(y - x)

#remove negative sign from difference calculated
if time_1 < 0:
    time_1= time_1 * -1
if time_2 < 0:
    time_2= time_2 * -1
    
print(time_1 ,"hours" , time_2 , "minutes")

'''


















































