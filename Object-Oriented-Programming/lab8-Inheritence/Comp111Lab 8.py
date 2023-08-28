#Hafsah Shahbaz
#251684784
#1
class polygon:
    def __init__(self, numOfside):
        self.numOfside = numOfside

    def inputSides(self,length, height):
        self.length = length
        self.height = height

        return self.length, self.height

class triangle(polygon):
    def __init__(self,numOfside):
        super().__init__(numOfside)

    def area(self):
        self.area = 1/2 * self.length * self.height
        return self.area

    def display(self):
        print(self.area)

class square(polygon):
    def __init__(self,numOfside):
        super().__init__(numOfside)

    def area(self):
        self.area = self.length**2
        return self.area

    def display(self):
        print(self.area)

def main():
    num = int(input("Number of sides 3 or 4: "))
    polygonobj = polygon(num)
    if num == 3:
        triangleobj = triangle(num)
        triangleobj.inputSides(6, 7)
        triangleobj.area()
        triangleobj.display()
    elif num == 4:
        squareobj = square(num)
        squareobj.inputSides(5, 5)
        squareobj.area()
        squareobj.display()
main()

#2

class person():

    def __init__(self, personId, personName):
        self.personId = personId
        self.personName = personName

class patient(person):

    def __init__(self, personId , personName, disease):
        super().__init__(personId, personName)
        self.disease = disease
        self.treatment = ''

    def chart(self):
        print(self.personId , self.personName , self.disease, self.treatment)

class doctor(person):
    def __init__(self,personId , personName):
        super().__init__(personId, personName)

    def treat(self,patientobj):
        patientobj.treatment = input('Diagnosis: ' + patientobj.disease + '. Enter treatment: ')

def main():
    patientobj = patient(43, 'daim' , 'insomnia')
    doctorobj = doctor(43, 'Dr')
    patientobj.chart()
    doctorobj.treat(patientobj)
main()





