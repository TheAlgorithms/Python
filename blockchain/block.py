from hashlib import sha256


def updatehash(*args):
    """
    This function takes in arbitary number of arguments and returns a sha256 hash object in hexadecimal.
    - Exmple :
        >>> updatehash(1,2,3,4,5)
        '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'
    -doctest :
        >>> updatehash(1,2,3,4,5)
        '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'

    """
    # create a hashing text
    hashing_text = ""
    # create a hashing object
    h = sha256()

    # loop through each argument and hash
    for arg in args:
        hashing_text += str(arg)

    # update the hashing object with the hashing text
    h.update(hashing_text.encode("utf-8"))
    # return the hexadeciaml hash
    return h.hexdigest()


# block class
class Block:
    """
    Block class represents each block in the blockchain and it's attributes.
    Atruibutes:
        - data : data to be stored in the block
        - number : the number of the block
        - previous_hash : the hash of the previous block
        - nonce : the nonce of the block ( number to make the hash of the block valid)
    Methods:
        - hash : returns the hash of the block
        - __str__ : returns a string representation of the block
    """

    # __init__ is a special method in python that is called when an object is created.
    def __init__(self, number=0, previous_hash="0" * 64, data=None, nonce=0):
        self.data = data
        self.number = number
        self.previous_hash = previous_hash
        self.nonce = nonce

    # hash method (returns the hash of the block)
    def hash(self):
        return updatehash(self.number, self.previous_hash, self.data, self.nonce)

    # __str__ is a special method in python that is called when an object is printed.
    def __str__(self):
        return str(
            "Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n"
            % (self.number, self.hash(), self.previous_hash, self.data, self.nonce)
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
