arr = []

for _ in range(3):
    a = input()
    arr.append(len(a))

arr.sort()

print(arr[2]-arr[0])