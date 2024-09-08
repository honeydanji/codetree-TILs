def check(st):
    for i in range(0, len(st)-1):
        if st[i] == st[i+1]:
            continue
        else:
            return True
    return False

st = input()
if check(st):
    print("Yes")
else:
    print("No")