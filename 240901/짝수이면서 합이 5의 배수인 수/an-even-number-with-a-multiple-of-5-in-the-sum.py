def yes(n):
    total = 0
    if n % 2 == 0:
        for i in str(n):
            total += int(i)
        if total % 5 == 0:
            return True
        else:
            return False



n = int(input())
if yes(n):
    print("Yes")
else:
    print("No")