'''
class d:
    def __init__(self,d):
        self.d = d
        print('in d')

class a(d):
    def __init__(self,a):
        print('in a')
        self.a = a
        super().__init__(1)

class b(d):
    def __init__(self,b):
        self.b = b
        print('in b')
        super().__init__(2)

class c(b,a):
    def __init__(self,c):
        print('in c')
        self.c = c
        super().__init__(3)


cobj = c(5)
print(c.mro())
print(cobj.a)
print(cobj.b)

'''
##

'''
class A:
    def __init__(self,a):
        self.a = a
class B:
    def __init__(self,b):
        self.b = b

class C(B,A):
    def __init__(self,c):
        self.c = c
        A.__init__(self,3)
        B.__init__(self,5)
        #super(B,self).__init__(8)
        #super().__init__(9)

Cobj = C(5)
print(C.mro())
C.mro()
print(Cobj.b)
print(Cobj.a)
'''
class VM:
    def setd(self):
        self.d +=1

    def setr(self):
        self.r +=1

    def getr(self):
        return self.r

    def getd(self):
        return self.d
    def reset(self):
        self.d = 0
        self.r = 0

obj = VM()
obj.reset()
obj.setr()
obj.setr()
obj.etd()
print(obj.getd(), obj.getr())