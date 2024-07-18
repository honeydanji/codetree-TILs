n = list(input())

for i in n:
    if ord(i) >= 65 and ord(i) <= 122:
        print(i.upper(), end="")