n = int(input())

a = 1
b = n

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(a, end='')
        else:
            print(b, end='')
            
    print()
    a += 1
    b -= 1