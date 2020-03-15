# Smallest multiple
from problem3 import largest_prime_factor

def smallest_multiple(n):
    """Calculates the smallest number that evenly divides all of 1, 2, ..., n"""
    result = 1
    for i in range(2, n+1):
        lpf = largest_prime_factor(i)
        if result % i != 0:
            result *= lpf
    return result

print("1-10:", smallest_multiple(10))
print("1-20:", smallest_multiple(20))
    