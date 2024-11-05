from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, make):
        self.brand = brand
        self.make = make

    @abstractmethod
    def printReg(self, regNo):
        pass

    def display_vehicle(self):
        print(self.brand, self.make)

class Toyota(Vehicle):
    def __init__(self, brand, make, speed, year):
        super().__init__(brand, make)
        self.speed = speed
        self.year = year

    def display_toyota(self):
        return f"{self.brand} {self.make} {self.speed} {self.year}"

    def printReg(self, regNo):
        return f"{regNo}"

car1 = Toyota('Camry', 'Toyota', '550', '2021')
print(car1.display_toyota())
print(car1.display_vehicle())
print(car1.printReg("KBU  162C"))