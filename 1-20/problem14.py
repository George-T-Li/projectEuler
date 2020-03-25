# Longest collatz sequence
def collatz(n, sequence = []):
    """Generates a collatz sequence starting with n"""
    sequence.append(n)
    if n == 1:
        return sequence
    if n % 2 == 0:
        next = int(n/2)
    else:
        next = 3*n + 1
    return collatz(next, sequence)

longestValue = 0
longestSequence = []
for i in range(1, 1000000):
    c = collatz(i, [])
    if len(c) > len(longestSequence):
        longestValue = i
        longestSequence = c
print(longestValue, longestSequence, len(longestSequence))
