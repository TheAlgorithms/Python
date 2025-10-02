#!/usr/bin/env python3
"""Four-Square cipher implementation with CLI encode/decode.

Usage examples:
  python -m ciphers.four_square_cipher encode --key1 EXAMPLE --key2 KEYWORD --text "attack at once"
  python -m ciphers.four_square_cipher decode --key1 EXAMPLE --key2 KEYWORD --text <ciphertext>

This is a digraph substitution cipher using four 5x5 squares with I/J merged.
"""
from __future__ import annotations

import argparse
import sys
from typing import List, Tuple

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def build_square(keyword: str) -> str:
    key = "".join(ch for ch in keyword.upper() if ch.isalpha())
    key = key.replace("J", "I")
    seen = set()
    sq = []
    for ch in key + ALPHABET:
        if ch not in seen:
            seen.add(ch)
            sq.append(ch)
    return "".join(sq[:25])


def clean_text(text: str) -> str:
    s = []
    for ch in text.upper():
        if ch.isalpha():
            s.append("I" if ch == "J" else ch)
    return "".join(s)


def to_digraphs(text: str) -> List[Tuple[str, str]]:
    t = clean_text(text)
    if len(t) % 2 == 1:
        t += "X"
    return [(t[i], t[i + 1]) for i in range(0, len(t), 2)]


def pos(square: str, ch: str) -> Tuple[int, int]:
    i = square.index(ch)
    return (i // 5, i % 5)


def encode_pair(a: str, b: str, sq1: str, sq2: str) -> Tuple[str, str]:
    # top-left: standard alphabet, top-right: sq1, bottom-left: sq2, bottom-right: standard
    r1, c1 = pos(ALPHABET, a)
    r2, c2 = pos(ALPHABET, b)
    return (sq1[r1 * 5 + c2], sq2[r2 * 5 + c1])


def decode_pair(a: str, b: str, sq1: str, sq2: str) -> Tuple[str, str]:
    # reverse mapping
    r1, c2 = pos(sq1, a)
    r2, c1 = pos(sq2, b)
    return (ALPHABET[r1 * 5 + c1], ALPHABET[r2 * 5 + c2])


def encode(key1: str, key2: str, text: str) -> str:
    sq1 = build_square(key1)
    sq2 = build_square(key2)
    out: List[str] = []
    for a, b in to_digraphs(text):
        x, y = encode_pair(a, b, sq1, sq2)
        out.extend([x, y])
    return "".join(out)


def decode(key1: str, key2: str, text: str) -> str:
    sq1 = build_square(key1)
    sq2 = build_square(key2)
    t = clean_text(text)
    if len(t) % 2 == 1:
        t += "X"
    out: List[str] = []
    for i in range(0, len(t), 2):
        a, b = t[i], t[i + 1]
        x, y = decode_pair(a, b, sq1, sq2)
        out.extend([x, y])
    return "".join(out)


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Four-Square cipher encode/decode")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_enc = sub.add_parser("encode")
    p_enc.add_argument("--key1", required=True)
    p_enc.add_argument("--key2", required=True)
    p_enc.add_argument("--text", required=True)

    p_dec = sub.add_parser("decode")
    p_dec.add_argument("--key1", required=True)
    p_dec.add_argument("--key2", required=True)
    p_dec.add_argument("--text", required=True)

    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.cmd == "encode":
        print(encode(args.key1, args.key2, args.text))
        return 0
    if args.cmd == "decode":
        print(decode(args.key1, args.key2, args.text))
        return 0
    return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
