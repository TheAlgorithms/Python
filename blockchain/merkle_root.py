import hashlib
import doctest


def merkle_root(transactions):
    """
    Calculate the Merkle Root Hash for a list of transactions using the Merkle Tree algorithm.

    :param transactions: List of transaction data (bytes) to build the Merkle Tree from.
    :type transactions: list[bytes]
    :return: The Merkle Root Hash as a hexadecimal string.
    :rtype: str

    >>> transactions = [b"tx1", b"tx2", b"tx3", b"tx4"]
    >>> merkle_root(transactions).hex()
    '2a98ce6f17215458f14d2ef9a300f94c387f93a26e8ef272704103605329c4f19'
    """

    if not transactions:
        return None

    if len(transactions) == 1:
        return transactions[0]

    # Create a list to store the current level of Merkle tree nodes
    current_level = transactions

    while len(current_level) > 1:
        next_level = []

        # Combine pairs of transactions and hash them together
        for i in range(0, len(current_level), 2):
            if i + 1 < len(current_level):
                combined_hash = hashlib.sha256(
                    current_level[i] + current_level[i + 1]
                ).digest()
            else:
                combined_hash = hashlib.sha256(current_level[i]).digest()

            next_level.append(combined_hash)

        current_level = next_level

    return current_level[0]


if __name__ == "__main__":
    doctest.testmod()
