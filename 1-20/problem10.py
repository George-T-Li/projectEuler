# Summation of primes
from problem7 import is_prime

def sum_of_primes(n):
    """Calculates the sum of primes < n"""
    total = 0
    for i in range (2, n):
        if is_prime(i):
            total += i
    return total

#print("10:", sum_of_primes(10))
#print("2000000:", sum_of_primes(2000000))
