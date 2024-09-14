count = 0

def test(n):
    global count

    if n == 1:
        return count

    if n % 2 == 0:
        count += 1
        return test(int(n / 2))
    else:
        count += 1
        return test(n * 3 + 1)


n = int(input())
print(test(n))