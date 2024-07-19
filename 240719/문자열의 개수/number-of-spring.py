count = 0
check = False
nn = []

while check == False:
    n = input()

    if n == "0":
        check = True
    else:
        count += 1
        if count % 2 == 0:
            continue
        nn.append(n)

print(count)
for i in nn:
    print(i)