# Special Pythagorean triplet
"""
Constraint 1: a**2 + b**2 = c**2
Constraint 2: a + b + c = 1000
=> 500000 = 1000a + 1000b - ab
"""

for a in range(1, 999):
    for b in range(a, 999):
        if a + b > 1000:
            break
        compare = 1000*a + 1000*b - a*b
        if compare == 500000:
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a, b, c, a*b*c)