"""
Design geometric approach for minima-point problem while sweeping
the sweep line along y-direction? Change the class-discussed algorithm accordingly. Dry
run your algorithm to prove its working, displaying the stack states side by side.

"""


from queue import Empty
class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def is_not_empty(self):
        return len(self._data) > 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Create a list of Point3D objects using the provided coordinates


points = [Point3D(12, 5, 8), Point3D(21, 3, 6), Point3D(4, 7, 2), 
        Point3D(10, 2, 5), Point3D(2, 3, 2), Point3D(6, 1, 3), Point3D(2, 1, 10)]



# Sort points based on y-coordinate
points.sort(key=lambda point: point.y)
for point in points:
    print(point)
print("\n")


s = Stack()

for i in range(len(points)):
    while s.is_not_empty() and s.top().x >= points[i].x and s.top().z >= points[i].z:
        s.pop()
    s.push(points[i])

for p in s:
    print(p)


"""
DRY RUN:
sorted points on y coordinate: 
(6, 1, 3)   (2, 1, 10)   (10, 2, 5)   (21, 3, 2)   (2, 3, 2)   (12, 5, 8)   (4, 7, 2)
check the inner loop:
while s.is_not_empty() and s.top().x >= points[i].x and s.top().z >= points[i].z:
        s.pop()
    s.push(points[i])

STACK TRACE:
i = 0:                         i = 1:
p = (6, 1, 3)                  p = (2, 1, 10)
stack:                         stack: condition is false so we push
[ (6, 1, 3) ]                  [ (2, 1, 10) ]
                               [ (6, 1, 3) ] 



i = 2:                          i = 3:
p = (10, 2, 5)                  p = (21, 3, 2)
stack:condition is false        stack: condition is false
[ (10, 2, 5) ]                  [ (21, 3, 2) ]
[ (2, 1, 10) ]                  [ (10, 2, 5) ] 
[ (6, 1, 3) ]                   [ (2, 1, 10) ]
                                [ (6, 1, 3) ] 


i = 4:                                 i = 5:
p = (2, 3, 2)                          p = (12, 5, 8)
condition is true so pop               condition is false
again condition true pop               
again condition true pop
pop again as 6,1,3 has x and z
greater than (2,3,3)
stack:                                  stack: 
[  ]                                   [ (12, 5, 8) ] 
[  ]                                   [ (2, 3, 2) ]           
[  ]                  
[ (2, 3, 2) ]                   
                                


i = 6:                          
p = (4, 7, 2)                  
stack:condition is true so pop        
[ (4, 7, 2) ]
[ (2, 3, 2) ] 

final minimal points:  (2, 3, 2),   (4, 7, 2)
"""