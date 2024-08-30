def n_squre(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            print(num, end=" ")
            num += 1
            if num == 10:
                num = 1
        print()


n = int(input())
n_squre(n)