a, b = map(int, input().split())

print(a,b, end=" ")
for _ in range(3, 11):
    c = a + b
    print(c % 10, end=" ")
    a = b
    b = c