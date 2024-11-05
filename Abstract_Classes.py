from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
#class for circle
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

#class for square
class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2

#instances
circle = Circle(9)
square = Square(9)

print(f'circle area: {circle.area():,.2f}')
print(f'Square area: { square.area(): }')
