'''
RC4 is a stream cypher algorithm
At first a matrix S is create , with 256 elements where each element is the index
Then,based on the message some pseudorandom permutations are being made to the matrix S
Later, a keystream is created based on the permuted S, length equals to the message's
When the creation of this keystream is completed, the basic operation, the XOR logic,
is performed, between each byte of the message and the keystream, one by one.
'''

import array as S
aDict = dict(zip('abcdefghijklmnopqrstuvwxyz.!?()-ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                              ['00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001',
                              '11010','11011','11100','11101','11110','11111',
                              '00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
'11000','11001'])) #the function from our alphabet to 5-bit binary strings
bits = 5
mes = "THIS IS THE MESSAGE"
print("my message is :"+mes)
mes = mes.replace(" ","")

k = "KEY"
print("my key is : " + k)

def bitXor(a,b):
    if(a is b):
        return "0"
    else:
        return "1";

def text_enc(text):
    text = text[::-1]
    length = len(text)
    coded_text = ''
    for i in range(length):
        coded_text = aDict[text[i]]+ coded_text
    return coded_text.lower()


def KSA(message,key):
    k = text_enc(key)

    S = [0 for i in range(255)]
    for i in range(0,255):
        S[i] = i

    j = 0
    key_length = len(k)
    for i in range(0,255):
        j = (j + S[i] + int(k[i%key_length]))%255
        S[i],S[j] = S[j],S[i]

    return S

def PRG(S,message,key):
    length = len(message)
    i=0
    j=0
    new_key = []
    while(length > 0):
        i = (i + 1)%255
        length = length -1
        j = (j + S[i])%255
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j])%255
        new_key.append(S[t]%(2**bits))

    return new_key

def RC4_en(message,key):

    keystreams = []
    keystreams = PRG(KSA(message,key),message,key)

    inv_map = {v: k for k, v in aDict.items()}
    encoded = ""
    par1 =""
    result = ""
    par1 = text_enc(message)
    k = 0

    for i in range(len(par1)):
        par2 = format(keystreams[k], 'b').zfill(bits)
        result = result + ""+bitXor(par1[i],par2[i%bits])

        if((i%bits)==bits-1):
            encoded = encoded+""+inv_map[result]
            result = ""
            k=k+1


    return encoded


def RC4_dec(encrypted,key):
    keystreams = []
    keystreams = PRG(KSA(encrypted, key), encrypted, key)

    inv_map = {v: k for k, v in aDict.items()}
    decoded = ""
    par1 = ""
    result = ""
    par1 = text_enc(encrypted)
    k = 0
    for i in range(len(par1)):
        par2 = format(keystreams[k], 'b').zfill(bits)
        result = result + ""+bitXor(par1[i],par2[i%bits])

        if ((i % bits) == bits - 1):
            decoded = decoded+""+inv_map[result]
            result = ""
            k = k + 1

    return decoded


encr = RC4_en(mes,k);
print("Encrypted message is : " + encr)
decr = RC4_dec(encr,k)
print("Decrypted message is : " + decr )
