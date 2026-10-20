# """
# Python Instance Methods - Quick Review Notes
# ---------------------------------------------

# 1. Instance Method Kya Hai?
#    - Class ke andar define kiye gaye functions ko methods kehte hain.
#    - Jo methods object (instance) ke sath bound ya associated hote hain, unhe **Instance Methods** kehte hain.
#    - Built-in data types (jaise list ke append, pop, clear) sabhi instance methods hain.

# 2. 'self' Argument ka Concept:
#    - Jab aap instance method ko object se call karte hain (`obj.method()`), Python internally us object ko as a first argument pass kar deta hai.
#    - Is object ko receive karne ke liye method ke parameter mein ek argument dena zaroori hota hai.
#    - Standard convention ke mutabiq is first parameter ka naam **`self`** rakha jata hai.

# 3. 'self' Kya Represent Karta Hai?
#    - `self` kuch aur nahi balki wahi actual object (instance) hota hai jisne method ko call kiya hai.
#    - `self` ko print karne par wahi memory address aur object details milti hain jo object print karne par milti hain.

# 4. Key Rule for Instance Methods:
#    - Kisi bhi custom instance method ko banate waqt uska pehla parameter hamesha `self` hona hi chahiye.
#    - Agar `self` nahi likhenge, toh Python error throw karega (takes 0 positional arguments but 1 was given).
# """


class Student:
    '''
    This is a class Student to manage student infomation and activities.
    '''
    def study(self):
        print(f'self is: {self}')
        print("Hello, World \n i am learning instance method in OOPs")

   
student1 = Student()    
print(f'the object: {student1}')


Student.study(student1)

'''
When we call an instance methodusing the object/instance of the class, 
python pass the object it self as the first argument two the method
that 1st argument is by standard is self


'''