class PhoneBook():
    phone_directory = []
    def __init__(self,name,number):
        self.name = name
        self.number = number
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}  Phone Number: {self.number}"

    @classmethod 
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contact in the Phone Directory")   
        else:
            for PhoneBook in cls.phone_directory:
                print(PhoneBook.show_contact())

person1 = PhoneBook('John',1234567890)
person2 = PhoneBook('Carl',8932579034)


PhoneBook.show_all_contact()
