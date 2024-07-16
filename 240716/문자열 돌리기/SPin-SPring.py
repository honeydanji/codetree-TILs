n = input()
n_len = len(n)

print(n)
for _ in range(n_len):
    n = n[-1] + n[:-1]
    print(n)