n = int(input())

a = 0

for i in range(n):
    for j in range(n):
        if i > j:
            print(" ", end=" ")
        else:
            print(n-j, end=" ")
    print()