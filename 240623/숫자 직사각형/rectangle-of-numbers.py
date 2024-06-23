a, b = map(int, input().split())

j = 1

for i in range(a):
    for _ in range(b):
        print(j, end=" ")
        j+=1
    print()