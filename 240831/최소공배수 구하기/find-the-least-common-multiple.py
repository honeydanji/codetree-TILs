def min(a, b):
    num_a = 1
    num_b = 1
    tem_a = a
    tem_b = b
    answer = 0

    while a != b:
        if a < b:
            a = tem_a*num_a
            num_a += 1
        else:
            b = tem_b*num_b
            num_b += 1
        if a > b:
            answer = a
        else:
            answer = b
    print(answer)
    
        

a,b = map(int, input().split())
min(a,b)