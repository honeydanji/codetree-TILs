def minority(i):
    for j in range(2, i):
        if i % j != 0:
            continue
        else:
            return False
    return True

def total_even_number(i):
    total = 0
    for j in str(i):
        total += int(j)
    
    if total % 2 == 0:
        return True
    else:
        return False


a,b = map(int, input().split())
cnt = 0
for i in range(a,b+1):
    if minority(i) and total_even_number(i):
        cnt += 1

print(cnt)