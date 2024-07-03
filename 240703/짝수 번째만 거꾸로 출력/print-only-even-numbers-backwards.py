arr = input()

for i in range(len(arr)-1, -1, -1):
    if (i+1) % 2 == 0:
        print(arr[i], end="")