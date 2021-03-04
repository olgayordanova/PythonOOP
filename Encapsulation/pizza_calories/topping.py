class Topping:

    def __init__( self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @property
    def weight(self):
        return self.__weight

    @topping_type.setter
    def topping_type(self, value):
        self.__topping_type = value

    @weight.setter
    def weight(self, value):
        self.__weight = value

