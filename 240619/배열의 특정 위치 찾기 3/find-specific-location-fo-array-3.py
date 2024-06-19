arr = list(map(int, input().split()))

count = 0

for i in arr:
    if i != 0:
        count+=1
    else:
        break

print(sum(arr[count-3:count:1]))