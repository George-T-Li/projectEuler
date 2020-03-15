# Multiples of 3 and 5
def multiples_of_3_and_5(n):
    sum = 0

    for i in range(1, n):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum

print("1000:", multiples_of_3_and_5(1000))
