# print(10 + 20)
# print("Hello " + "Bhai")
# # a.__add__(b) == a + b

# class A():
#     def f1(self):
#         pass

# obj1 = A()     
# obj2 = A()    
# obj1.A(20)# == A.f1(obj1, 20)
# obj2.A(40)# == A.f1(obj2, 40)


class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __add__(self,other):
        return self.length + other.length # + other.breadth self.breadth 

r1 = Rectangle(4, 6)
print(r1.area())

r2 = Rectangle(7,4)
print(r2.area())
print(r1+r2)