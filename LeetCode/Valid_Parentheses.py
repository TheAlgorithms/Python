def isValid(s):
    if len(s)==0:
        return True

    s1=[]
    dic={')':'(',']':'[','}':'{'}

    for i in s:
        if i=='(' or i=='[' or i=='{':
            s1.append(i)

        else:
            if len(s1)==0:
                return False

            else:
                c1=s1.pop()

                if dic[i]!=c1:
                    return False

    if len(s1)==0:
        return True
    else:
        return False
