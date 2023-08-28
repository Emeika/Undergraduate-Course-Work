#Task 1
# a
num = 5.6
print(int(num),type(int(num)))


# b
nums = 5678
print(str(nums),type(str(nums)))

# c
# (2+(2*2)) = 6
print(2+2*2)

#Task 2
mul = int(input("Enter any natural number:"))
print("Number multiplied by 20:",mul*20)

#Task 3
fuel = float(input("Enter the amount of fuel in the car: "))
total_distance= float(377.2)  # in km
total_fuel= float((377.2/12)/3.79)  # in gallons(8.29)
distance_travelled= float(round((fuel*total_distance)/total_fuel,2))
print("The distance that can be travelled with" , fuel , "gallons is:" ,distance_travelled, "km") 
if fuel < total_fuel:
	fuel_needed = print("Extra Fuel needed:", round((total_fuel - fuel),2), "gallon")
else:
	print("extra fuel of",round((fuel - total_fuel),2),"gallons")
if distance_travelled > total_distance:
	print("Extra km that can be travelled with extra fuel:", round((distance_travelled - total_distance),2),"km")

#Task 4
def amplifier(frequency,times_amplified):
	print(frequency*times_amplified ,"Hz")
amplifier(60,3)

#Task 5
def check (a,b,c,d,e):
    list=[]
    flist=[]
    list.append (a)
    list.append (b)
    list.append (c)
    list.append (d)
    list.append (e)
    for x in list:
        if (x >= 13 and x <= 18) :
           flist.append(x)
        else:
            None
    return (flist)
print(check (14,23,44,18,12))
print()

#Task 6

word = input("Enter a word: ")
for y in range(1,len(word)+1):
	for x in range(0,len(word)- y +1):
		print(wssord[x:x+y])

#Task 7
# global 
# count = 0,1,2,3,4,5


#Task 8

list_1=[1,2,3,4,5,6,7,8,9,10]
list_2=[2,4,6,8,10,12,14,16,18,20]
print(list(filter(lambda x: x in list_1,list_2)))

#Task 9

# Dictionary of employees ID, Name, Department and Salary
dic = {"employe1" : {"id" : "909", "name":"joe", "department " :"h", "salary":"50000"},
       "employe2": {"id" : "897", "name":"amy", "department " :"f", "salary":"70000"},
       "employe3": {"id" : "597", "name":"kmy", "department " :"Hf", "salary":"60000"},
       "employe4": {"id" : "397", "name":"lmy", "department " :"JK", "salary":"30000"}}
from functools import reduce
def minimum (data):
    return reduce (lambda x, y :x if x<y else y,data)
def maximum (data):
    return reduce (lambda x, y :x if x>y else y,data)

def min(dic):
    dlist=[]
    min_sal=0
    for i in dic:
        dlist.append ((dic[i]["salary"]))
    min_sal = minimum(dlist)
    return min_sal
def max (dic):
    dlist2=[]
    max_sal=0
    for i in dic:
        dlist2.append ((dic[i]["salary"]))
    max_sal = maximum(dlist2)
    return max_sal
print(min(dic))
print(max(dic))