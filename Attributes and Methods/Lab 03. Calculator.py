from functools import reduce

def operate (operation, *args):
    action_d = {
        "+": lambda a,b: a+b,
        "-": lambda a,b: a-b,
        "*": lambda a,b: a*b,
        "/": lambda a,b: a/b,
    }
    return reduce ( action_d[operation], args )

class Calculator:

    @staticmethod
    def add(*args):
        return operate("+", *args)

    @staticmethod
    def multiply(*args):
        return operate("*", *args)

    @staticmethod
    def divide(*args):
        return operate("/", *args)

    @staticmethod
    def subtract(*args):
        return operate("-", *args)

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))


# add(*args) – sums all the arguments passed to the function and returns the result
# multiply(*args) – multiplies all the numbers and returns the result
# divide(*args) – divides all the numbers and returns the result
# subtract(*args) – subtracts all the numbers and returns the result

# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("/", 3, 0))