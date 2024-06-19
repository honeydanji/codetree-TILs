arr = list(map(int, input().split()))

count = 0

for i in arr:
    if i != 0:
        count+=1
    else:
        break

if count-3 == 0:
    print(sum(arr[count-1::-1]))    
else:
    print(sum(arr[count-1:count-3:-1]))