n = int(input())

for i in range(n):
    for j in range(n):
        if (11+(j+i)*2) % 2 != 0:
            print(11+(j+i)*2,end=' ')
    print()