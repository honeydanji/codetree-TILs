check = False


while check == False:
    n = input()

    if n == "END":
        check = True
    else:
        print(n[::-1])