# Largest palindrome product
def is_palindrome(s):
    forwardString = str(s)
    reversed = forwardString[::-1]
    return forwardString==reversed

def largest_palindrome_product(n):
    """Calculates the largest palindrome that is a product of two n-digit numbers"""
    lowest = 10**(n-1)
    highest = 10**n
    largest = -1
    for i in range(lowest, highest):
        for j in range(i, highest):
            product = i*j
            if is_palindrome(product):
                if product > largest:
                    largest = product
                    x = i
                    y = j
    return largest, x, y

print("2-digit:", largest_palindrome_product(2))
print("3-digit:", largest_palindrome_product(3))
