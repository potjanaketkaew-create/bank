class Car:
    def __init__(self, model):
        self.model = model
        self.__mileage = 0 

    def drive(self):
        print(f"{self.model} is driving!")

    def read_mileage(self):
        print(f"This car has {self.__mileage} miles on it.")

    def update_mileage(self, new_miles):
        if new_miles >= self.__mileage:
            self.__mileage = new_miles
        else:
            print("Error: You can't roll back mileage!")


    def make_sound(self):
        print("Beep Beep!")


class ElectricCar(Car):
    def __init__(self, model, battery_size):
        super().__init__(model)
        self.battery_size = battery_size

    def charge(self):
        print(f"The {self.battery_size}kWh battery is charging...")

 
    def make_sound(self):
        print("Silent Hum...")


class Truck(Car):
    def make_sound(self):
        print("HONK HONK!")


print("--- Testing Inheritance & Encapsulation ---")
my_ev = ElectricCar("Tesla Model 3", 75)
my_ev.drive()
my_ev.charge()
my_ev.update_mileage(150)
my_ev.read_mileage()
my_ev.update_mileage(100) 

print("\n--- Testing Polymorphism ---")
garage = [Car("Toyota"), ElectricCar("BYD", 60), Truck("Volvo")]

for vehicle in garage:
    print(f"{vehicle.model}: ", end="")
    vehicle.make_sound()