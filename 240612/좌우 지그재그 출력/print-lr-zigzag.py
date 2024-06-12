n = int(input())

a = 1
b = n 


for i in range(n):
    for j in range(1, n+1):
        if i % 2 == 0:
            print(a, end=' ')
            a += 1
            if j == n:
                b += j
        else:
            print(b, end=' ')
            b -= 1
            if j == n:
                a += n
    print()