arr = list(map(int, input().split()))

brr = arr[1::2]
crr = arr[2::3]

print(f"{sum(brr)} {round(sum(crr)/len(crr),1)}")