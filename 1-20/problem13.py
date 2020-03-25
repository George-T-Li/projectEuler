# Large sum
with open("problem13.txt", "r") as f:
    sum = 0
    for line in f:
        sum += int(line)
    print(sum)
f.close()

#5537376230390876637302048746832985971773659831892672
