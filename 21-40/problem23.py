# Non-abundant sums
from problem21 import proper_divisors
"""
n is abundant if sum(proper_divisors(n)) > n
All integers > 28123 can be written as a sum of two abundant numbers
Goal is to find all the numbers that cannot be written as a sum of two abundant numbers
"""

"""
Steps:
1. Find sum(proper_divisors(n)) for all n < 28123.
2. Use 1 to generate a list of all abundant numbers.
3. Iterate over the list from 2 twice, to find all sums of two abundant numbers.
4. Use a loop from 1..28123 to check for all numbers that aren't in 3. Add them to a list.
5. The list from 4. is a list that meets the critera.
"""

limit = 28123
abundants = []
for i in range(1, limit):
    sumDivisors = sum(proper_divisors(i))
    if i < sumDivisors:
        abundants.append(i)

abundantsSums = []
for index, a in enumerate(abundants):
    for b in abundants[index:]:
        s = a + b
        if s < 28123:
            abundantsSums.append(s)
sortedSums = sorted(list(dict.fromkeys(abundantsSums)))

nonabundantSums = []
for i in range(1, limit):
    if i not in sortedSums:
        nonabundantSums.append(i)
print(len(nonabundantSums), sum(nonabundantSums))
