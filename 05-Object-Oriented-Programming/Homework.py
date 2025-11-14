import math

class Line():

    #constructor
    #coor is being passed as tuple (x,y)
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

        self.x1, self.y1 = self.coor1
        self.x2, self.y2 = self.coor2

    #calculate distance
    def distance(self):
        return ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5
    
    #calculate the slope
    def slope(self):
        return (self.y1 - self.y2) / (self.x1 - self.x2)
    
# EXAMPLE OUTPUT
print('----------- Line Example -----------')
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())    #9.433981132056603
print(li.slope())       #1.6


class Cylinder():

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (self.radius ** 2) * math.pi * self.height
    
    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * (self.radius ** 2) * math.pi
    
# EXAMPLE OUTPUT
print('----------- Cylinder Example -----------')
c = Cylinder(2,3)
print(c.volume())       #56.548667764616276
print(c.surface_area()) #94.24777960769379