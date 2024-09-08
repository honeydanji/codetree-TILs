st = input()
a = input()

def test():
    for i in range(0, len(st)-len(a)+1):
        if a == str(st[i:i+2]):
            return i
    return -1
            

i = test()
print(i)