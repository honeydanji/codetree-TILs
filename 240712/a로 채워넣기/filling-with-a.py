n = list(input())

n[1] = "a"
n[len(n)-2] = "a"

print("".join(map(str, n)))