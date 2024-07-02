arr = input()
brr = []

count = 1

if len(arr) > 0:
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

else:
    brr.append(arr[0])
    brr.append(2)

print(len(brr))
print(''.join(map(str, brr)))