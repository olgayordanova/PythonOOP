from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Food

class Owl(Bird):
    FOOD_INCREASE_FACTOR = 0.25
    def __init__(self,name, weight, wing_size):
        super ().__init__ ( name, weight, wing_size )

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Owl.FOOD_INCREASE_FACTOR*food.quantity
        self.food_eaten += food.quantity



class Hen(Bird):
    FOOD_INCREASE_FACTOR = 0.35
    def __init__(self,name, weight, wing_size):
        super ().__init__ ( name, weight, wing_size )

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += Hen.FOOD_INCREASE_FACTOR*food.quantity
        self.food_eaten += food.quantity



# Hens eat everything
# Mice eat vegetables and fruits
# Cats eat vegetables and meat
# Tigers, Dogs and Owls eat only meat
