arr = list(map(int, input().split()))

brr = []

for i in arr:
    if i != 0:
        if i % 2 == 0:
            brr.append(round(i / 2))
        else:
            brr.append(i + 3)
    else:
        break

print(' '.join(map(str, brr)))