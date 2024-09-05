def palindrome(st):
    st = list(st)[::-1]
    return ''.join(map(str, st))

st = input()
if st == palindrome(st):
    print("Yes")
else:
    print("No")