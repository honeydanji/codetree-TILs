def sequence_check(a_li, b_li, a, b):
    for i in range(0, a-b):
        if str(a_li[i:i+b]) == str(b_li):
            return True    
    return False

a,b = map(int, input().split())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

if sequence_check(a_li, b_li, a, b):
    print("Yes")
else:
    print("No")