n = int(input())

arr = list(map(int, input().split()))
brr = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        brr.append(arr[i])

print(' '.join(map(str, brr[::-1])))