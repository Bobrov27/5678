from math import pi
class Figure:
    def __init__(self): #p = (a+b+c)/2 #sqrt (p*(p-a)(p-b)(p-c))
          pass
    def calculate_area(self):
        pass


class Figure:
    pass



class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        p = (self.a + self.b + self.c) /2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

My_Triangle = Triangle (3,4,5)
print(My_Triangle.calculate_area())


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a*self.b

My_Rectangle = Rectangle(5,4)
print(My_Rectangle.calculate_area())


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi*self.radius**2
My_Circle = Circle(6)
print(My_Circle.calculate_area())
