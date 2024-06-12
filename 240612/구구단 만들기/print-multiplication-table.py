a,b = map(int, input().split())
c = b

for i in range(1, 10):
    stop = True
    while stop:
        if b != a:
            print(f"{b} * {i} = {b*i}", end=" / ")
            b -= 2
        else:
            print(f"{b} * {i} = {b*i}", end="")
            b -= 2
        if b < a:
            stop = False
            b = c
    print()