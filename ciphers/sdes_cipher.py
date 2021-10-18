
ip = (2, 6, 3, 1, 4, 8, 5, 7)
ip_inverse = (4, 1, 3, 5, 7, 2, 8, 6)
ep = (4, 1, 2, 3, 2, 3, 4, 1)
p10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
p8 = (6, 3, 7, 4, 8, 5, 10, 9)
p4 = (2, 4, 3, 1)

#predefined sboxes
sb0 = ((1, 0, 3, 2),
       (3, 2, 1, 0),
       (0, 2, 1, 3),
       (3, 1, 3, 2))

sb1 = ((0, 1, 2, 3),
       (2, 0, 1, 3),
       (3, 0, 1, 0),
       (2, 1, 0, 3))

#permute takes a bitstring and a predefined permutation as input and outputs a new permuted bitstring
def permute(bitstring, permutation):
    new = ''
    for i in permutation:
        new += bitstring[i - 1]
    return new

#left_half takes a bitstring as input and breaks it in half, returning the left side
def left_half(bitstring):
    return bitstring[:int(len(bitstring)/2)]

#right_half takes a bitstring as input and breaks it in half, returning the right side
def right_half(bitstring):
    return bitstring[int(len(bitstring)/2):]

#lshift takes a bitstring as input and shifts the two halves of it to the left by one
def lshift(bitstring):
    shifted_left_half = left_half(bitstring)[1:] + left_half(bitstring)[0]
    shifted_right_half = right_half(bitstring)[1:] + right_half(bitstring)[0]
    return shifted_left_half + shifted_right_half

#key1 applys all of the functions necessary to generate k1 from the original 10 bit key
def key1(key):
    return permute(lshift(permute(key, p10)), p8)

#key2 applys all of the functions necessary to generate k2 from the original 10 bit key
def key2(key):
    return permute(lshift(lshift(lshift(permute(key, p10)))), p8)

#xor takes two bitstrings as input XOR-ing them and giving the result as output
def xor(bitstring, key):
    new = ''
    for str_bit, key_bit in zip(bitstring, key):
        new += str(((int(str_bit) + int(key_bit)) % 2))
    return new

#sblookup takes a bitstring and an sbox as input.
#using the bitstring value, it gets the corresponding value from the sbox.
#it then converts the values from the sbox to binary and returns that binary value
def sblookup(bitstring, sbox):
    row = int(bitstring[0] + bitstring[3], 2)
    col = int(bitstring[1] + bitstring[2], 2)
    return '{0:02b}'.format(sbox[row][col])

#applys the functions that make up f_K
def f_k(bitstring, key):

    #breaks the bitstring into right and left sides
    L = left_half(bitstring)
    R = right_half(bitstring)

    #expand and permute the right side of the 8 bit plaintext
    bitstring = permute(R, ep)

    #xor the previous output with the key
    bitstring = xor(bitstring, key)

    #looks up the left and right halves of the previous output in sbox0 and sbox1 respectively
    #then it recombines the sbox values into 'bitstring'
    bitstring = sblookup(left_half(bitstring), sb0) + sblookup(right_half(bitstring), sb1)

    #appys p4 to 'bitstring'
    bitstring = permute(bitstring, p4)

    #returns the previous output xor'd with the left half of the original bitstring
    return xor(bitstring, L)

#applys the functions that make up the encryption process
def encrypt(plain_text,key):

    #permutes the plaintext using ip
    bitstring = permute(plain_text, ip)

    #holds the output of fk using the previous output and k1 and input
    temp = f_k(bitstring, key1(key))

    #combines the output of fk with the right half of the result of ip
    bitstring = right_half(bitstring) + temp

    #puts the previous output and k2 through the fk function
    bitstring = f_k(bitstring, key2(key))

    #ip inverse permutes the previous output combined with the output of fk(ip, k1)
    return (permute(bitstring + temp, ip_inverse))

#applys the functions that make up the decryption process
def decrypt(cipher_text,key):
    #permutes the cyphertext using ip
    bitstring = permute(cipher_text, ip)

    #holds the output of fk using the previous output and k2 and input
    temp = f_k(bitstring, key2(key))

    #combines the output of fk with the right half of the result of ip
    bitstring = right_half(bitstring) + temp

    #puts the previous output and k1 through the fk function
    bitstring = f_k(bitstring, key1(key))

    #ip inverse permutes the previous output combined with the output of fk(ip, k2)
    return (permute(bitstring + temp, ip_inverse))


plaintext='10100001'
key='0001101101'
cipher_text=encrypt(plaintext,key)
print("Encrypted Text: ",encrypt(plaintext,key))
print("Decrypted Text: ",decrypt(cipher_text,key))




