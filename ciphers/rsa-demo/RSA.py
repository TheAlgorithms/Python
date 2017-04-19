from tools import generate_sen_jermen_prime, generate_prime
from tools import rand_range
from tools import inv_mod, pow_mod
from fractions import gcd
from pickle import dump, load


def generate_RSA_credentials(bit_length, strong=True, fast=True):
    #  fast: uses common public exponent with almost all bits equals to zero
    #  strong: uses sen jermen type of prime numbers
    
    get_prime = generate_sen_jermen_prime if strong else generate_prime

    credentials = {"secret_key": {}, "shared_key": {}}

    #  there is no guarantee that length of generated shared_key always would equal to bit_length
    p, q = get_prime(bit_length/2), get_prime(bit_length/2)
    n = p*q

    credentials["secret_key"]["p"] = p
    credentials["secret_key"]["q"] = q
    credentials["shared_key"]["n"] = n

    phi = (p-1) * (q-1)

    if fast:
        e = 65537
        d = inv_mod(e, phi)
        credentials["shared_key"]["e"] = e
        credentials["secret_key"]["d"] = d
        return credentials

    while True:
        e = rand_range(2, phi-1)
        if gcd(e, phi) == 1:
            d = inv_mod(e, phi)
            credentials["shared_key"]["e"] = e
            credentials["secret_key"]["d"] = d
            return credentials


def save_credentials(filename, credentials):
    with open(filename, "wb") as f:
        dump(credentials, f)


def load_credentials(filename):
    credentials = None
    with open(filename, "rb") as f:
        credentials = load(f)

    return credentials


def RSA_encrypt(message, shared_key):
    n = shared_key["n"]
    e = shared_key["e"]
    if 0 < message < n:
        return pow_mod(message, e, n)


def RSA_decrypt(cipher, credentials):
    n = credentials["shared_key"]["n"]
    d = credentials["secret_key"]["d"]
    if 0 < cipher < n:
        return pow_mod(cipher, d, n)


def RSA_sign(message, credentials):
    d = credentials["secret_key"]["d"]
    n = credentials["shared_key"]["n"]
    signature = pow_mod(message, d, n)
    return signature


def RSA_check(message, signature, shared_key):
    e = shared_key["e"]
    n = shared_key["n"]
    M = pow_mod(signature, e, n)
    return M == message
