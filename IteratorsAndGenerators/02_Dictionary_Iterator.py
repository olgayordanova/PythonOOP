class dictionary_iter:

    def __init__(self, dictionary ):
        self.dictionary = dictionary
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <len(self.dictionary):
            key = list ( self.dictionary.keys () )[self.i]
            value =self.dictionary[key]
            self.i+=1
            return  key, value
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
