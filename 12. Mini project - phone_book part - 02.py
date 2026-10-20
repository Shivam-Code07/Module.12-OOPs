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

    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_directory:
            if contact.name.lower()  ==  search_name.lower():
                return F"{search_name.capitalize()}: {contact.number}"
          
        return f"No contact found for {search_name.capitalize()}"    

    @staticmethod
    def validate_number(phone_number):
        if 8 <= len(phone_number) <= 12 and phone_number.isdigit():
            return True
        else:
            return False     

n_contacts = int(input("How mane contact do you want to add....?: "))
for i in range(n_contacts):
    name = input("Enter the name: ")
    number = input("Enter the number: ")
    if PhoneBook.validate_number(number):
        PhoneBook(name,number)
    else:
        print("invalid phone number")







# person1 = PhoneBook('John',1234567890)
# person2 = PhoneBook('Carl',8932579034)
# person3 = PhoneBook('Alice',645899032)


PhoneBook.show_all_contact()
# search_result = PhoneBook.search_contact(input("Name: "))
# print(search_result) 