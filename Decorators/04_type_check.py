def type_check(typ):
    def decorator(function):
        def wrapper(*args):
            if not isinstance(*args, typ):
                return "Bad Type"
            return function ( *args)
        return wrapper
    return decorator



@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
