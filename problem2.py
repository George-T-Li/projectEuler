# Even Fibonacci numbers
def even_Fibonnaci_numbers(n):
    sum = 0
    f0 = 0
    f1 = 1
    prevFib = f1
    thisFib = f0 + f1

    while thisFib < n:
        if thisFib % 2 == 0:
            sum += thisFib
        nextFib = prevFib + thisFib
        prevFib = thisFib
        thisFib = nextFib
    return sum

print("4000000:", even_Fibonnaci_numbers(4000000))
