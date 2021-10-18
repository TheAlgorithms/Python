def unjumble(word):
    str = []
    str2 = []
    res = []

    for i in word:
        str.append(i)

    str.sort()
    f = open("words.txt","r")


    for line in f:
        i = line
        for x in i:
            str2.append(x)


        str2.pop()
        str2.sort()
        if str == str2:
            res.append(line)
        str2=[]



    print(res)

word = input("Enter the jumbled word : ")
word=word.lower()
unjumble(word)