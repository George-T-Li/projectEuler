# Names scores
with open("problem22.txt", "r") as f:
    line = f.readline()
    names = line.split(",")

parsedNames = []
for name in names:
    parsedName = name.strip("\"")
    parsedNames.append(parsedName)

def char_score(c):
    """Returns the position of c in the alphabet"""
    return ord(c) - 64

sortedNames = sorted(parsedNames)
total = 0
for index, name in enumerate(sortedNames, start=1):
    sumOfName = 0
    for char in name:
        sumOfName += char_score(char)
    nameScore = sumOfName * index
    total += nameScore
print(total)