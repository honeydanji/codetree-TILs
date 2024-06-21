arr = []


for _ in range(4):
    brr = list(map(int, input().split()))
    arr.append(brr)
        

sum = 0

for i in range(1, 5):
    for j in range(i):
        sum += arr[i-1][j]


print(sum)