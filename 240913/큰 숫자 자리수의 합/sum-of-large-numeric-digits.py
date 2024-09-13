def total(n):

    if len(str(n)) == 1:
        return n

    return (n % 10) + total(n // 10)


a,b,c = map(int, input().split())
aa = a*b*c
print(total(aa))