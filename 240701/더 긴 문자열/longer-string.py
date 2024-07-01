a, b = map(str, input().split())

if len(a) > len(b):
    print(f"{a} {len(a)}")
else:
    print(f"{b} {len(b)}")