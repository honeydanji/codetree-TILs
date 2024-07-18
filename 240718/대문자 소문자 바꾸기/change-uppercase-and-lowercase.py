n = list(input())

for i in n:
    if ord(i) >= 65 and ord(i) <= 90:
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')