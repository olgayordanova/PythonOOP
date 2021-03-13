import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper

@measure_time
def fibonachi(n):
    def fib_wraper(n):
        if n==0:
            return 0
        if n==1:
            return 1
        return fib_wraper(n-1)+fib_wraper(n-2)
    return fib_wraper(n)


fibonachi(35)


# import time
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return result
#     return wrapper
#
# @measure_time
# def fibonachi(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonachi(n-1)+fibonachi(n-2)
#
# fibonachi(15)