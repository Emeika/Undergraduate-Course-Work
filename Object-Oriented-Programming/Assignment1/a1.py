## Hafsah Shahbaz
## 251684784
# ASSIGNMENT #1 COMP111 B

# 1

def num_english(number):
	alphabets = ['zero','one','two','three','four','five','six','seven','eight','nine']
	if number < 10 or number == 0:
		return alphabets[number]
	else:
		return num_english(number//10)+' '+ alphabets[number%10]

num = 34567
print('The digits of', num , 'in english: ', num_english(num),'\n')


# 2

class die:
    import random

    def roll(self):
        self.number = die.random.randint(1,6)
        return self.number

    def showface(self):
        return self.number

class statistics:
    def __init__(self):
    	self.numlist = []

    def enternum(self,num):
    	self.numlist.append(num)

    def getSum(self):
    	self.sum = 0
    	for i in self.numlist:
    		self.sum += i
    	return self.sum

    def getMean(self):
        self.mean = round((self.sum/len(self.numlist)),2)
        return self.mean

    def getMax(self):
    	self.tempMax = 0
    	for n in self.numlist:
    		if n > self.tempMax:
    			self.tempMax = n
    	return self.tempMax

    def getMin(self):
    	self.tempMin = 10000
    	for n in self.numlist:
    		if n < self.tempMin:
    			self.tempMin = n
    	return self.tempMin

    def getStdDev(self):
        devSum = 0
        for i in self.numlist:
            devSum += (i - self.mean)**2
        self.stdev = round(((devSum/(len(self.numlist)-1))**(1/2)),4)
        return self.stdev

def main():
	testFace = int(input('Enter the die face number to be tested: '))
	while testFace < 0 or testFace > 7:
		testFace = int(input('Enter the correct die face number between 1 and 6: '))

	throwDie = int(input('Enter the number of times the experiment will be run: '))
	throwObj = die()
	statObj = statistics()

	for experiment in range(throwDie):
		check = 0
		for throw in range(50):
			dieFace = throwObj.roll()
			if dieFace == testFace:
				check += 1
		statObj.enternum(check)

	outfile = open('output.txt','w')

	print('The statistics for the die face are as follows:', file = outfile)
	print('The sum is: ', statObj.getSum(), file = outfile)
	print('The mean is: ', statObj.getMean(), file = outfile)
	print('The maximum is: ', statObj.getMax(), file = outfile)
	print('The minimum is: ', statObj.getMin(), file = outfile)
	print('The standard deviation is: ', statObj.getStdDev(), file = outfile)
	outfile.close()

main()