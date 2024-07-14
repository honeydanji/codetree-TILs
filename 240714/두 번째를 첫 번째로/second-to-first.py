n = list(input())
a, b = n[1], n[0]

for i in range(len(n)):
    if n[i] == a:
        n[i] = b

print("".join(map(str, n)))