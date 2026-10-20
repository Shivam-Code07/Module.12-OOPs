class Vechile:
    company = "xyx company"


    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"Seats: {self.n_wheels}, Wheels: {self.n_seats}, Mileage: {self.mileage} "

bike = Vechile(2,3,50)
print(bike.get_details()) 

class Car(Vechile):
    pass

# Car class inherits the vechile class
# Car class is called child Class/Derived class
# Vechile class is called Parent class/Base class