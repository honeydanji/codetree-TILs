n = int(input())

a = 1

for i in range(n):
    for j in range(n):
        print(a, end='')
        if a==9:
            a = 1
        else:
            a += 1
    print()