arr = list(map(int, input().split()))

sum = 0
count = 0

for i in arr:
    if i != 0:
        sum += i
        count += 1
    else:
        break

print(f"{sum} {round(sum/(count),1)}")