# Encryption
print("welcome to RSA enter the public key to encrypt.....................")
public = (int(input("enter e-->>")), int(input("enter n-->>")))


def encrypt(pub_key, n_text):
    e, n = pub_key
    x = ""
    p = ""
    
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-64

        elif(i.islower()):
            m = ord(i)-96

        elif(i.isspace()):
            m = 32
        
        p=str(p)+str('%02d' % m)
    print("no.conversion is:",p)  

    z =[(p[i:i+4]) for i in range(0, len(p), 4)]
    print(z)
    e, n = pub_key
    for y in z:
        
        
        c = (int(y.lstrip('0'))**e)%n
        #print(c)
        x = str(x)+str('%06d' % c)
    
    return x


message = input("What would you like encrypted:")
print("Your message is:", message)

choose = input("enter 'go' for encryption>>>>> ")
if(choose == 'go'):
    enc_msg = encrypt(public, message)
    print("Your encrypted message is(copy this to A program for decryption):", enc_msg)
    print("Thanks for using!:):):)")

else:
    print("Try again and enter 'go'")


input('Press ENTER to exit')
