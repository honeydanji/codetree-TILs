n = int(input())

a = 65

for i in range(1, n+1):
    for j in range(i):
        print(chr(a), end="")
        if chr(a)=="Z":
            a = 64
        a+=1
    print()