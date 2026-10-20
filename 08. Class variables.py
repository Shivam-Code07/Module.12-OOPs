'''
Class variables are defined at the class level
Same copy of the class variables shared among the object
'''



class Student:
    college = 'S.B.S.S. College'
    subject = ['Physic','Mathematics','Chemistry']

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

student1 = Student('Rahul',101)
student2 = Student('Aman',102)


print(f'Student 1 Name: {student1.name}')
print(f'Student 1 Roll Number: {student1.roll}')
print(f'Student 2 Name: {student2.name}')
print(f'Student 2 Roll Number: {student2.roll}')
print(f'Student 1 College: {Student.college}')
print(f'Student 2 College: {Student.college}')
print(f'Student 1 Subject: {Student.subject}')
print(f'Student 2 Subject: {Student.subject}')








# s1 = student1.__dict__
# s2 = student2.__dict__


# print(f'Student 1 Name: {s1['name']}')


# print(f"Student 1 Roll Number: {s1['roll']}"")


# print(f'Student 2 Name: {s2['name']}')


# print(f'Student 2 Roll Number: {s2['roll']}')



# print('--------------------------------------------')






class Student:
    '''
    This is a Student to manage student info and activities
    '''
    college_name = "ABC College"
    department = ["Physic", "Mathematics", "Chemistry"]

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        print(self)

    def study(self, hours):
        print(f"The student studies for {hour} hours a day.")   
    def sports(self, sports):
        print(f"he student play {sports}")    


student1 = Student("John",1001)            
print(student1.__dict__)