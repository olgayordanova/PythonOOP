def is_prime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

def get_primes(n):
    for i in n:
        if is_prime(i):
            yield i



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
