import hashlib
import random


def verifySig(M, S):
    for i in range(q):
        if(((S[1]*i) % q) == 1):
            w = i
    Mhash = hashlib.sha1(M.encode()).hexdigest()
    MhashInt = int(Mhash, 16)
    u1 = (MhashInt * w) % q
    u2 = (S[0] * w) % q
    v = (((g**u1) * (y**u2)) % p) % q
    print("\n=========\nVerifying\n=========")
    print("Message Recieved :", M)
    print(f"u1 = {u1}\nu2 = {u2}\nv = {v}")
    return True if v == S[0] else False


p = int(input("Enter Large Prime Number (>100) :: "))
q = int(input("Enter Prime Divisor :: "))
g = int(input("Enter Global Variable :: "))

x = random.randint(1, q-1)
y = (g**x) % p
k = random.randint(1, q-1)

for i in range(q):
    if(((k*i) % q) == 1):
        kInv = i

print("\n============================\nGlobal Public Key Components\n============================")
print(f"p = {p}\nq = {q}\ng = {g}")

print("\n================\nUser Private Key\n================")
print("x =", x)

print("\n===============\nUser Public Key\n===============")
print("y =", y)

print("\n==================\nUser Secret Number\n==================")
print("k =", k)

msg = input("\nEnter The Message :: ")

msgHash = hashlib.sha1(msg.encode()).hexdigest()
msgHashInt = int(msgHash, 16)
r = ((g**k) % p) % q
s = (kInv * (msgHashInt + (x*r))) % q
sig = [r, s]

print("\n=======\nSigning\n=======")
print(f"r = {r}\ns = {s}\nSignature = {sig}")
checked = verifySig(msg, sig)

print("\n=======\nResult\n=======")
print("Verified" if checked else "Not Verified")
