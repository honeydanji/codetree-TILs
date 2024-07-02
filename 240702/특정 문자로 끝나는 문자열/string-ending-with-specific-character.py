arr = [input() for _ in range(10)]
n = input()
check = False

for a in arr:
    if a[-1] == n:
        print(a)
        check = True

if check == False:
    print(None)