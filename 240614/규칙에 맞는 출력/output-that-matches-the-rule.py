n = int(input())

a=0

for i in range(n):
    for j in range(n):
        if i >= j:
            print(n-i+a, end=" ")
            a += 1
        else:
            print(" ", end=" ")
    a = 0
    print()