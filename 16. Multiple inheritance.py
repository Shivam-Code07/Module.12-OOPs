class A():
    def state_1(self):
        print("This is state 1")
    def state_2(self):
        print("This is state 2")

class B():
    def state_3(self):
        print("This is state 3")
    def state_4(self):
        print("This is state 4")        

class C(A,B):
    def state_5(self):
        print("This is state 5")
    def state_6(self):
        print("This is state 6") 

c1 = C()
c1.state_1()
c1.state_2()
c1.state_3()
c1.state_4()
c1.state_5()
c1.state_6()