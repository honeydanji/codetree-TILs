a,b = map(int, input().split())

arr=[]
brr=[]

for i in range(2*a):
    if i < (2*a)/2:
        arr.append(list(map(int, input().split())))
    else:
        brr.append(list(map(int, input().split())))

for i in range(a):
    for j in range(b):
        if arr[i][j] == brr[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()