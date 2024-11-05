class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #To overload the operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'vector({self.x},{self.y})'

V1 = Vector(1,6)
V2 = Vector(2,7)

result = V1+V1
print(result)