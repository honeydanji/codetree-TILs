s, e = map(int, input().split())

total = 0

for i in range(s, e+1):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j

    if sum == i:
        total += 1

print(total)