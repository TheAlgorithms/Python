"""
RC4 (Rivest Cipher 4) Stream Cipher

RC4 is a symmetric stream cipher designed by Ron Rivest in 1987. It was widely
used in protocols such as SSL/TLS and WEP before being deprecated due to
statistical biases in its keystream. Understanding RC4 remains important for
security education, particularly for studying why stream cipher design matters.

The algorithm has two phases:
1. Key Scheduling Algorithm (KSA): Initialises a 256-byte permutation using
   the key.
2. Pseudo-Random Generation Algorithm (PRGA): Produces keystream bytes by
   further permuting the state array.

Encryption and decryption are identical: XOR the keystream with the plaintext
to encrypt, or XOR with the ciphertext to decrypt.

Reference:
  https://en.wikipedia.org/wiki/RC4

Security note:
  RC4 is cryptographically broken and must NOT be used in production systems.
  This implementation is provided for educational purposes only.
"""

from __future__ import annotations


def key_scheduling(key: list[int]) -> list[int]:
    """
    Perform the Key Scheduling Algorithm (KSA).

    Initialises a 256-byte identity permutation and scrambles it using the
    provided key bytes.

    Args:
        key: A list of integers (0-255) representing the key bytes.

    Returns:
        A 256-element permutation list (the initial state array S).

    >>> key_scheduling([1, 2, 3])
    ... # doctest: +ELLIPSIS
    [...]

    >>> len(key_scheduling([65, 66, 67]))
    256

    >>> key_scheduling([0]) == list(range(256))
    False
    """
    key_length = len(key)
    # Initialise the state array as the identity permutation
    state = list(range(256))
    j = 0
    for i in range(256):
        j = (j + state[i] + key[i % key_length]) % 256
        # Swap state[i] and state[j]
        state[i], state[j] = state[j], state[i]
    return state


def pseudo_random_generation(state: list[int], length: int) -> list[int]:
    """
    Perform the Pseudo-Random Generation Algorithm (PRGA).

    Generates a keystream of the requested length from the state array
    produced by the KSA.

    Args:
        state: A 256-element permutation list from key_scheduling().
        length: The number of keystream bytes to generate.

    Returns:
        A list of keystream bytes (integers 0-255).

    >>> state = list(range(256))
    >>> keystream = pseudo_random_generation(state, 5)
    >>> len(keystream)
    5
    >>> all(0 <= b <= 255 for b in keystream)
    True
    """
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        # Swap state[i] and state[j]
        state[i], state[j] = state[j], state[i]
        keystream.append(state[(state[i] + state[j]) % 256])
    return keystream


def encrypt(plaintext: str, key: str) -> list[int]:
    """
    Encrypt a plaintext string using RC4 with the given key.

    Converts the plaintext and key to byte lists, runs KSA and PRGA, then
    XORs the plaintext bytes with the keystream to produce ciphertext bytes.

    Args:
        plaintext: The message to encrypt (ASCII string).
        key: The encryption key (ASCII string, 1-256 characters).

    Returns:
        A list of integers representing the ciphertext bytes.

    Raises:
        ValueError: If the key is empty.

    >>> encrypt("Hello", "secret")
    [165, 83, 190, 112, 237]

    >>> encrypt("", "key")
    []

    >>> encrypt("Attack at dawn", "Key")
    [170, 235, 3, 224, 212, 95, 234, 19, 211, 57, 46, 73, 16, 216]
    """
    if not key:
        raise ValueError("Key must not be empty.")
    key_bytes = [ord(c) for c in key]
    plaintext_bytes = [ord(c) for c in plaintext]
    state = key_scheduling(key_bytes)
    keystream = pseudo_random_generation(state, len(plaintext_bytes))
    return [p ^ k for p, k in zip(plaintext_bytes, keystream)]


def decrypt(ciphertext: list[int], key: str) -> str:
    """
    Decrypt RC4 ciphertext bytes back to a plaintext string.

    RC4 decryption is identical to encryption: generate the same keystream
    and XOR it with the ciphertext bytes.

    Args:
        ciphertext: A list of integers (ciphertext bytes) from encrypt().
        key: The same key used during encryption.

    Returns:
        The decrypted plaintext as a string.

    Raises:
        ValueError: If the key is empty.

    >>> decrypt([165, 83, 190, 112, 237], "secret")
    'Hello'

    >>> decrypt([], "key")
    ''

    >>> decrypt([170, 235, 3, 224, 212, 95, 234, 19, 211, 57, 46, 73, 16, 216], "Key")
    'Attack at dawn'
    """
    if not key:
        raise ValueError("Key must not be empty.")
    key_bytes = [ord(c) for c in key]
    state = key_scheduling(key_bytes)
    keystream = pseudo_random_generation(state, len(ciphertext))
    return "".join(chr(c ^ k) for c, k in zip(ciphertext, keystream))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    message = "Hello, World!"
    secret_key = "mysecretkey"

    print(f"Original : {message}")
    encrypted = encrypt(message, secret_key)
    print(f"Encrypted: {encrypted}")
    decrypted = decrypt(encrypted, secret_key)
    print(f"Decrypted: {decrypted}")
    assert decrypted == message, "Decryption failed — output does not match original."
    print("Encrypt -> Decrypt round-trip successful.")
