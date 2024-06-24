n, m = tuple(map(int, input().split()))

answer = [[0 for _ in range(m)] for _ in range(n)]


count = 0

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            answer[j][i] = count
            count+=1
    else:
        for j in range(n-1, -1, -1):
            answer[j][i] = count
            count+=1

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()