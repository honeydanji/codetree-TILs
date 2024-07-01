n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    arr[i][0] = 1
    if i > 0:
        for j in range(1,i+1):
            if i > 0 and j > 0:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            break
        print(arr[i][j], end=" ")
    print()