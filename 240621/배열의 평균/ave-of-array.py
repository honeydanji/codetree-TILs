arr = []
avg_width = []
avg_height = []
avg_all = []

sum_height = [0,0,0,0]
sum_all = 0

for _ in range(2):
    brr = list(map(int, input().split()))
    arr.append(brr)

for i in range(len(arr)):
    avg_width.append(round(sum(arr[i]) / len(arr[i]), 1))
    for j in range(len(arr[i])):
        sum_height[j] += arr[i][j]
        sum_all += arr[i][j]

for i in range(len(sum_height)):
    avg_height.append(round(sum_height[i] / 2, 1))


print(' '.join(map(str, avg_width)))
print(' '.join(map(str, avg_height)))
print(round(sum_all / 8, 1))