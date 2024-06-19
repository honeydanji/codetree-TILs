arr = list(map(int, input().split()))

brr = arr[0::2]
crr = arr[1::2]

if sum(brr) > sum(crr):
    print(sum(brr) - sum(crr))
else:
    print(sum(crr) - sum(brr))