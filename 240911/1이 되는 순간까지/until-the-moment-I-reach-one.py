cnt = 0

def test(n):
    global cnt

    if n == 1:
        return cnt

    if n % 2 == 0:
        temp = n // 2
        cnt += 1
        return test(temp)
    else:
        temp = n // 3
        cnt += 1
        return test(temp)


n = int(input())
print(test(n))