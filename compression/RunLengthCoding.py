def encode(mystr):
    size=0 # initialising count of character
    encoded_msg='' #initialising empty encoded string
    
    for i in range(len(mystr)): #parsing through the string
        c=mystr[i] # storing char in variable
        size+=1    # increment count
        if i==len(mystr)-1: #if c is last character in string
            encoded_msg=encoded_msg+str(size)+c
            break
        else:
            if c==mystr[i+1]: #if look ahead char is same as c 
                pass
            else: #if look ahead char is not the same as c
                encoded_msg=encoded_msg+str(size)+c
                size=0 # reset count
                
        
    return encoded_msg

def decode(m_str):
    ret_str='' # initialise empty decoded string
    index=0 # pointer variable
    if m_str !='': # if string is not null
        while (index<len(m_str)):
            first='' #inintialise string for char count
            while (m_str[index] in '0123456789'):
                first+= m_str[index]
                index+=1
            num = int(first) #storing count value as integer
            c=m_str[index]   #corresponding character
            index+=1
            
            ret_str+=c*num   #concatenate count and character
    return ret_str            