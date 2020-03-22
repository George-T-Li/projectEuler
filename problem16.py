# Power digit sum
def sum_digits(base, exp):
    n = str(base**exp)
    sum = 0
    for digit in n:
        sum += int(digit)
    return sum

#print("2**15:", sum_digits(2, 15))
#print("2**1000:", sum_digits(2, 1000))
    