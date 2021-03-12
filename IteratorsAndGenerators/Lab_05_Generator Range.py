# genrange = lambda n1, n2 :(i for i in range (n1, n2+1))

#
# def genrange(n1, n2):
#     i = n1
#     while i <=n2:
#         yield i
#         i+=1

genrange = lambda n1, n2 :range (n1, n2+1)

print(list(genrange(1, 10)))