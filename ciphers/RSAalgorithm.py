'''
Author : Dhruv B Kakadiya

'''

# import functions from prime number generater
from prime_number_generater import simple_testing, miller_rabin_test
from math import gcd
import random

alphabet = "qazxswedcvfrtgbnhyujmkiolp"

# function multiplicative inverse
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

# find phi of prime number n => n - 1 ; n is prime
def phi (n):
    return (n - 1)

# encryption function
def encryption (plain_text, e, n):
    return multiply_and_square(plain_text, e, n)

# decryption function
def decryption (cipher_text, d, n):
    return multiply_and_square(cipher_text, d, n)

#generate_keys
def generate_keys (p, q):
    while (True):
        e = random.randint(2, (phi(p) * phi(q) - 1))
        gcd_ = gcd(e, phi(p) * phi(q))
        if (gcd_ == 1):
            break
    d = find_mul_inverse(e, phi(p) * phi(q))
    public_key = (e, p * q)
    private_key = (d, p * q)
    return public_key, private_key

# main method
if __name__ == '__main__':
    count = 0
    primes = []
    n = int(input("\nEnter the number of bits of prime number :- "))
    while (count < 2):
        n_bit_prime = simple_testing(n)
        if (not miller_rabin_test(n_bit_prime)):
            continue
        else:
            primes.append(n_bit_prime)
            count += 1
    p, q = primes
    print(f"\nThe prime1 is => {p}")
    print(f"\nThe prime2 is => {q}")

    # rsa implementation
    public_key, private_key = generate_keys (p, q)
    print(f"\nPublic key is :- {public_key}")
    print(f"\nPrivate key is :- {private_key}")
    e, n = public_key
    d, n = private_key
    encrypted_text = decrypted_text = ""
    plain_text = input("\nEnter the plain text :- ")
    plain_text_list = plain_text.split()

    # encryption of plain text
    encrypted_ord_list = []
    for str in plain_text_list:
        encrypted_single_ord_list = []
        for letter in str:
            encrypted_single_ord_list.append(encryption(ord(letter), e, n))
        for cipher in encrypted_single_ord_list:
            encrypted_text += alphabet[(cipher % 26)]
        encrypted_text += " "
        encrypted_ord_list.append(encrypted_single_ord_list)
    print(f"\nEncrypted text is :- {encrypted_text}")

    # decryption of cipher text
    for str in encrypted_ord_list:
        for letter in str:
            decrypted_text += chr(decryption(letter, d, n))
        decrypted_text += " "

    print(f"\nDecrypted text is :- {decrypted_text}\n")


