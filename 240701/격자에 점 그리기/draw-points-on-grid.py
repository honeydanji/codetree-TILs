n, m = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]

count = 1

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = count
    count += 1

for i in range(len(arr)):
    print(' '.join(map(str, arr[i])))