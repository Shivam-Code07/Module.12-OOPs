class Empolyee:
    def working_hours(self):
        return 45

class Intern(Empolyee):
    def working_hours(self):
        return 40

s1 = Intern()
print(s1.working_hours())