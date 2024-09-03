def check(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        return True
    else:
        return False

y = int(input())
if check(y):
    print("true")
else:
    print("false")