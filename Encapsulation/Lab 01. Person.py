class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name (self):
        return self.__name

    def get_age(self):
        return self.__age

person = Person("George", 32)
print(person.get_name())
print(person.get_age())


# class Person:
#     def __init__(self, age=0):
#         self.age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age < 18:
#             self.__age = 18
#         else:
#             self.__age = age
#
#
# person = Person(25)
# print(person.age)	# 25
# person.age = 10
# print(person.age)	# 18

