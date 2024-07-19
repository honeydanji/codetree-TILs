a = input()
b = input()
count = 0


for i in range(len(a)):
    count += 1
    a = a[-1] + a[:len(a)-1]

    if a == b:
        break

if count == 0:
    print(-1)
else:
    print(count)