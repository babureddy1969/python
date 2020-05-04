#point
import math
class Point:
    def __init__(self, x , y):
        self.x=x
        self.y=y
    def translate(self, dx, dy):
	        self.x += dx
	        self.y += dy
    def distance_from_origin(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
