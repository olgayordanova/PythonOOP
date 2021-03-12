class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.j<self.count:
            i =self.start
            self.start+=self.step
            self.j+=1
            return i
        else:
            raise StopIteration



numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)


