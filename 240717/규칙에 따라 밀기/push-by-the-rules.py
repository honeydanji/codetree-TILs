n = input()
co = input()

for i in range(len(co)):
    if co[i] == "L":
        n = n[1:len(n)] + n[0]
    else:
        n = n[-1] + n[:-1]

print(n)