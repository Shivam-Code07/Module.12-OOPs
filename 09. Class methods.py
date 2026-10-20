# class Student:
#     college_name = "ABC College"

#     @classmethod
#     def college_change(cls, new_name):
#         cls.college_name = new_name


# student1 = Student()    

# print(student1.college_name)
# Student.college_change('XYZ College')

# print(Student.college_name)

'''
Class methods are defined inside the class that are bound to the class
To create a class methode, we use a decorater -> @classmethod 
'''


class Student:
    '''
    This is a Student to manage student info and activities
    '''
    college_name = "ABC College"
    department = ["Physics", "Mathematics", "Chemistry"]

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
      
    def study(self, hours):
        print(f"The student studies for {hours} hours a day.")   
    def sports(self, sports):
        print(f"The student play {sports}")    
    @classmethod
    def greet(cls,sub):
        cls.sub = sub
    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.department}")  
        for departments in cls.department:
            print(departments)
  



student1 = Student("John",1001)            
student2 = Student("Carl",1002)            
print(student1.name)
print(student1.roll)
student2.greet("Phycis")
print(Student.sub)
print(student1.sub)
print(Student.college_name)
print(student1.college_name)
student1.get_departments()
