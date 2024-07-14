n = list(input())

count = len(n)

while count != 1:
    a = int(input())
    if a < len(n):
        n.pop(a)
        print(''.join(map(str,n)))
    else:
        n.pop(len(n)-1)
        print(''.join(map(str,n)))
    count-=1