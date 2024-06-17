m = int(input())

for i in range(m):
    count = 0
    n = int(input())
    while 1:
        if n == 1:
            print(count)
            break;
        else:
            count += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = n * 3 + 1