def reversevowel(s):
    st =[]
    k = ""
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u']:
            st.append(s[i])
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u']:
            k+= st.pop()
        else:
            k+=s[i]

    return k

if __name__ == "__main__":
    s=input()
    print(reversevowel(s))