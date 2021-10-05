import os
from typing import Any

from Cryptodome.PublicKey import RSA


def RSAKeyGen(keylen: int = 1024) -> dict:
    """Create a new RSA public-private key pair and stores them in separate files.

    Args:
        keylen: Key length, or size (in bits) of the RSA modulus. It must be
        at least 1024. Default is 1024.

    Returns:
        dict: Returns a dictionar containing the path to the key files and a
        flag indicating whether the "keys" folder already contains a key pair,
        which would be overwritten.

    >>> RSAKeyGen (1024) != None
    True
    """
    os.makedirs("keys", exist_ok=True)
    private_path = os.path.join("keys", f"private-{keylen}.pem")
    public_path = os.path.join("keys", f"public-{keylen}.pem")
    item = None
    if os.path.exists(private_path) and os.path.exists(public_path):
        with open(private_path, "r") as pri_read:
            private_key = RSA.import_key(pri_read.read())
        with open(public_path, "r") as pub_read:
            public_key = RSA.import_key(pub_read.read())

        item = {"pub_path": public_path, "pri_path": private_path, "flag": 0}
        return item

    private_key = RSA.generate(int(keylen))
    public_key = private_key.publickey()

    with open(private_path, "wb") as pri_write:
        pri_write.write(private_key.export_key("PEM"))

    with open(public_path, "wb") as pub_write:
        pub_write.write(public_key.export_key("PEM"))
    item = {"pub_path": public_path, "pri_path": private_path, "flag": 1}
    return item


def make_valid(value: Any) -> int:
    """Makes sure the input is valid for the Key generation algorithm.

    Args:
        value: the user input
    Returns:
        int: valid key length for the key generation algorithm.
    """
    default = 1024
    if value.isalpha():
        print("You pressed a letter. Returning default keylength 1024.")
        return default
    else:
        value = int(float(value))
        return value


if __name__ == "__main__":
    print("Starting RSA Key Generation ....")
    flag = True
    key_ = input("Pick one of the keylengths :\n1. 1024\n2. 2048\n3. 4096\n")
    key = make_valid(key_)

    if key == 1 or key == 1024:
        keylen = 1024
    elif key == 2 or key == 2048:
        keylen = 2048
    elif key == 3 or key == 4096:
        keylen = 4096
    else:
        print("Only one of the given options (1,2,3) is accepted.")
        flag = False
    if flag is True:
        print(f"Generating RSA key pairs for key length {keylen} ....")
        response = RSAKeyGen(keylen)
        if response["flag"] == 1:
            print("Generating first time key pairs.")
        else:
            print("Using previously generated key pairs.")
        print(f"Public Key in: {response['pub_path']}")
        print(f"Private Key in: {response['pri_path']}")
