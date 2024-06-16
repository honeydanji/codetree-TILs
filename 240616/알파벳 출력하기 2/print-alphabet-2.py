n = int(input())

a = 65

for i in range(n):
    for j in range(n):
        if j < i:
            print(" ", end=" ")
        else:
            print(chr(a), end=" ")
            a+=1

        if chr(a-1)=="Z":
            a=65

        
    print()