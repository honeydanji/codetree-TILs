n = input()

in_data = ["ee", "eb"]

ee = 0
eb = 0

for j in range(len(in_data)):
    for i in range(len(n)-1):
        if in_data[j] == n[i:i+2]:
            if j == 0:
                ee += 1
            else:
                eb += 1

print(ee,eb)