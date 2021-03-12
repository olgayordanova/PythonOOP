import itertools

def possible_permutations(nums):
    l=list(itertools.permutations(nums))
    for el in l:
        yield list(el)

[print(n) for n in possible_permutations([1, 2, 3])]