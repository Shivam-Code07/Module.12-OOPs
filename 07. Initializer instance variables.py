class Student:
    '''
    This is a class Student to manage student infomation and activities.
    '''

    def __init__(self,name,roll,dep):
        self.name = name
        self.roll_no  = roll
        self.department = dep

    def study(self,n_hours):
        print(f'The student studies for {n_hours} hours a day.')

    def sports(self,sports_name):
        print(f'The student plays {sports_name}.')

student1 = Student("John",1001,"Physic") 

student2 = Student("Carl",1002,"Mathematics")        
student2.grade = "B"

student3 = Student('Alice',1003,'Chemistry')  
student3.department = 'Zoology' 
# student3.roll_no = student3.pop('roll_no') # ye galat concept hai
# student3.__dict__.pop('roll_no') yaha pr ham aagar kuch remove karna hai to object kr data se remove kar rahe hai 

delattr(student3, 'roll_no') # yaha pr ham aagar kuch remove karna hai to direct class se remove kar sakte hai 

print(student1.name,student1.roll_no,student1.department)
print(student2.name,student2.roll_no,student2.department,student2.grade)

print(student1.__dict__)

print(student2.__dict__)

print(student3.__dict__)