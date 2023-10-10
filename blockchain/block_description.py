from hashlib import sha256


def updatehash(*args: object) -> str:
    """
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

    def __init__(
        self,
        number: int,
        previous_hash: str = "0" * 64,
        data: object = None,
        nonce: int = 0,
    ) -> None:
        self.data = data
        self.number = number
        self.previous_hash = previous_hash
        self.nonce = nonce

    def hashdata(self) -> str:
        """
        Returns the hash of the block's data.

        >>> block1 = Block(1, "0"*64, "data1", 0)
        >>> block1.hashdata()
        '47cf022b180526de8f7d0ec5951f00181d2a2853c68305c3c1fbdede2eaec30d'
        """
        return updatehash(self.number, self.previous_hash, self.data, self.nonce)

    def __str__(self) -> str:
        """
        >>> block1 = Block(1, "0"*64, "data1", 0)
        >>> print(block1)
        Block#: 1
        Hash: 0000000000000000000000000000000000000000000000000000000000000000
        Previous: 0000000000000000000000000000000000000000000000000000000000000000
        Data: data1
        Nonce: 0
        """
        return (
            f"Block#: {self.number}\n"
            f"Hash: {self.previous_hash}\n"
            f"Previous: {self.previous_hash}\n"
            f"Data: {self.data}\n"
            f"Nonce: {self.nonce}"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
