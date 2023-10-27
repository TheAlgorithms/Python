#python prog to capitilize the string
def custom_upper(string) -> None:
    upper_string=""
    for char in string:
        if 'a'<=char<='z':
            upper_string+=chr(ord(char)-32)
        else:
            upper_string+=char
    return upper_string

def custom_lower(string) -> None:
    lower_string=""
    for char in string:
        if 'A'<=char<='Z':
            lower_string+=chr(ord(char)+32)
        else:
            lower_string+=char
    return lower_string


def custom_capitalize(w)-> None:
    return custom_upper(w[0])+custom_lower(w[1:])

def custom_title(string)-> None:
    words=string.split()
    tcw=[]
    for i in words:
        t=custom_capitalize(i)
        tcw.append(t)
    sentence=' '.join(tcw)
    print(sentence)

string=input("enter the string")
custom_title(string)M