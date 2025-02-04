from functools import lru_cache

def fibo1(n):
    # if n == 39
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibo1(n-1) + fibo1(n-2)

@lru_cache
def fibo2(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibo2(n - 1) + fibo2(n - 2)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

def is_prime_bad(n):
    if n < 2:
        return False
    for i in range(2, n):  # Goes up to n-1
        if n % i == 0:
            return False
    return True

import math

def is_prime_good(n):
    if n < 2:
        return False
    if n in (2, 3):  # Directly return for small prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # Eliminate even numbers and multiples of 3 early
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 2):  # Check odd numbers only
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(fibo2(990))
    fibo2.cache_clear()