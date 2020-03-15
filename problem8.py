# Largest product in a series
def largest_n_adjacent_product(fname, n):
    """Determines the largest product of n adjacent digits of the number stored in fname"""
    with open(fname, "r") as f:
        s = ""
        for line in f:
            s += line[:-1]
    f.close()
        
    largest = 0
    for i in range(1000 - (n-1)):
        adj_n = s[i:i+n]
        product = 1
        for j in adj_n:
            product *= int(j)
        if product > largest:
            largest = product
    return largest

print("adjacent 4:", largest_n_adjacent_product("problem8.txt", 4))
print("adjacent 13:", largest_n_adjacent_product("problem8.txt",13))
