# spiral_transposition.py

from __future__ import annotations
import math


def encrypt(plaintext: str) -> str:
    """
    Encrypts text by writing it in a square matrix
    and reading characters in spiral order.
    """
    text = "".join(ch for ch in plaintext.upper() if ch.isalpha())
    n = math.ceil(math.sqrt(len(text)))
    matrix = [["X"] * n for _ in range(n)]

    idx = 0
    for r in range(n):
        for c in range(n):
            if idx < len(text):
                matrix[r][c] = text[idx]
                idx += 1

    result = []
    top, left, bottom, right = 0, 0, n - 1, n - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    return "".join(result)


def decrypt(cipher_text: str) -> str:
    """
    Attempts to reconstruct the original message by reversing the spiral order.
    """
    L = len(cipher_text)
    n = math.ceil(math.sqrt(L))
    matrix = [[None] * n for _ in range(n)]

    top, left, bottom, right = 0, 0, n - 1, n - 1
    idx = 0
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            matrix[top][c] = cipher_text[idx]
            idx += 1
        top += 1
        for r in range(top, bottom + 1):
            matrix[r][right] = cipher_text[idx]
            idx += 1
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = cipher_text[idx]
                idx += 1
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = cipher_text[idx]
                idx += 1
            left += 1

    result = []
    for row in matrix:
        for ch in row:
            if ch:
                result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    while True:
        print("\n" + "-" * 10 + "\nSpiral Transposition Cipher\n" + "-" * 10)
        print("1. Encrypt\n2. Decrypt\n3. Quit")
        choice = input("Choice: ").strip()
        if choice == "1":
            pt = input("Plaintext: ")
            print("Ciphertext:", encrypt(pt))
        elif choice == "2":
            ct = input("Ciphertext: ")
            print("Recovered:", decrypt(ct))
        elif choice == "3":
            break
        else:
            print("Invalid option.")
