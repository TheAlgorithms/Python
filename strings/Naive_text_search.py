def naive(txt,wrd):
    lt=len(txt)#length of the string
    lw=len(wrd)/3length of the substring(pattern)
    for i in range(lt-lw+1):
        j=0
        while(j<lw):
            if txt[i+j]==wrd[j]:
                j+=1
            else:
                break
        else:
            print('found at position',i)
