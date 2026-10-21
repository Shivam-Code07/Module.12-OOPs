class Vechile:
    company = 'TATA Moters'

    def __init__(self, n_sheets, n_wheels, mialage):
        self.n_sheets = n_sheets
        self.n_wheels = n_wheels
        self.mialage = mialage

    def vechile_info(self):
        print(f"Number of Sheets in Vechile: {self.n_sheets}")
        print(f"Number of Wheels in Vechile: {self.n_wheels}")
        print(f"Vechile Mialage : {self.mialage}")


class Car(Vechile):
    model_name = "Mercedes Benz 11s"

    def __init__(self,n_sheets, n_wheels, mialage,car_type, drive_type):
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(n_sheets, n_wheels, mialage)

    def car_info(self):
        print(f"Car type: {self.car_type}")
        print(f"Drive type: {self.drive_type}")


class ElectricCar(Car):
    car_colour = "Pink"

    def __init__(self,n_sheets, n_wheels, mialage,car_type, drive_type,battery_capacity,distance_range):
        super().__init__(n_sheets, n_wheels, mialage,car_type, drive_type)
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
    

    def electric_car_info(self):
        print(f"Battery capacity of car: {self.battery_capacity}")
        print(f"Distance Range of car: {self.distance_range}")

ev = ElectricCar(7,4,30,"Sedan","Mnual","100 kwh","200KM")    

ev.vechile_info()   
ev.car_info()   
ev.electric_car_info()

print(ElectricCar.company)
print(ElectricCar.model_name)
print(ElectricCar.car_colour)