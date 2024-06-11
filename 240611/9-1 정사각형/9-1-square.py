n = int(input())

a = 9

for i in range(n):
    for j in range(n):
        print(a, end='')
        if a < 2:
            a = 9
        else:
            a -= 1
    print()