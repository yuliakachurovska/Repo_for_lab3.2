def degree_of_five(numb):
    if numb <= 0:
        return False
    elif numb == 1:
        return True
    while numb % 5 == 0:
        numb /= 5
    return numb == 1


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)