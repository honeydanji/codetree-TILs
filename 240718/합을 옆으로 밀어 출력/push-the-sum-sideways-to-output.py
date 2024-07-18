n = int(input())

total = 0

for _ in range(n):
    a = int(input())
    total += a

total = str(total)

print(total[1:] + total[0])