

# coding=utf-8
from random import randint
import math

# generate random prime function
def generate_prime():
    x = randint(50, 999)
    while True:
        if is_prime(x):
            break
        else:
            x += 1
    return x

# primality check function
def is_prime(x):
    i = 2
    root = math.ceil(math.sqrt(x))
    while i <= root:
        if x % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
   
    p = generate_prime()
    while True:
        q = generate_prime()
        if q != p:
            break
    print("p = %d" % p)
    print("q = %d" % q)


# RSA Modulus
n = p * q
print("RSA Modulus(n) is:", n)

# Eulers Toitent
r = (p-1)*(q-1)
print("Eulers Toitent(r) is:", r)
print("--------------------------------------------------------------")

# GCD
def egcd(e, r):
    while(r != 0):
        e, r = r, e % r
    return e

# Euclid's Algorithm
def eugcd(e, r):
    for i in range(1, r):
        while(e != 0):
            a, b = r//e, r % e
            if(b != 0):
                print("%d = %d*(%d) + %d" % (r, a, e, b))
            r = e
            e = b

# Extended Euclidean Algorithm
def eea(a, b):
    if(a % b == 0):
        return(b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return(gcd, t, s)

# Multiplicative Inverse
def mult_inv(e, r):
    gcd, s, _ = eea(e, r)
    if(gcd != 1):
        return None
    else:
        if(s < 0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d." %
                  (s, s, s % r))
        elif(s > 0):
            print("s=%d." % (s))
        return s % r


# e Value Calculation
for i in range(1, randint(50,1000)):
    if(egcd(i, r) == 1):
        e = i
print("The value of e is:", e)
print("------------------------------------------------------")

# d, Private and Public Keys
print("EUCLID'S ALGORITHM:")
eugcd(e, r)
print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e, r)
print("The value of d is:", d)
public = (e, n)
private = (d, n)
print("Private Key is:", private)
print("Public Key is:", public)
print("------------------------------------------------------")


# Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(priv_key, c_text):
    d, n = priv_key
    txt = c_text

    z = [(txt[i:i+6]) for i in range(0, len(txt), 6)]
    q = ""
    print(z)
    x = ''
   # m = 0
    for y in z:
        m = (int(str(y).lstrip('0'))**d) % n

        q = str(q)+str('%04d' % m)
    t = [(q[e:e+2]) for e in range(0, len(q), 2)]
    print(t)
    for g in t:

        g = int(g)+64
        c = chr(int(g))
        x += c

    return x

message = input("What would you like decrypted>>>>")
print("Your message is:", message)

# Choose 2 for Decrypt and Print
choose = input("Type '2' for decrytion.")
if (choose == '2'):
    print("Your decrypted message is:", decrypt(private, message))
    print("Thank you for using.:):):)!")
else:
    print("You entered the wrong option.")
    print("Thank you for using. :);):)!")

input('Press ENTER to exit')
