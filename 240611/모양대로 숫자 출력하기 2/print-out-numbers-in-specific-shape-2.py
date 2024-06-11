n = int(input())

a = 2

for i in range(n):
    for j in range(n):
        print(a, end=' ')
        if a == 8:
            a = 2
        else:
            a += 2
    print()