def astar(n):
    if n == 0:
        return
    print("* "*n)
    astar(n-1)

def bstar(n):
    if n == 0:
        return
    bstar(n-1)
    print("* "*n)

n = int(input())
astar(n)
bstar(n)