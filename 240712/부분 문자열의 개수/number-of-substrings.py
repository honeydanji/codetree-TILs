aa = input()
a = input()

a_count = 0

for i in range(len(aa)-len(a)+1):
    if a == aa[i:i+len(a)]:
        a_count += 1
        

print(a_count)