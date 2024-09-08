n, m = map(int, input().split())
li = list(map(int, input().split()))

def test():
    global m
    cnt = 0
    while True:
        cnt += li[m-1]
        if m == 1:
            break
        if m % 2 == 0:
            m /= 2
            m = int(m)
        else:
            m -= 1

    return cnt

print(test())