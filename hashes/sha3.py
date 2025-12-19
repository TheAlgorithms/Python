"""
Pure Python SHA-3 (Keccak-f[1600]) implementation

Usage:
  python sha3.py --string "hello"
  python sha3.py --file data.bin
"""

import argparse
import struct
from typing import List


class KeccakSHA3:
    # Round constants
    _RC = [
        0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
        0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
        0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
        0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
        0x000000008000808B, 0x800000000000008B, 0x8000000000008089,
        0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
        0x000000000000800A, 0x800000008000000A, 0x8000000080008081,
        0x8000000000008080, 0x0000000080000001, 0x8000000080008008
    ]

    _ROT = [
        [0, 36, 3, 41, 18],
        [1, 44, 10, 45, 2],
        [62, 6, 43, 15, 61],
        [28, 55, 25, 21, 56],
        [27, 20, 39, 8, 14]
    ]

    def __init__(self, message: bytes, bits: int = 256):
        if bits not in (224, 256, 384, 512):
            raise ValueError("Invalid SHA3 length")

        self.msg = message
        self.out_bits = bits
        self.rate = 1600 - 2 * bits
        self.state = [[0] * 5 for _ in range(5)]

        self._absorb()
        self.digest = self._squeeze().hex()

    # ================= CORE =================

    @staticmethod
    def _rol(x: int, n: int) -> int:
        n %= 64
        return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

    def _permute(self):
        A = self.state

        for rnd in range(24):
            # θ
            C = [A[x][0] ^ A[x][1] ^ A[x][2] ^ A[x][3] ^ A[x][4] for x in range(5)]
            D = [C[(x - 1) % 5] ^ self._rol(C[(x + 1) % 5], 1) for x in range(5)]
            for x in range(5):
                for y in range(5):
                    A[x][y] ^= D[x]

            # ρ + π
            B = [[0] * 5 for _ in range(5)]
            for x in range(5):
                for y in range(5):
                    B[y][(2 * x + 3 * y) % 5] = self._rol(A[x][y], self._ROT[x][y])

            # χ
            for x in range(5):
                for y in range(5):
                    A[x][y] = B[x][y] ^ ((~B[(x + 1) % 5][y]) & B[(x + 2) % 5][y])

            # ι
            A[0][0] ^= self._RC[rnd]

    # ================= SPONGE =================

    def _pad(self, data: bytes) -> bytes:
        r = self.rate // 8
        buf = bytearray(data)
        buf.append(0x06)
        while len(buf) % r != r - 1:
            buf.append(0x00)
        buf.append(0x80)
        return bytes(buf)

    def _absorb(self):
        r = self.rate // 8
        padded = self._pad(self.msg)

        for off in range(0, len(padded), r):
            block = padded[off:off + r]
            for i in range(0, r, 8):
                lane = struct.unpack("<Q", block[i:i + 8])[0]
                x = (i // 8) % 5
                y = (i // 8) // 5
                self.state[x][y] ^= lane
            self._permute()

    def _squeeze(self) -> bytes:
        out = bytearray()
        r = self.rate // 8
        need = self.out_bits // 8

        while len(out) < need:
            for i in range(0, r, 8):
                x = (i // 8) % 5
                y = (i // 8) // 5
                out.extend(struct.pack("<Q", self.state[x][y]))
            if len(out) < need:
                self._permute()

        return bytes(out[:need])


# ================= CLI =================

def main():
    parser = argparse.ArgumentParser(description="SHA-3 hashing tool")
    parser.add_argument("-s", "--string", help="String input")
    parser.add_argument("-f", "--file", help="File input")
    parser.add_argument("-l", "--length", type=int, default=256,
                        choices=[224, 256, 384, 512])

    args = parser.parse_args()

    if args.file:
        with open(args.file, "rb") as f:
            data = f.read()
    else:
        data = (args.string or "Hello World").encode()

    h = KeccakSHA3(data, args.length)
    print(f"SHA3-{args.length}: {h.digest}")


if __name__ == "__main__":
    main()
