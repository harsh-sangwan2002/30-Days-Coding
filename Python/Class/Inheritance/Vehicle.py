class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Starting engine...")
        
class Car(Vehicle):
    def __init__(self,make,model,year,numDoors):
        super().__init__(make,model,year)
        self.numDoors = numDoors
        
    def drive(self):
        print("Driving the car...")
        
vehicle = Vehicle("Toyota","Corolla",2022)
car = Car("Tesla","Model S",2021,4)

vehicle.start_engine()
car.start_engine()
car.drive()