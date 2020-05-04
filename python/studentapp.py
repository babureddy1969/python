import student
from Point import Point
p1 = Point(100,200)
print(p1)
p1.translate(10,10)
print(p1)
print('from origin',p1.distance_from_origin())
print('from other',p1.distance(Point(10,10)))