from abc import ABC, abstractmethod

class Vehicle( ABC ):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive (self,distance ):
        pass

    @abstractmethod
    def refuel (self, fuel):
        pass


class Car (Vehicle):
    INCREASING_SUMMER_FACTOR = 0.9

    def fuel_needs(self,distance):
        needs = (self.fuel_consumption +Car.INCREASING_SUMMER_FACTOR)*distance
        return needs

    def drive(self,distance):
        fuel_needs = self.fuel_needs(distance)
        if self.fuel_quantity >= fuel_needs:
             self.fuel_quantity -= fuel_needs
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity+=fuel
        return self.fuel_quantity


class Truck(Vehicle):
    INCREASING_SUMMER_FACTOR = 1.6
    KEPT_PERC = 0.95

    def fuel_needs(self,distance):
        needs = (self.fuel_consumption +Truck.INCREASING_SUMMER_FACTOR)*distance
        return needs

    def drive(self, distance) :
        fuel_needs = self.fuel_needs(distance)
        if self.fuel_quantity >= fuel_needs:
             self.fuel_quantity -= fuel_needs
        return self.fuel_quantity

    def refuel(self, fuel) :
        self.fuel_quantity+=fuel*Truck.KEPT_PERC
        return self.fuel_quantity

# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
