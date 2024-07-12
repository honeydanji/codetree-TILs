a,b = map(str, input().split())
a,b = list(a), list(b)

b[0:2] = a[0:2]

print("".join(map(str, b)))