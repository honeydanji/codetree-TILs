n = int(input())

a = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if j > a:
            if j == n:
                print(f"{i} * {j-a} = {i*(j-a)}", end="")
            else:
                print(f"{i} * {j-a} = {i*(j-a)}", end=" / ")
        
    print()
    a += 1