def divide(n, a):
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = int(a[i]/2)

n = int(input())
a = list(map(int, input().split()))
divide(n, a)
print(' '.join(map(str, a)))