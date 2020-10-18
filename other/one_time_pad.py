"""https://en.wikipedia.org/wiki/One-time_pad"""
import secrets as sc
import typing as tp


def encryption(
    original_data: str, byteorder: str = "big", token: str = None
) -> Tuple[int, int]:
    """
    2Key-Encrypting of a string based on XOR algorithm.

    Parameters
    ----------
    original_data : str
        Original text data to encrypt.
    byteorder : str, optional
        Can be "little" or "big", by default "big"
    token : str, optional
        Token-pattern as second key-element for the encryption, by default None.
        If none, a random token will be generated based on the length of the original
        data. If not none, the token should have the same length as the original_data
        at least.

    Returns
    -------
    encrypted_data : int
        The original text data as encrypted integer.
    encrypted_token : int
        The original token as encrypted integer.
    """
    original_data_as_bytes: bytes = original_data.encode()
    original_data_as_key: int = int.from_bytes(original_data_as_bytes, byteorder)

    if token is not None:
        token_as_bytes: bytes = token.encode()

    else:
        token_as_bytes: bytes = sc.token_bytes(len(original_data))
    encrypted_token: int = int.from_bytes(token_as_bytes, byteorder)

    encrypted_data: int = original_data_as_key ^ encrypted_token
    return encrypted_data, encrypted_token


def decryption(reference_key: int, token_key: int, byteorder: str = "big") -> str:
    """
    2Key-Decrypting of a string based on XOR algorithm.

    Parameters
    ----------
    reference_key : int
        Reference key with the encrypted data as integer
    token_key : int
        Encrypted token as integer.
    byteorder : str, optional
        Can be "little" or "big", by default "big"

    Returns
    -------
    str
        Return the decrypted data as a string

    Examples
    --------
    >>> key_1, key_2 = encryption("test_key")
    >>> decryption(key_1, key_2)
    'test_key'
    """
    decrypted: int = reference_key ^ token_key
    if decrypted:
        return decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder).decode()
    return None


if __name__ == "__main__":
    # With given random-token
    key_1, key_2 = encryption("test_key")
    print(decryption(key_1, key_2))
    # With given token
    key_1, key_2 = encryption("test_key", token="2342323")
    print(decryption(key_1, key_2))
