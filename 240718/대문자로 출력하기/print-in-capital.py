n = list(input())

for i in n:
    if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
        print(i.upper(), end="")