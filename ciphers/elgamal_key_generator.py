import os
import random
import sys
import rabin_miller as rabinMiller, cryptomath_module as cryptoMath

min_primitive_root = 3


def main():
    print('Making key files...')
    makeKeyFiles('elgamal', 2048)
    print('Key files generation successful')


# I have written my code naively same as definition of primitive root
# however every time I run this program, memory exceeded...
# so I used 4.80 Algorithm in Handbook of Applied Cryptography(CRC Press, ISBN : 0-8493-8523-7, October 1996)
# and it seems to run nicely!
def primitiveRoot(p_val):
    print("Generating primitive root of p")
    while True:
        g = random.randrange(3,p_val)
        if pow(g, 2, p_val) == 1:
            continue
        if pow(g, p_val, p_val) == 1:
            continue
        return g


def generateKey(keySize):
    print('Generating prime p...')
    p = rabinMiller.generateLargePrime(keySize)  # select large prime number.
    e_1 = primitiveRoot(p)  # one primitive root on modulo p.
    d = random.randrange(3, p)  # private_key -> have to be greater than 2 for safety.
    e_2 = cryptoMath.findModInverse(pow(e_1, d, p), p)

    publicKey = (keySize, e_1, e_2, p)
    privateKey = (keySize, d)

    return publicKey, privateKey


def makeKeyFiles(name, keySize):
    if os.path.exists('%s_pubkey.txt' % name) or os.path.exists('%s_privkey.txt' % name):
        print('\nWARNING:')
        print('"%s_pubkey.txt" or "%s_privkey.txt" already exists. \n'
              'Use a different name or delete these files and re-run this program.' %
              (name, name))
        sys.exit()

    publicKey, privateKey = generateKey(keySize)
    print('\nWriting public key to file %s_pubkey.txt...' % name)
    with open('%s_pubkey.txt' % name, 'w') as fo:
        fo.write('%d,%d,%d,%d' % (publicKey[0], publicKey[1], publicKey[2], publicKey[3]))

    print('Writing private key to file %s_privkey.txt...' % name)
    with open('%s_privkey.txt' % name, 'w') as fo:
        fo.write('%d,%d' % (privateKey[0], privateKey[1]))


if __name__ == '__main__':
    main()