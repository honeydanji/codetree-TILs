def check(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


a,b = map(int, input().split())
total = 0
for i in range(a,b+1):
    if check(i) == True:
        total += i
print(total)