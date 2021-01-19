'''
Author : Dhruv B Kakadiya

'''

import random as rd
from prime_number_generater import simple_testing, miller_rabin_test
# In python there is a module called Elgamal!

all_char = ""
for i in range(32, 128):
    all_char += chr(i)

#alphabet = "abcdefghijklmnopqrstuvwxyz"

# to find multiplicative_inverse
def find_mul_inverse (a, n):
    mod = n
    t1, t2 = 0, 1
    while(a > 0):
        q = n // a
        r = n - (q * a)
        n, a = a, r
        t = t1 - (q * t2)
        t1, t2 = t2, t
    return (t1 % mod)

# phi function
def phi (n):
    return (n - 1)

# multiply and square function
def multiply_and_square(a, x, n):
    x = bin(x)
    x = x[2 : ]
    x = x[:: -1]
    y = 1
    for i in range(0, len(x)):
        if (int(x[i]) == 1):
            y = (y * a) % n
        a = (a ** 2) % n
    return y

# find order
def primitive_roots_order (prime):
    order = [None] * prime
    # find the all primitive roots
    for r in range(1, prime):
        #first_one = True
        for c in range(1, prime):
            mas = multiply_and_square(r, c, prime)
            if (mas == 1):
                order[r] = c
                break
    return order

# find all primitive roots
def all_roots (order, prime):
    proots = []
    phi_prime = phi (prime)
    for i in range(1, len(order)):
        if (order[i] == phi_prime):
            proots.append(i)
    return proots

# find public and private keys
def find_public_private_key (proots, prime):
    e1 = proots[rd.randint(0, len(proots) - 1)]
    condition = prime - 2
    while (True):
        d = proots[rd.randint(0, len(proots) - 1)]
        if (d <= condition):
            break
    e2 = multiply_and_square (e1, d, prime)
    return (e1, e2, prime), d


# encryption
def encryption_for_2 (letter, e2, r, prime):
    return (multiply_and_square(e2, r, prime) * (letter % prime))

def encryption_for_1 (e1, r, prime):
    return (multiply_and_square(e1, r, prime))

def decryption (letter, cipher_text_1, d, prime):
    return ((letter % prime) * (find_mul_inverse (cipher_text_1 ** d, prime))) % prime


# main if condition
if __name__ == "__main__":
    n = int(input("\nEnter the number of bits of prime number :- "))
    while (True):
        n_bit_prime = simple_testing(n)
        if (not miller_rabin_test(n_bit_prime)):
            continue
        else:
            prime = n_bit_prime
            break
    print(f"\nThe prime number is => '{prime}'")

    order = primitive_roots_order (prime)
    proots = all_roots (order, prime)

    # finding public and private key
    public_key, private_key = find_public_private_key (proots, prime)
    e1, e2, prime = public_key
    d = private_key
    print(f"\nPublic key is => '{public_key}'")
    print(f"private key is => '{private_key}'")

    # Encryption and Decryption of plain_text data
    r = proots[rd.randint(0, len(proots) - 1)]
    plain_text = input("\nEnter the plain text :- ")
    cipher_text_1 = ""
    cipher_text_2 = ""

    cipher_text_1 = encryption_for_1 (e1, r, prime)

    cipher2_ord_list = []
    encrypted_ord_list = []
    for letter in plain_text:
        encrypted_ord_list.append(encryption_for_2(ord(letter), e2, r, prime))
    for cipher in encrypted_ord_list:
        cipher_text_2 += all_char[(cipher % 96)]

    print(f"\nCipher text 1 => '{cipher_text_1}'")
    print(f"\nCipher text 2 => '{cipher_text_2}'")

    decrypted_text = ""
    for letter in encrypted_ord_list:
        decrypted_text += chr(decryption(letter, cipher_text_1, d, prime) % prime)

    print(f"\n\n\nDecrypted text => {decrypted_text}")