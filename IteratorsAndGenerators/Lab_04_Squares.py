
# def squares (n):
#     for i in range (1, n+1):
#         yield i**2

squares = lambda n:(i**2 for i in range (1, n+1))

print(list(squares(5)))