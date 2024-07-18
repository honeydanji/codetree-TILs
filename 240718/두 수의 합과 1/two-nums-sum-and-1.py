a,b = map(int, input().split())

n = list(str(a+b))

count = 0

for i in n:
    if i == "1":
        count += 1

print(count)