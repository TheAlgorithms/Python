try:               # Python 2
    raw_input
    unichr
except NameError:  # Python 3
    raw_input = input
    unichr = chr


def Atbash():
    output=""
    for i in raw_input("Enter the sentence to be encrypted ").strip():
        extract = ord(i)
        if 65 <= extract <= 90:
            output += unichr(155-extract)
        elif 97 <= extract <= 122:
            output += unichr(219-extract)
        else:
            output+=i
    print(output)


if __name__ == '__main__':
    Atbash()
