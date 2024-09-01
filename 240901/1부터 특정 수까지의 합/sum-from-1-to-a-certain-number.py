def sum(n):
    count = 0

    for i in range(1,n+1):
        count = count + i

    return count//10

n = int(input())
print(sum(n))