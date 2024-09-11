def sum(n):

    if n <= 0:
        return 0

    if n % 2 == 0:  ## 짝수
        temp = n + sum(n-2)
        return temp 
    else:           ## 홀수
        temp = n + sum(n-2)
        return temp 

n = int(input())
print(sum(n))