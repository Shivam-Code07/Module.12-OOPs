class A:
    def add(self,num1,num2,num3):
        print(num1+num2+num3)

    def add(self,num1,num2):
        print(num1+num2)    

    def add(self,num1,num2,num3,num4):
        print(num1+num2+num3+num4)     
n1 = A() 
# n1.add(1,2,3)      
# n1.add(1,2)      # Hamesha latest vala hi call hoga.
n1.add(1,2,3,4)      