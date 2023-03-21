class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        print(f"{self.brand} is moving...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def drive(self):
        print(f"{self.brand} {self.model} is driving...")

class Plane(Vehicle):
    def __init__(self, brand, flight_number):
        super().__init__(brand)
        self.flight_number = flight_number
    
    def fly(self):
        print(f"{self.brand} Flight {self.flight_number} is flying...")

class FlyingCar(Car, Plane):
    def __init__(self, brand, model, flight_number):
        Car.__init__(self, brand, model)
        Plane.__init__(self, brand, flight_number)
    
    def fly_and_drive(self):
        print(f"{self.brand} {self.model} with Flight {self.flight_number} is flying and driving...")

my_flying_car = FlyingCar("Tesla", "Model S", "SQ345")
my_flying_car.move()  # Tesla is moving...
my_flying_car.drive()  # Tesla Model S is driving...
my_flying_car.fly()  # Tesla Flight SQ345 is flying...
my_flying_car.fly_and_drive()  # Tesla Model S with Flight SQ345 is flying and driving...
