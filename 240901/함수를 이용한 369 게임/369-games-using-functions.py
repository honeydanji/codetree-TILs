def three(i):
    if i % 3 == 0:
        return True


def check(i):
    if "3" in str(i) or "6" in str(i) or "9" in str(i) or three(i):
        return True


a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if check(i):
        cnt += 1
print(cnt)