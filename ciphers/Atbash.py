def Atbash():
    inp=raw_input("Enter the sentence to be encrypted  ")
    output=""
    for i in inp:
        extract=ord(i)
        if extract>=65 and extract<=90:
            output+=(unichr(155-extract))
        elif extract>=97 and extract<=122:
            output+=(unichr(219-extract))
        else:
            output+=i
    print (output)

Atbash()   ;
