# 1000-digit Fibonacci number

fPrev = 1
fThis = 1
fNext = 2
count = 3
while len(str(fNext)) < 1000:
    fPrev = fNext
    fNext = fThis + fNext
    fThis = fPrev
    count += 1

print(count)
