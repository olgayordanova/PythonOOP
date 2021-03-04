# from collections import defaultdict

class Pizza:

    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings ={}

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @property
    def toppings(self):
        return self.__toppings

    @name.setter
    def name(self, value):
        self.__name = value

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping):
        if topping.weight + self.calculate_total_weight() > self.toppings_capacity:
            raise ValueError ("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type]+=topping.weight
            return
        self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = sum([v for k,v in self.__toppings.items()])
        return total_weight


