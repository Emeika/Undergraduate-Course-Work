class classroom():
	total = 0
	def __init__(self,classroomId, no_student, namelst):
		self.classroomId = id 
		self.no_student = no_student
		self.namelst = namelst
		classroom.total += no_student


	def studentadded(self,name):
		self.no_student += 1
		classroom.total += 1
		self.namelst.append(name)

	def getstudentcount(self):
		return self.no_student

	def displayClassroom(self):
		print(self.namelst)

	def getTotalStudentCount(self):
		return classroom.total

def main():
	a = classroom(98 , 1 , ['h'])
	b = classroom(89 , 2 , ['d','l'])
	c = classroom(87 , 3 , ['j','o','i'])


	a.studentadded('l')
	a.displayClassroom()
	print('total students in class',a.getstudentcount())
	print(a.getTotalStudentCount())

	b.studentadded('m')
	b.displayClassroom()
	print('total students in class',b.getstudentcount())
	print(b.getTotalStudentCount())


	c.studentadded('o')
	c.displayClassroom()
	print('total students in class',c.getstudentcount())
	print(c.getTotalStudentCount())

main()









		