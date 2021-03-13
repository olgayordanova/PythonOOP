def number_increment(numbers):
    def increase():
        numbers_new = [el+1 for el in numbers]
        return numbers_new
    return increase()


print(number_increment([1, 2, 3]))