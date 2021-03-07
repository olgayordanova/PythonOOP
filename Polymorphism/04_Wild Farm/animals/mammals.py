from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Food

class Mouse(Mammal):
    FOOD_INCREASE_FACTOR = 0.10
    def __init__(self,name, weight, wing_size):
        super ().__init__ ( name, weight, wing_size )

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Mouse.FOOD_INCREASE_FACTOR*food.quantity
        self.food_eaten += food.quantity

class Dog(Mammal):
    FOOD_INCREASE_FACTOR = 0.40
    def __init__(self,name, weight, wing_size):
        super ().__init__ ( name, weight, wing_size )

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Dog.FOOD_INCREASE_FACTOR*food.quantity
        self.food_eaten += food.quantity

class Cat(Mammal):
    FOOD_INCREASE_FACTOR = 0.30
    def __init__(self,name, weight, wing_size):
        super ().__init__ ( name, weight, wing_size )

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Cat.FOOD_INCREASE_FACTOR*food.quantity
        self.food_eaten += food.quantity

class Tiger(Mammal):
    FOOD_INCREASE_FACTOR = 1.00
    def __init__(self,name, weight, wing_size):
        super ().__init__ ( name, weight, wing_size )

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Tiger.FOOD_INCREASE_FACTOR*food.quantity
        self.food_eaten += food.quantity



