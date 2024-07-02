n = int(input())

total = 0
a_total = 0

for _ in range(n):
    a = input()
    total += len(a)
    if a[0] == "a":
        a_total += 1

print(f"{total} {a_total}")