a = list(input())
b = list(input())

check = True

while check == True:
    check = False
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            check = True
            a = a[0:i] + a[i+len(b):len(a)+1]
            
        
print(''.join(map(str, a)))