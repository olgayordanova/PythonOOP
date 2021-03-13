def even_parameters(fn):
    def wrapper(*args):
        for i in args:
            a = i
            if not isinstance(a, int) or a%2!=0:
                return f"Please use only even numbers!"
        return fn ( *list(args ))
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

