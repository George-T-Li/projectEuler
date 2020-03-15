# Sum squares difference
def sum_squares_difference(n):
    """calculates the difference between (1**2 + 2**2 + ... + n**2) and (1 + 2 + ... + n)**2"""
    sumOfSquares = 0
    sumThenSquared = 0
    for i in range(1, n+1):
        sumOfSquares += i**2
        sumThenSquared += i
    sumThenSquared = sumThenSquared**2
    return sumThenSquared - sumOfSquares

print("1-10:", sum_squares_difference(10))
print("1-100:", sum_squares_difference(100))
