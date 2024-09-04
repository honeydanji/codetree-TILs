def check(m, d):
    if m >= 1 and m <= 12:
        if m == '2' and d >= 1 and d <= 28:
            return True
        else:
            return False

        if m % 2 == 0 and d >= 1 and d <= 30:
            return True
        elif m % 2 != 0 and d >= 1 and d <= 31:
            return True
    else:
        return False


m,d = map(int, input().split())
if check(m, d):
    print("Yes")
else:
    print("No")