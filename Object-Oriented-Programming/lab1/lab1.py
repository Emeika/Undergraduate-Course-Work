# 1

rate = int(input('enter the annual interest rate: '))
original = int(20)
total = original
years = 0

while (original <= total*2):
	original += original * (rate/100)
	years += 1

print('number of year:' , years,'\n')



#2

n = int(input('Enter any number: '))
prime = True
for i in range(2,n+1):
	if n%i == 0:
		x = False
		break
if prime is True:
	print('prime','\n')
else:
	print('not prime')
		


#3

mystery = {'HAFSAH':20,'DAIM':51,'KIRAN':11,'MANAL':29}
def ageing(dic):
	for key in mystery:
		mystery[key] = mystery[key] + 1
	print(mystery, '\n')
ageing(mystery)


#4

Id = input("Enter student id: ")
print('Student ID  ', Id)

infile=open("classes.txt","r")
data=infile.readline().rstrip("\n")
while data !="":
        subject_dataject=data+".txt"
        subject_data=open(subject_dataject,"r")
        data1=subject_data.readline().split()
        while len(data1)!=0:
                        if Id==data1[0]:
                                print(data,"\t",data1[1])
                        data1=subject_data.readline().split()
        data=infile.readline().rstrip("\n")
		


















