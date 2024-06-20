n = int(input())

count = 0
arr = []

for i in range(1, 11):
    if count == 2:
        break
    else:
        a = n * i
        arr.append(a)

    if a % 5 == 0:
        count += 1

print(' '.join(map(str, arr)))