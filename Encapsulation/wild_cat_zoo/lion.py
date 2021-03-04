class Lion:

    def __init__(self, name, gender, age):
        self.name=name
        self.gender = gender
        self.age = age
        self.__money_needs = 50

    # @property
    def get_needs(self):
        return self.__money_needs

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"