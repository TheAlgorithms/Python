def find_char():
    str1 = input()
    char = input()
    if char in str1 and str1[-1] != char:
        print(str1.index(char) + 1)
    else:
        print("not found")


find_char()
