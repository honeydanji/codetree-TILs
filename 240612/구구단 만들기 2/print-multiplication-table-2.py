a, b = map(int, input().split())
c = b

for i in range(1, 5):
    stop = True
    while stop:
        if b > a:
            print(f"{b} * {i*2} = {b * (i*2)}", end=' / ')
            b -= 1
        else:
            print(f"{b} * {i*2} = {b * (i*2)}")
            stop = False
            b = c