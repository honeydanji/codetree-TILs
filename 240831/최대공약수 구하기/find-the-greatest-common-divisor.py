def max(a, b):
    check = True
    if a > b:
        num = a
    else:
        num = b
    while check:
        if a % num == 0 and b % num == 0:
            check = False
        else:
            num -= 1
    print(num)

a, b = map(int, input().split())
max(a,b)