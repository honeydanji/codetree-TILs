def test(n, a):
    for i in range(0, n):
        if a[i] < 0:
            a[i] *= -1


n = int(input())
a = list(map(int, input().split()))
test(n, a)
print(' '.join(map(str, a)))