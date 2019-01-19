def encodeBase64(text):
    base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    r = "" #the result
    c = 3 - len(text) % 3 #the length of padding
    p = "=" * c #the padding
    s = text + "\0" * c #the text to encode
    
    i = 0   
    while i < len(s):
        if i > 0 and ((i / 3 * 4) % 76) == 0:
            r = r + "\r\n"
        
        n = (ord(s[i]) << 16) + (ord(s[i+1]) << 8 ) + ord(s[i+2])
        
        n1 = (n >> 18) & 63
        n2 = (n >> 12) & 63
        n3 = (n >> 6)  & 63
        n4 = n & 63
        
        r += base64chars[n1] + base64chars[n2] + base64chars[n3] + base64chars[n4]
        i += 3

    return r[0: len(r)-len(p)] + p
    
def decodeBase64(text):
    base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    s = ""
    
    for i in text:
        if i in base64chars:
            s += i
            c = ""
        else:
            if i == '=':
                c += '='
    
    p = ""
    if c == "=":
        p = 'A'
    else:
        if c == "==":
            p = "AA"
    
    r = ""
    s = s + p
   
    i = 0
    while i < len(s):
        n = (base64chars.index(s[i]) << 18) +  (base64chars.index(s[i+1]) << 12) +  (base64chars.index(s[i+2]) << 6) +base64chars.index(s[i+3])
        
        r += chr((n >> 16) & 255) + chr((n >> 8) & 255) + chr(n & 255)
        
        i += 4
    
    return r[0: len(r) - len(p)]

def main():
    print(encodeBase64("WELCOME to base64 encoding"))
    print(decodeBase64(encodeBase64("WELCOME to base64 encoding")))
    

if __name__ == '__main__':
    main()
