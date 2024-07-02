n = int(input())
arr = [input() for _ in range(n)]
m = input()
count = 0
str_total = 0

for a in arr:
    if a[0] == m:
        count += 1
        str_total += len(a)

print(f"{count} {str_total/count:.2f}")