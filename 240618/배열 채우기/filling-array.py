arr = list(map(int, input().split()))

index = 0

for i in arr:
    if i != 0:
        index += 1

print(' '.join(map(str,arr[index-1::-1])))