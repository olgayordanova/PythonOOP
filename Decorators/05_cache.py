def cache(func):
    def wrapper(n):
        result = func(n)
        wrapper.log[n] = result
        return result
    wrapper.log = {}
    return wrapper

@cache
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)

