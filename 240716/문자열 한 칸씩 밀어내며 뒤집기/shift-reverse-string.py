st, n = map(str, input().split())

for i in range(1,int(n)+1):
    m = int(input())
    if m == 1:
        st = st[1:] + st[0]
        print(st)
    elif m == 2:
        st = st[-1] + st[:len(st)-1]
        print(st)
    elif m == 3:
        st = st[::-1]
        print(st)