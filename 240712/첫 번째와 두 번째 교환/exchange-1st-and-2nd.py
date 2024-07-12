n = list(input())

a, b = n[0], n[1]

for i in range(len(n)):
    if a == n[i]:
        n[i] = b
        continue

    if b == n[i]:
        n[i] = a
        continue

print(''.join(map(str, n)))