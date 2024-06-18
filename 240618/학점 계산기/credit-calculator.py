n = int(input())

arr = list(map(float, input().split()))

avg = round(sum(arr) / len(arr), 1)

print(avg)
grade = "Perfect" if avg >= 4.0  else "Good" if avg >= 3.0 else "Poor"
print(grade)