def test(n):
    if len(str(n)) == 1:
        return n**2
    return test(n // 10) + (n % 10)**2

n = int(input())
print(test(n))