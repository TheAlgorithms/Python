#!/usr/bin/env python3
"""ADFGVX cipher implementation with CLI encode/decode.

Usage examples:
  python -m ciphers.adfgvx encode --key squarekeyword --transposition SECRET --text "attack at once"
  python -m ciphers.adfgvx decode --key squarekeyword --transposition SECRET --text <ciphertext>

The ADFGVX cipher uses a 6x6 Polybius square (A-Z + 0-9) and a columnar
transposition with a keyword.
"""
from __future__ import annotations

import argparse
import math
import sys
from typing import List

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
HEADERS = "ADFGVX"


def build_square(keyword: str) -> str:
    key = "".join(ch for ch in keyword.upper() if ch.isalnum())
    seen = set()
    square = []
    for ch in key + ALPHABET:
        if ch not in seen:
            seen.add(ch)
            square.append(ch)
    return "".join(square[:36])


def to_pairs(text: str, square: str) -> str:
    out = []
    for ch in text.upper():
        if not ch.isalnum():
            continue
        idx = square.find(ch)
        if idx == -1:
            continue
        r, c = divmod(idx, 6)
        out.append(HEADERS[r])
        out.append(HEADERS[c])
    return "".join(out)


def from_pairs(pairs: str, square: str) -> str:
    assert len(pairs) % 2 == 0
    out = []
    for i in range(0, len(pairs), 2):
        r = HEADERS.index(pairs[i])
        c = HEADERS.index(pairs[i + 1])
        out.append(square[r * 6 + c])
    return "".join(out)


def columnar_transpose_encrypt(text: str, key: str) -> str:
    key = "".join(ch for ch in key.upper() if ch.isalnum())
    order = sorted(range(len(key)), key=lambda i: (key[i], i))
    rows = math.ceil(len(text) / len(key))
    grid = [list(text[i * len(key):(i + 1) * len(key)]) for i in range(rows)]
    if grid:
        last = grid[-1]
        while len(last) < len(key):
            last.append("X")
    out = []
    for col in order:
        for r in range(rows):
            if col < len(grid[r]):
                out.append(grid[r][col])
    return "".join(out)


def columnar_transpose_decrypt(cipher: str, key: str) -> str:
    key = "".join(ch for ch in key.upper() if ch.isalnum())
    order = sorted(range(len(key)), key=lambda i: (key[i], i))
    rows = math.ceil(len(cipher) / len(key))
    cols = len(key)
    grid = [[None] * cols for _ in range(rows)]
    idx = 0
    for col in order:
        for r in range(rows):
            if idx < len(cipher):
                grid[r][col] = cipher[idx]
                idx += 1
    out = []
    for r in range(rows):
        for c in range(cols):
            ch = grid[r][c]
            if ch is not None:
                out.append(ch)
    return "".join(out)


def encode(key: str, transposition: str, text: str) -> str:
    square = build_square(key)
    pairs = to_pairs(text, square)
    return columnar_transpose_encrypt(pairs, transposition)


def decode(key: str, transposition: str, text: str) -> str:
    square = build_square(key)
    pairs = columnar_transpose_decrypt(text, transposition)
    if len(pairs) % 2 == 1:
        pairs = pairs[:-1]
    return from_pairs(pairs, square)


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ADFGVX cipher encode/decode")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_enc = sub.add_parser("encode")
    p_enc.add_argument("--key", required=True)
    p_enc.add_argument("--transposition", required=True)
    p_enc.add_argument("--text", required=True)

    p_dec = sub.add_parser("decode")
    p_dec.add_argument("--key", required=True)
    p_dec.add_argument("--transposition", required=True)
    p_dec.add_argument("--text", required=True)

    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.cmd == "encode":
        print(encode(args.key, args.transposition, args.text))
        return 0
    if args.cmd == "decode":
        print(decode(args.key, args.transposition, args.text))
        return 0
    return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
