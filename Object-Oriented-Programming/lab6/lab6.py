class actor:

	def __init__(self, name, dateofbirth, gender, movie):
		self.name = name
		self.dateofbirth = dateofbirth
		self.gender = gender
		self.movie = movie
		

	def setname(self,name):
		self.name= name
	def setdateofbirth(self,dateofbirth):
		self.dateofbirth = dateofbirth
	def setgender(self,gender):
		self.gender = gender

	def getname(self,name):
		return self.name
	def getdateofbirth(self,dateofbirth):
		return self.dateofbirth
	def getgender(self,gender):
		return self.gender

	def DisplayActor(self):
		print(self.name , self.dateofbirth , self.gender)
		for i in self.movie:
			print(i)

	def AddMovie(self,moviename):
		self.movie.append(moviename)
		

	def CompareActor(self,moviename2):
		lst = []
		for x in self.movie:
			if x in moviename2.movie:
				lst.append(x)
		return lst

def main():

	infile = open('actor.txt','r')
	objlit = []
	for line in infile:
		line = line.strip()
		wordList = line.split(',')
		actorobj = actor(wordList[0],wordList[1],wordList[2],wordList[3:])
		objlit.append(actorobj)

	
	for i in objlit:

		i.DisplayActor()
	

	print(objlit[0].CompareActor(objlit[1]))

	infile.close()
main()




