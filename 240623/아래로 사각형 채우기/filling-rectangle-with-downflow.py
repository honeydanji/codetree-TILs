n = int(input())

for i in range(1,n+1):
    for j in range(0, n*n, n):
        print(i+j, end=" ")
    print()