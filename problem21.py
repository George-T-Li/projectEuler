# Amicable numbers
import math
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

Find the sum of all amicable numbers < 10000
"""
def proper_divisors(n):
    """Returns the list of all positive numbers less than n that divide evenly into n"""
    l = [1]
    if n == 1 or n == 2:
        return l
    else:
        limit = math.floor(n/2) + 1
        for i in range(2, limit):
            if n % i == 0:
                l.append(i)
        return l

#print(proper_divisors(220))
#print(proper_divisors(284))

def amicable_numbers(n):
    """Returns all amicable numbers < n"""
    amicables = []
    sumDivisors = {}
    for i in range(1, n):
        divisors = proper_divisors(i)
        sumDivisors[i] = sum(divisors)
    for i in range(1, n):
        sumDivisorsOfi = sumDivisors[i]
        if sumDivisorsOfi < n:
            compare = sumDivisors[sumDivisorsOfi]
            if compare == i and sumDivisorsOfi != i:
                amicables.append(i)
    return amicables

#print(sum(amicable_numbers(10000)))
