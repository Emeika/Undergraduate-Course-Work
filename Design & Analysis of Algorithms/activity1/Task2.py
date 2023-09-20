"""
Write python/C++/Java script for your above algorithm and generate
screen dump of your program’s output for at least 7 points. Note that your program should
be general and should work fine for any value of n points.

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


#points = [Point3D(12, 5, 8), Point3D(21, 3, 6), Point3D(4, 7, 2), 
  #      Point3D(10, 2, 5), Point3D(3, 4, 9), Point3D(6, 1, 3), Point3D(2, 1, 10)]

# points = [Point3D(1, 5, 2), Point3D(2, 5, 3), Point3D(3, 5, 1), Point3D(4, 5, 4)]
# points = [Point3D(5, 1, 2), Point3D(5, 2, 3), Point3D(5, 3, 1), Point3D(5, 4, 4)]
# points = [Point3D(1, 1, 1), Point3D(2, 2, 2), Point3D(3, 3, 3), Point3D(4, 4, 4)]
# 
points = [Point3D(2, 9, 1), Point3D(2, 5, 2), Point3D(2, 4, 3), Point3D(2, 1, 4)]

# Sort points based on x-coordinate
points.sort(key=lambda point: point.x)


s = Stack()

for i in range(len(points)):
    while s.is_not_empty() and s.top().y <= points[i].y and s.top().z <= points[i].z:
        s.pop()
    s.push(points[i])

for p in s:
    print(p)