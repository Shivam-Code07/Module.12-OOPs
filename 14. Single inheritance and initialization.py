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
    model = "BMWS005"
    def __init__(self,car_type,drive_type):
        self.car_type = car_type
        self.drive_type = drive_type
        # Vechile.__init__(self,4,2,20)
        super().__init__(4,2,20)

c1 = Car('electric','manual')


print(c1.car_type)
print(c1.mileage)
print(c1.drive_type)
print(c1.n_wheels)
print(c1.n_seats)