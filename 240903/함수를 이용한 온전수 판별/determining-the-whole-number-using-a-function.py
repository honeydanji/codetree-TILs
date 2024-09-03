def two(i):
    if i % 2 == 0:
        return False
    else:
        return True

def five(i):
    if str(i)[-1] == "5":
        return False
    else:
        return True

def three_and_nine(i):
    if i % 3 == 0 and i % 9 != 0:
        return False
    else:
        return True

a,b = map(int, input().split())
cnt = 0
for i in range(a,b+1):
    if two(i) and five(i) and three_and_nine(i):
        cnt += 1
print(cnt)


## 조건 반대로 입력