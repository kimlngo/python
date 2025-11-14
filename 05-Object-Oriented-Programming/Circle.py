class Circle():
    #Class Object Attribute
    #can be retrive by calling class name too: Circle.pi
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = Circle.pi * (radius ** 2) #define the new attribute without explicit argument

    #Method
    def calc_circumference(self):
        return 2 * Circle.pi * self.radius
    

circle = Circle(30)
print(f'radius: {circle.radius}')
print(f'circumference: {circle.calc_circumference()}')
print(f'area: {circle.area}')