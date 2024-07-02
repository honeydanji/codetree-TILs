arr = input()
brr = []

count = 1

for i in range(1, len(arr)):
    if arr[i-1] == arr[i]:
        count += 1
    else:
        brr.append(arr[i-1])
        brr.append(str(count))
        count = 1

    if i == len(arr)-1:
        brr.append(arr[i])
        brr.append(str(count))

print(len(brr))
print(''.join(map(str, brr)))