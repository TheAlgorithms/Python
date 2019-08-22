def atbash():
    output=""
    for i in input("Enter the sentence to be encrypted ").strip():
        extract = ord(i)
        if 65 <= extract <= 90:
            output += chr(155-extract)
        elif 97 <= extract <= 122:
            output += chr(219-extract)
        else:
            output += i
    print(output)


if __name__ == '__main__':
    atbash()
