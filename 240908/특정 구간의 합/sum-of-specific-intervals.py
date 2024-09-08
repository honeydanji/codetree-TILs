n,m = map(int, input().split())
A = list(map(int, input().split()))
a = []
for _ in range(m):
    a.append(list(map(int, input().split()))) 
    

def test():
    global A
    for i in range(m):
        sum = 0
        for j in range(a[i][0], a[i][1]+1): # 2,3,4
            sum += A[j-1]
        print(sum)

test()