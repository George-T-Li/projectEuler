# 10001st prime
from problem3 import largest_prime_factor
def is_prime(n):
    """Returns 'true' if n is prime, otherwise 'false'"""
    lpf = largest_prime_factor(n)
    return n == lpf

def nth_prime(n):
    """Returns the nth prime number (2 is the first prime)"""
    counter = 1
    numberToCheck = 2
    while counter < n:
        numberToCheck += 1
        if is_prime(numberToCheck):
            counter += 1
    return numberToCheck

#print("6th:", nth_prime(6))
#print("10001st:", nth_prime(10001))
