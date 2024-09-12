def mx(n, n_li):

    if n == 1:
        return n_li[0]

    if n_li[n-1] > n_li[n-2]:
        n_li[n-2] = n_li[n-1]
    return mx(n-1, n_li) 

n = int(input())
n_li = list(map(int, input().split()))
print(mx(n, n_li))