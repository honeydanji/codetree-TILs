n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

num = 1
check = 0

for i in range(n-1, -1, -1):
    if check % 2 == 0:
        for j in range(n-1, -1, -1):
            arr[j][i] = num
            num+=1
    else:
        for j in range(n):
            arr[j][i] = num
            num+=1
    check+=1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()