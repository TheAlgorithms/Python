"""
for more information visit this url : https://www.geeksforgeeks.org/knapsack-encryption-algorithm-in-cryptography/
"""

from typing import List


def get_value_from_message_bits(s: str) -> int:
    """
    Return the value of message bits string s using public key
    >>> get_value_from_message_bits("00001")
    11
    >>> get_value_from_message_bits("10100")
    92
    """
    summ = 0
    for i in range(len(s)):
        if s[i] == "1":
            summ += public_key[i]
    return summ


def inverse(n: int, m: int) -> int:
    """
    Return the n inverse using n and m
    >>> inverse(67,89)
    4
    >>> inverse(55,97)
    30
    """
    i = 1
    while ((n * i) % m) != 1:
        i += 1
    return i


def get_message_bits_from_value(target: int) -> str:
    """
    Return the message bits string of value target using private key
    >>> get_message_bits_from_value(11)
    '00100'
    >>> get_message_bits_from_value(92)
    '11111'
    """
    mess = ""
    for i in range(len(private_key) - 1, -1, -1):
        curr = 0
        if target >= private_key[i]:
            curr = 1
            mess = "1" + mess
        if target < private_key[i]:
            curr = 0
            mess = "0" + mess
        target = target - private_key[i] * curr
    return mess


def decode(n_inv: int, m: int, coded: List[int]) -> str:
    """
    Return the decoded message bits string
    """
    ans = ""
    for i in coded:
        ans += get_message_bits_from_value((i * n_inv) % m)
    return ans


def encode(mess: str) -> List[int]:
    """
    Return the array of coded number
    """
    coded_message = []
    for k in range(len(mess) // len(private_key)):
        curr = mess[(k * len(private_key)) : (k * len(private_key)) + len(private_key)]
        coded_message.append(get_value_from_message_bits(curr))
    return coded_message


if __name__ == "__main__":
    private_key = [3, 5, 9, 20, 44]
    n = 67
    m = 89

    public_key = list(map(lambda x: (x * n) % m, private_key))

    message = "000011010011000011010111010110"
    coded_message = encode(message)

    print("public_key key : ", " ".join(map(str, public_key)))
    print("private_key key : ", " ".join(map(str, private_key)))
    print("message : ", message)
    print("coded message : ", " ".join(map(str, coded_message)))
    print("decoded message : ", decode(inverse(n, m), m, coded_message))
