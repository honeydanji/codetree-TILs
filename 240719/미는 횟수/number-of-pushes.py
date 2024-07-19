a = input()
b = input()
count = 0
check = False

for i in range(len(a)-1):
    count += 1
    a = a[-1] + a[:len(a)-1]

    if a == b:
        check = True
        break

if check == False:
    print(-1)
else:
    print(count)