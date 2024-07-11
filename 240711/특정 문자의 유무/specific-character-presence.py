n = input()

s = ["ee", "ab"]

answer = ["No", "No"]

for j in range(len(s)):
    for i in range(len(n)-1):
        if s[j] == n[i:i+2]:
            if j == 0:
                answer[j] = "Yes"
                break
            elif j == 1:
                answer[j] = "Yes"
                break

print(' '.join(map(str, answer)))