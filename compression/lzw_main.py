from .lzw import LZW
import sys


class Main_LZW:
    if __name__ == "__main__":
        zipper = LZW()
        print("" + zipper.compression(sys.argv[1]))
        # print("" + zipper.decompression(sys.argv[1]))
        # zipper.dictionary.print_dictionary()
