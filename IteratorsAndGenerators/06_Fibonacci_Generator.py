def fibonacci():
    n0 = 0
    n1= 1
    while True:
        yield n0
        n0, n1 = n1, n0+n1



generator = fibonacci()
for i in range(10):
    print(next(generator))
