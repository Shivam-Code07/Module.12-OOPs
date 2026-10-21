from my_abstract_test import shape


class Square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2
    
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    
class Cicle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):    
        return 3.14 * self.radius ** 2
        
obj = Square(4)
print(obj.area())
obj = Rectangle(4,8)
print(obj.area())
obj = Cicle(4)
print(obj.area())
