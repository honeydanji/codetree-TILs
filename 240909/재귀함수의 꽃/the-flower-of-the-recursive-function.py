def a_print(n):
    if n == 0:
        return
    print(n, end=" ")
    a_print(n-1)

def b_print(n):
    if n == 0:
        return
    b_print(n-1)
    print(n, end=" ")

n = int(input())
a_print(n)
b_print(n)