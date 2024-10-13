"""
Paillier cryptosystem was introduced in 1999 by Pascal Paillier. It is
an asymmetric algorithm for public key cryptography.
    ----Public-Key Cryptosystems Based on Composite Degree Residuosity Classes
    ----https://link.springer.com/content/pdf/10.1007/3-540-48910-X_16.pdf

It is famous for its Homomorphic Properties present between cypher and
message space. i.e.
    E(m1 + m2) = E(m1) * E(m2)
    where:
        E is encryption scheme
        m1, m2 are messages
        + is addition operation in message space
        * is multiplication operation in cypher space

Due to its Homomorphic properties it is highly studied in fields like:
    Electronic voting
    Electronic cash
    Electronic auction
    Zero Knowledge Proofs

Read more : https://en.wikipedia.org/wiki/Paillier_cryptosystem
"""


# Implementation details:
#     Utils:
#         primeGenerator()  ++
#         GCD()             ++
#         LCM()             ++
#         getInverse()      ++
#         L()               ++
#         Zn:
#            __init__()     ++
#            sample()       ++
#            __contains__() ++
#         Zn_star:
#            __init__()     ++
#            sample()       ++
#            __contains__() ++
#         Zn2_star:
#            __init__()     ++
#            sample()       ++
#            __contains__() ++
#     PaillierCryptosystem:
#         __init__()        ++
#         keyGen()          ++
#         getPublicKey()    ++
#         getPrivateKey()   ++
#         encrypt()         ++
#         decrypt()         ++
#         homomorphicADD()  ++
#         homomorphicMUL()  ++

import sympy
import random


class Utils:
    def primeGenerator(bit_size):
        """
        Uses sympy.randprime() for genearing a prime number
        of a particular bit-size
        """
        low = 2 ** (bit_size - 1)
        high = (2**bit_size) - 1
        return sympy.randprime(low, high)

    def GCD(a, b):
        """
        Returns the Greatest Common Divisor of 2 numbers
        aka Highest Common Factor
        """
        while b > 0:
            a, b = b, a % b
        return a

    def LCM(a, b):
        """
        Returns Least Common Multiple of 2 numbers
        """
        return a * b // Utils.GCD(a, b)

    def getInverse(a, n):
        """
        Returns number 'b' such that
        a*b == 1 (mod n)
        """
        return pow(a, -1, n)

    def L(x, n):
        """
        As defined in original paper by Pascal Paillier
        L(x) = (x-1)/n
        """
        mu = x - 1
        assert mu % n == 0
        mu = mu // n
        return mu

    class Zn:
        """
        Model of set of Whole numbers less than n.
        """

        def __init__(self, n):
            # n :: n = p*q -> p,q are prime
            self.n = n

        def sample(self):
            return random.randint(0, self.n - 1)

        def __contains__(self, item):  # in operator
            return (0 <= item) and (item < self.n)

    class Zn_star:
        """
        Model of set of Natural numbers less than n
        which are invertible in (mod n) system.
        """

        def __init__(self, n):
            self.n = n

        def sample(self):
            while True:
                temp = random.randint(1, self.n - 1)
                if Utils.GCD(temp, self.n) == 1:
                    return temp

        def __contains__(self, item):  # in operator
            if (1 <= item) and (item < self.n):
                if Utils.GCD(item, self.n) == 1:
                    return True
            return False

    class Zn2_star:
        """
        Model of set of Natural numbers less than n^2
        which are invertible in (mod n^2) system.
        """

        def __init__(self, n):
            # n :: n = p*q -> p,q are prime
            self.n2 = n**2
            self.p = p
            self.q = q

        def sample(self):
            while True:
                temp = random.randint(1, self.n2 - 1)
                if Utils.GCD(temp, self.n2) == 1:
                    return temp

        def __contains__(self, item):  # in operator
            if (1 <= item) and (item < self.n2):
                if Utils.GCD(item, self.n2) == 1:
                    return True
            return False


class PaillierCryptosystem:
    def __init__(self, bit_size=256):
        self.bitSize = bit_size
        self.p = None
        self.q = None
        self.n = None
        self.n2 = None
        self.g = None
        self.l = None
        self.lcm = None

        self.privateKey = None
        self.publicKey = None

    def keyGen(self):
        """
        This function is resoponsible for:
            initialising p, q
            setting n, n^2
            setting lambda
            setting mu ( lambda^-1 - TRAPDOOR)
            setting PUBLIC and PRIVATE KEY
        """
        p = Utils.primeGenerator(self.bitSize)
        while True:
            q = Utils.primeGenerator(self.bitSize)
            if q != p:
                break
        self.p = p
        self.q = q
        self.n = p * q
        self.n2 = self.n**2
        self.g = self.n + 1
        self.l = (p - 1) * (q - 1)
        self.lcm = Utils.LCM((p - 1), (q - 1))

        self.mu = Utils.getInverse(
            self.lcm, self.n
        )  # mu = lambda^(-1) (mod n) -->> TRAPDOOR

        self.publicKey = {
            "n": self.n,  # Main PUBLIC KEY
            "n2": self.n2,  # Defining System - Computational Ease
            "g": self.g,  # Main PUBLIC KEY
        }

        self.privateKey = {
            "n": self.n,  # Defining System - Computational Ease - Available from PUBLIC KEY
            "n2": self.n2,  # Defining System - Computational Ease - Available from PUBLIC KEY
            "mu": self.mu,  # Main PRIVATE KEY
            "lambda": self.lcm,  # Main PRIVATE KEY
        }

    def getPublicKey(self):
        """
        Function to access PUBLIC KEY
        """
        return self.publicKey

    def getPrivateKey(self):
        """
        Function to access PRIVATE KEY
        """
        return self.privateKey

    def encrypt(pubKey: dict, msg: int):
        """
        Function to encrypt message using PRIVATE KEY.

        It is a static method to ensure it has no access to
        additional information other than provided PUBLIC KEY.

        msg belongs to Zn (all Whole numbers less than n)
        """
        n = pubKey["n"]
        n2 = pubKey["n2"]
        g = pubKey["g"]

        zn = Utils.Zn(n)
        zn_star = Utils.Zn_star(n)

        # c = (g**x)(r**n) (mod n^2)
        assert msg in zn
        r = zn_star.sample()
        assert r in zn_star

        a = pow(g, msg, n2)
        b = pow(r, n, n2)
        return (a * b) % n2

    def decrypt(prvKey: dict, cypher: int):
        """
        Function to decrypt cypher using PRIVATE KEY.

        It is a static method to ensure it has no access to
        additional information other than provided PRIVATE KEY.

        cypher belongs to Z(n^2) (all Naturals which are
        invertible in (mod n^2) system)
        """
        n = prvKey["n"]
        n2 = prvKey["n2"]
        mu = prvKey["mu"]
        lmbda = prvKey["lambda"]

        t = pow(cypher, lmbda, n2)
        t = Utils.L(t, n)  # L(cypher ^ lambda) == lambda * message (mod n)

        msg = (
            (t * mu) % n
        )  # (lambda * message) * mu == (lambda * message) * (lambda^-1) == msg (mod n)
        return msg

    def homomorphicADD(pubKey: dict, cypher1: int, cypher2: int):
        """
        cypher1 * cypher2 -->>  Encryption( msg1 + msg2 )
        Both the messages are encrypted and do not
        require decryption to perform Binary Operation (ADD)

        E(m1) = (g^m1)*(r1^n) (mod n^2)
        E(m2) = (g*m2)*(r2^n) (mod n^2)

        E(m1+m2) = E(m1)*E(m2) = (g^(m1+m2))*((r1*r2)^n) (mod n^2)
        """
        n2 = pubKey["n2"]
        return (cypher1 * cypher2) % n2

    def homomorphicMUL(pubKey: dict, cypher1: int, msg2: int):
        """
        cypher1 ** msg2 -->>  Encryption( msg1 * msg2 )
        It requires 2nd msg to be decrypted to perfrom
        Binary Operation (MUL).

        E(m1) = (g^m1)*(r1^n) (mod n^2)
        m2 in Zn

        E(m1*m2) = E(m1)^m2 (mod n^2)
        """
        n2 = pubKey["n2"]
        return pow(cypher1, msg2, n2)


if __name__ == "__main__":
    # base = 256
    for i in range(5, 9):
        base = 2**i
        print(f"TESTING BITSIZE : {base}")
        crypto = PaillierCryptosystem(base)
        crypto.keyGen()

        pub = crypto.getPublicKey()
        msg = 233
        print(f"Msg       : {msg}")
        c = PaillierCryptosystem.encrypt(pub, msg)
        print(f"Cypher    : {c}")

        prv = crypto.getPrivateKey()
        d = PaillierCryptosystem.decrypt(prv, c)
        print(f"Decryption: {d}")
        assert msg == d

        msg2 = 232
        c2 = PaillierCryptosystem.encrypt(pub, msg2)
        c3 = PaillierCryptosystem.homomorphicADD(pub, c, c2)
        d3 = PaillierCryptosystem.decrypt(prv, c3)
        assert d3 == (msg + msg2)
        print("Homomorphic Add SUCCESSFUL")

        c4 = PaillierCryptosystem.homomorphicMUL(pub, c, msg2)
        d4 = PaillierCryptosystem.decrypt(prv, c4)
        assert d4 == (msg * msg2)
        print("Homomorphic Mul SUCCESSFUL")
        print()
