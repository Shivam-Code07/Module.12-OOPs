class Student:
    pass
student1 = Student()
student2 = Student()

student1.name = "John"
student1.roll = 1001


print(student1.name)
print(student1.roll)


# print(student2.name) 
# print(student2.roll)
# student2 @ no attribute

# help(Student)

print(student1.__dict__)
print(student2.__dict__)