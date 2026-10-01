# Abstraction -> hiding the complex implementation details and
# showing only the necessary features of an object

from abc import ABC,abstractmethod

# Abstract base class

class Vehicle(ABC):
    def drive(self):
        print("vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("car engine started")

car = Car()
car.start_engine()

def operate_vehicle(obj):
    obj.start_engine()
    obj.drive()

operate_vehicle(car)


