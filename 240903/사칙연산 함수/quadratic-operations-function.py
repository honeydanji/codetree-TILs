def str_check(o):
    if o in ['+','-','/','*']:
        return True
    else:
        return False

def calculation(a,o,c):
    if o == '+':
        result = a + c
    elif o == '-':
        result = a - c
    elif o == '/':
        result = int(a / c)
    elif o == '*':
        result = a * c

    print(f"{a} {o} {c} = {result}")

a,o,c = map(str, input().split())
if str_check(o):
    calculation(int(a),o,int(c))
else:
    print("False")