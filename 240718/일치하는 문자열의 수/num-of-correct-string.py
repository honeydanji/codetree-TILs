a , n = map(str, input().split())

count = 0

for i in range(int(a)):
    b = input()
    if n == b:
        count += 1

print(count)