def make_bold(fn):
    def wrapper(*args):
        return f'<b>{fn(*args)}</b>'
    return wrapper

def make_italic(fn):
    def wrapper(*args):
        return f'<i>{fn(*args)}</i>'
    return wrapper

def make_underline(fn):
    def wrapper(*args):
        return f'<u>{fn(*args)}</u>'
    return wrapper



@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
