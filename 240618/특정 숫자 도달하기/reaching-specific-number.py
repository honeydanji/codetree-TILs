arr = list(map(int, input().split()))

sum = 0
avg = 0
count = 0

for i in arr:
    if i < 250:
        sum += i
        count += 1
    else:
        break

avg = round(sum / count, 2)

print(f"{sum} {avg}")