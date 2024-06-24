a, b = tuple(map(int, input().split()))

arr = [[0 for _ in range(b)] for _ in range(a)]

num = 1

for diag in range(a + b - 1):
    if diag < b:
        x = 0
        y = diag
    else:
        x = diag - b + 1
        y = b - 1
    
    while x < a and y >= 0:
        arr[x][y] = num
        num += 1
        x += 1
        y -= 1

for i in range(a):
    for j in range(b):
        print(arr[i][j], end=" ")
    print()