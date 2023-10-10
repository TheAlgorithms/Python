from hashlib import sha256


def updatehash(*args):
    """
    - Exmple :
        >>> updatehash(1,2,3,4,5)
        '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'
    """
    hashing_text = ""
    h = sha256()
    for arg in args:
        hashing_text += str(arg)
    h.update(hashing_text.encode("utf-8"))
    return h.hexdigest()


class Block:
    """
    Block class represents each block in the blockchain
    and it's attributes.
    Atruibutes:
        - data : data to be stored in the block
        - number : the number of the block
        - previous_hash : the hash of the previous block
        - nonce : the nonce of the block ( number to make the hash of the block valid)
    Methods:
        - hash : returns the hash of the block
        - __str__ : returns a string representation of the block
    """
    def __init__(self, number=0, previous_hash="0" * 64, data=None, nonce=0):
        self.data = data
        self.number = number
        self.previous_hash = previous_hash
        self.nonce = nonce
    def hashdata(self):
        return updatehash(self.number, self.previous_hash, self.data, self.nonce)

    def __str__(self):
        return str("Block#: {}\nHash: {}\nPrevious: {}\nData: {}\nNonce: {}\n".format
            (self.number, self.hashdata(), self.previous_hash, self.data, self.nonce)
        )

    """
        >>> block1 = Block(1, "0"*64, "data1", 0)
        >>> print(block1)
            Block#: 1
            Hash: 47cf022b180526de8f7d0ec5951f00181d2a2853c68305c3c1fbdede2eaec30d
            Previous: 0000000000000000000000000000000000000000000000000000000000000000
            Data: data1
            Nonce: 0
        >>> block2 = Block(2, block1.hash(), "data2", 0)
            Block#: 2
            Hash: e71a2a3711b3cc965d6c5888149ab81e51ee7bd29ff79e6cc077ffba5f23bb74
            Previous: 47cf022b180526de8f7d0ec5951f00181d2a2853c68305c3c1fbdede2eaec30d
            Data: data2
            Nonce: 0
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
