a, b = map(str, input().split())
c = ""
d = ""
for i in a:
    if ord(i) >= 48 and ord(i) <= 57:
        c += i
    else:
        break

for i in b:
    if ord(i) >= 48 and ord(i) <= 57:
        d += i
    else:
        break

print(int(c)+int(d))