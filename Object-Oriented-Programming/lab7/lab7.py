# 1
class address:
	def __init__(self,houseNo, streetNo, town, city):
		self.houseNo = houseNo
		self.streetNo = streetNo
		self.town = town
		self.city = city

	def display(self):
		print(self.houseNo, self.streetNo, self.town , self.city)



class student:
	def __init__(self, id, name, hNO,stNO,town,city):
		self.id = id
		self.name = name
		self.address = address(hNO,stNO,town,city)

	def display(self):
		print(self.id,self.name)
		self.address.display()


class staff:
	def __init__(self, id, name, hNO,stNO,town,city):
		self.id = id
		self.name = name
		self.address = address(hNO,stNO,town,city)

	def display(self):
		print(self.id,self.name)
		self.address.display()


class faculty:
	def __init__(self, id, name, hNO,stNO,town,city):
		self.id = id
		self.name = name
		self.address = address(hNO,stNO,town,city)

	def display(self):
		print(self.id,self.name)
		self.address.display()

def main():
	studentobj = student(34, 'DaimBkhalid', 9 , 7 , 'arcomplex', 'Lahore')
	facultyobj = faculty(34, 'KiranQaiser', 23 , 4 , 'shadman', 'Lahore')
	staffobj = staff(34, 'HS', 104 , 5 , 'angoori', 'Lahore')

	studentobj.display()
	facultyobj.display()
	staffobj.display()

main()

#2

class bank:
	account = []
	def __init__(self,nameTitle,accNo,accType,balance):
		self.nameTitle = nameTitle
		self.accNo = accNo
		self.accType = accType
		self.balance = balance
		bank.account.append(self)

	def deposit(self,amount):
		self.balance += amount
		print('remaining balance: ', self.balance)




	def withdraw(self,amount):
		self.balance -= amount
		print('remaining balance: ', self.balance)


def main():

	account1Obj = bank('HS', 456 , 'current' , 90000)
	account2Obj = bank('SG', 1191 , 'saving', 50000)
	findacc = input('which account do you want to find: ')
	for i in bank.account:
		if i.nameTitle == findacc:
			i.deposit(int(input('Enter the amount to be deposited: ')))
			i.withdraw(int(input('Enter the amount to be withdrawn')))

main()






