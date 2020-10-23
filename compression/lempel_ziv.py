"""
    One of the several implementations of Lempel–Ziv–Welch compression algorithm
    https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
"""

import math
import os
import sys


def read_file_binary(file_path: str) -> str:
    """
    Reads given file as bytes and returns them as a long string
    """
    result = ""
    try:
        with open(file_path, "rb") as binary_file:
            data = binary_file.read()
        for dat in data:
            curr_byte = f"{dat:08b}"
            result += curr_byte
        return result
    except OSError:
        print("File not accessible")
        sys.exit()


def add_key_to_lexicon(
    lexicon: dict, curr_string: str, index: int, last_match_id: int
) -> None:
    """
    Adds new strings (curr_string + "0",  curr_string + "1") to the lexicon
    """
    lexicon.pop(curr_string)
    lexicon[curr_string + "0"] = last_match_id

    if math.log2(index).is_integer():
        for curr_key in lexicon:
            lexicon[curr_key] = "0" + lexicon[curr_key]

    lexicon[curr_string + "1"] = bin(index)[2:]


def compress_data(data_bits: str) -> str:
    """
    Compresses given data_bits using Lempel–Ziv–Welch compression algorithm
    and returns the result as a string
    """
    lexicon = {"0": "0", "1": "1"}
    result, curr_string = "", ""
    index = len(lexicon)

    for i in range(len(data_bits)):
        curr_string += data_bits[i]
        if curr_string not in lexicon:
            continue

        last_match_id = lexicon[curr_string]
        result += last_match_id
        add_key_to_lexicon(lexicon, curr_string, index, last_match_id)
        index += 1
        curr_string = ""

    while curr_string != "" and curr_string not in lexicon:
        curr_string += "0"

    if curr_string != "":
        last_match_id = lexicon[curr_string]
        result += last_match_id

    return result


def add_file_length(source_path: str, compressed: str) -> str:
    """
    Adds given file's length in front (using Elias  gamma coding) of the compressed
    string
    """
    file_length = os.path.getsize(source_path)
    file_length_binary = bin(file_length)[2:]
    length_length = len(file_length_binary)

    return "0" * (length_length - 1) + file_length_binary + compressed


def write_file_binary(file_path: str, to_write: str) -> None:
    """
    Writes given to_write string (should only consist of 0's and 1's) as bytes in the
    file
    """
    byte_length = 8
    try:
        with open(file_path, "wb") as opened_file:
            result_byte_array = [
                to_write[i : i + byte_length]
                for i in range(0, len(to_write), byte_length)
            ]

            if len(result_byte_array[-1]) % byte_length == 0:
                result_byte_array.append("10000000")
            else:
                result_byte_array[-1] += "1" + "0" * (
                    byte_length - len(result_byte_array[-1]) - 1
                )

            for elem in result_byte_array:
                opened_file.write(int(elem, 2).to_bytes(1, byteorder="big"))
    except OSError:
        print("File not accessible")
        sys.exit()


def compress(source_path, destination_path: str) -> None:
    """
    Reads source file, compresses it and writes the compressed result in destination
    file
    """
    data_bits = read_file_binary(source_path)
    compressed = compress_data(data_bits)
    compressed = add_file_length(source_path, compressed)
    write_file_binary(destination_path, compressed)


if __name__ == "__main__":
    compress(sys.argv[1], sys.argv[2])
