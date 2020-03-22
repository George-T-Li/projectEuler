# Factorial digit sum
def factorial(n):
    """Computes n!"""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def factorial_digit_sum(n):
    """Computes the sum of the digits in n!"""
    sum = 0
    factStr = str(factorial(n))
    for digit in factStr:
        sum += int(digit)
    return sum

#print(factorial_digit_sum(10))
#print(factorial_digit_sum(100))
