n = int(input())

for i in range(n):
    for j in range(n):
        print(chr(65+j+i), end="")
    print()