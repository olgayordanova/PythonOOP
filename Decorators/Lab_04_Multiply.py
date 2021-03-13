# def multiply(times):
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             res = function ( *args, **kwargs )
#             filtered = res*times
#             return filtered
#         return wrapper
#     return decorator

multiply = lambda times: lambda function: lambda *args, **kwargs: function ( *args, **kwargs )*times
@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

