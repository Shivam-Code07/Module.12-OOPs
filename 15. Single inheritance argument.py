

class Vechile:
    company = 'TATA Moters'
    def __init__(self, n_sheets, n_wheels, mialage):
        self.n_sheets = n_sheets
        self.n_wheels = n_wheels
        self.mialage = mialage

    def get_vechile_details(self):
        print(f"Number of Sheets: {self.n_sheets}")
        print(f"Number of Wheels: {self.n_wheels}")
        print(f"Vechile Mialage: {self.mialage}")

class Car(Vechile):
    model_name = "Mercedes Benz 11s"
    def __init__(self,car_type, drive_type, n_sheets, n_wheels, mialage):
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(n_sheets, n_wheels, mialage)

c1 = Car("manual", "electric",7,4,25)
print(c1.car_type)
print(c1.drive_type)
print(c1.n_sheets)
print(c1.n_wheels)
print(c1.mialage)

c1.get_vechile_details()