class sequence_repeat:

    def __init__(self, string, num):
        self.string = string
        self.num=num
        self.i = 0
        self.j =0

    def __iter__(self):
        return self

    def __next__(self):
        while self.j < self.num:
            if self.i < len(self.string):
                ch = self.string[self.i]
                self.i+=1
                self.j += 1
                return ch
            else:
                self.i = 0
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
print(' ')
result = sequence_repeat('abc', 8)
for item in result:
    print(item, end ='')
