from math import pi

class Figure:
    def __init__(self): #p = (a+b+c)/2 #sqrt (p*(p-a)(p-b)(p-c))
          pass
    def calculate_area(self):
        pass




class triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        p =





















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
















