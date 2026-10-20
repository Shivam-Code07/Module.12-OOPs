class Student:
    def study(self,n_hours):
        print(f'The student studies for {n_hours} hours a day.')

    def sports(self,sports_name):
        print(f'The student plays {sports_name}.')

student1 = Student()        
student1.study(4)
student1.sports("Football")
print("--------------------------------------------")
student2 = Student()        
student2.study(6)
student2.sports("Cricket")