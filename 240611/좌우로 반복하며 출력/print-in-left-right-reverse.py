n = int(input())

a = 1
b = n

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(a, end='')
            a += 1
        else:
            print(b, end='')
            b -= 1
    a = 1
    b = n
    print()