a, b = map(str, input().split())

check = False

for i in range(len(a)):
    if a[i] == b:
        print(i)
        check = True
        break
    
if check == False:
    print("No")