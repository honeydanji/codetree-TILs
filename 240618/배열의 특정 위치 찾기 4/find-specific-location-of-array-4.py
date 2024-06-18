arr = list(map(int, input().split()))

count = 0
sum = 0

for i in arr:
    if i != 0:
        if i % 2 == 0:
            sum += i
            count += 1
    else:
        break

print(f"{count} {sum}")