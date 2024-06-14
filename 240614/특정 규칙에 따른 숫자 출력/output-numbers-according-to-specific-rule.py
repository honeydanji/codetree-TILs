n = int(input())

a = 1


for i in range(n):
    for j in range(n):
        if j >= i:
            print(a, end=" ")
            a += 1
        else:
            print(" ", end=" ")

        if a == 10:
            a = 1
    print()