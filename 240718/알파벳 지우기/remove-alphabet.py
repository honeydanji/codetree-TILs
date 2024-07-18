a = input()
b = input()
c = ''
d = ''

for i in a:
    if ord(i) >= 48 and ord(i) <= 57:
        c += i

for i in b:
    if ord(i) >= 48 and ord(i) <= 57:
        d += i

print(int(c)+int(d))