def test(a,b):
    if a > b:
        b += 10
        a *= 2
        return a,b
    else:
        a += 10
        b *= 2
        return a,b

a,b = map(int, input().split())
a,b = test(a,b)
print(a,b)