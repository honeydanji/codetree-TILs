n = int(input())

a = 0
b = n 


for i in range(n):
    for j in range(1, n+1):
        if i % 2 == 0:
            a += 1
            print(a, end=' ')
            if j == n:
                b = a + j
        else:
            print(b, end=' ')
            b -= 1
            if j == n:
                a = b + j
    print()