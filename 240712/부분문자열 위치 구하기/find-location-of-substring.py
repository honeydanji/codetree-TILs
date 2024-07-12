al = input()
a = input()


check = False

for i in range(len(al)-1):
    if a == al[i:i+2]:
        print(i)
        check = True
        break

if check == False:
    print(-1)