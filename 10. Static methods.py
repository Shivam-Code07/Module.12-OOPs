
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
    @staticmethod
    def greet():
        print( "Welcome to the College")
    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.department}")  
        for departments in cls.department:
            print(departments)

student1 = Student('John',1001)
print(student1.name) 
print(student1.roll) 
student1.greet()




# ===================================================================================================
# FEATURE                  | INSTANCE METHOD    | CLASS METHOD          | STATIC METHOD
# ===================================================================================================
# Decorator                | No need            | @classmethod          | @staticmethod
# 1st automatic argument   | self               | cls                   | No need
# How can I call           | From Object        | From Class or object  | From Class or object
# Normal use case          | data  of object    | data  of class        | Independent utility task
# ===================================================================================================