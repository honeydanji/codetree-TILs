n = list(input())

for i in range(len(n)):
    if n[i] == "e":
        n.pop(i)
        break

print(''.join(map(str,n)))