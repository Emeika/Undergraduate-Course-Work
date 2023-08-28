# 1
import math

inlist = input('Enter a word: ').split()
mylist=list(set(inlist))
mycount=[]
for i in range(len(mylist)):
        mycount.append(inlist.count(mylist[i]))

mydict=dict(zip(mylist,mycount))
print(mydict)


# 2
class Car:
    def __init__(self, carmake, modelyear, car_color, purchaseYr ='', car_price = '', owner_name =''):
        self.carmake = carmake
        self.modelyear = modelyear
        self.purchaseYr = purchaseYr
        self.car_color = car_color
        self.car_price = car_price
        self.owner_name = owner_name

    def setcarmake(self, carmake):
        self.carmake = carmake
    def setmodelyear(self, modelyear):
        self.modelyear = modelyear

    def setpurchaseYr(self, purchaseYr):
        self.purchaseYr = purchaseYr

    def setcar_color(self, car_color):
        self.car_color = car_color

    def setcar_price(self, car_price):
        self.car_price = car_price

    def setowner_name(self, owner_name):
        self.owner_name = owner_name

    def getcarmake(self):
        return self.carmake
    def getmodelyear(self):
        return self.modelyear

    def getpurchaseYr(self):
        return self.purchaseYr

    def getcar_color(self):
        return self.car_color

    def getcar_price(self):
        return self.car_price

    def getowner_name(self):
        return self.owner_name

    def ownership(self, owner_name, car_price, purchaseYr):
        self.car_price = car_price
        self.purchaseYr = purchaseYr
        self.owner_name = owner_name


    def display(self):
        print(self.carmake,self.modelyear, self.purchaseYr, self.car_color, self.car_price, self.owner_name)


def main():
    carobj = Car('Volvo', 2010, 'red')
    carobj.ownership('bob', 890000, 2020)
    carobj.display()
    carobj.ownership('Sam', 90000, 2022)
    carobj.display()

main()

# 3
from abc import ABC, abstractmethod
class Polygon:
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height, sidelength , side2length):
        self.base = base
        self.height = height
        self.sidelength = sidelength
        self.side2length = side2length

    def area(self):
        print('Triangle area')
        return 0.5 * self.base * self.height

    def perimeter(self):
        print('Triangle perimeter')
        return self.base * self.sidelength * self.side2length

class IsoscelesTriangle(Triangle):
    def __init__(self, base, height, sidelength, side2length):
        super().__init__(base, height, sidelength, side2length)

class EquilateralTriangle(Triangle):
    def __init__(self, base, height, sidelength, side2length):
        super().__init__(base, height, sidelength, side2length)

class Quadrilateral(Polygon):
    def __init__(self, width, length):
        self.width = width
        self.length = length

class Rectangle(Quadrilateral):

    def area(self):
        print('Rectangle area')
        return self.width * self.length
    def perimeter(self):
        print('Rectangle perimeter')
        return 2 *(self.width * self.length)

class Square(Quadrilateral):

    def area(self):
        print('Square area')
        return self.length ** 2
    def perimeter(self):
        print('Square perimeter')
        return self.length * 4

class Pentagon(Polygon):
    def __init__(self, side):
        self.side = side
    def area(self):
        print('Pentagon area')
        return (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * self.side * self.side) / 4
    def perimeter(self):
        print('Pentagon perimeter')
        return self.side * 5

class Hexagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        print('Hexagon area')
        return ((3 * math.sqrt(3) * (self.side * self.side)) / 2)
    def perimeter(self):
        print('Hexagon perimeter')
        return self.side * 6

class Octagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        print('Hexagon area')
        return (2 * (1 + (math.sqrt(2))) * self.side * self.side)

    def perimeter(self):
        print('Hexagon area')
        return self.side * 7

def main():
    triangleobj = Triangle(6, 8, 5, 8)

    Isoscelesobj = IsoscelesTriangle(8, 3, 9, 9)

    Equilateralobj = EquilateralTriangle(5, 5, 5, 5)

    rectangleobj = Rectangle(5, 6)

    squareobj = Square(9, 9)
    pentagonobj = Pentagon(10)
    hexagonobj = Hexagon(4)
    octagonobj = Octagon(9)

    objlt = [triangleobj, Isoscelesobj, Equilateralobj, rectangleobj, squareobj,pentagonobj,hexagonobj,octagonobj ]

    for i in objlt:
        print(i.perimeter())
        print(i.area())
        print()

main()