# Largest prime factor
import math

def largest_prime_factor(n):
    limit = math.floor(math.sqrt(n))

    for i in range(2, limit+1):
        if n % i == 0:
            quo = int(n / i)
            return largest_prime_factor(quo)
    return n

print("13195:", largest_prime_factor(13195))
print("600851475143:", largest_prime_factor(600851475143))
