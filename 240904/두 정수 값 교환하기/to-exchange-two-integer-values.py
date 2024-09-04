def change(a, b):
    a, b = b, a
    print(a,b)

a, b = map(int, input().split())
change(a,b)