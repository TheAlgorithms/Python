# secret code generator :
str1 = "axz"
str2 = "byz"


def code():
    print("\n***YOU CAME TO CODING SECTION***\n")
    code = input(" enter string to be encripted :  ")
    if len(code) >= 3:
        code = code.split()
        new_code = " ".join(code)
        new_code = new_code[1:] + new_code[0]
        new_code = str1 + new_code + str2
        print(f" \n generated code is  {new_code}\n")
    else:
        print(f"\n code is  : {code[::-1]} \n")


def decode():
    print("\n***YOU CAME TO DeCODING SECTION***\n")
    code = input(" \nenter string to be decripted :  ")
    if len(code) >= 3:
        code = code[3:-3]
        code = code[-1] + code[:-1]
        print(f" \n generated code is :  {''.join(code)}\n")
    else:
        print(f"\n code is  : {code[::-1]} \n")

    pass


while True:
    print(" \n1.Coding \n2. Decoding \n 3.exit")
    choice = int(input(" Please enter Ur choice"))
    match choice:
        case 1:
            code()
        case 2:
            decode()
        case 3:
            exit(1)
