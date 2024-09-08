def n_aprint(n):
    if n==0:
        return
    n_aprint(n-1)
    print(n, end=' ')

def n_bprint(n):
    if n==0:
        return
    print(n, end=' ')
    n_bprint(n-1)


n = int(input())
n_aprint(n)
print()
n_bprint(n)