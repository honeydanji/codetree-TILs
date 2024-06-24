a, b = map(int, input().split())

arr = [[0 for _ in range(b)] for _ in range(a)]

num = 1
n = 0
m = 0
k = 0
l = 0
c = 0

while True:
    if num > a*b:
        break
    n = l
    m = k
    while True:
        arr[n][m] = num
        num += 1
        if m == c or n == a-1:
            if k < b-1:
                k += 1
            else:
                l += 1
                c += 1
            break
        else:
            n += 1
            m -= 1

    
for i in range(a):
    for j in range(b):
        print(arr[i][j], end=" ")
    print()