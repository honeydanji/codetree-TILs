al = input()
a = input()


check = False

for i in range(len(al)-len(a)):
    if a == al[i:len(a)+i]:
        print(i)
        check = True
        break

if check == False:
    print(-1)