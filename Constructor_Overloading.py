class Rectangle:
    def __init__(self,length,width=None):
        self.length = length
        self.width = width if width is not None else length

    def area(self):
        return self.length * self.width

square = Rectangle(10)
rectangle = Rectangle(10,11)

print('Square area:',square.area())
print('Rectangle area:',rectangle.area())
