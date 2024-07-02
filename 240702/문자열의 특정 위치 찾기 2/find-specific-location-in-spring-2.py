n = input()

arr = [ "apple", "banana", "grape", "blueberry", "orange"]

count = 0

for a in arr:
    if a[2] == n or a[3] == n:
        print(a)
        count += 1

print(count)