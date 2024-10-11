#!/usr/bin/env python

import argparse
import os
from typing import List

class FlashSorter:
    def __init__(self, filename: str):
        self.filename = filename

    def sort(self) -> None:
        # Main logic for flash sort goes here
        pass

    def _flash_sort(self, data: List[int]) -> List[int]:
        # Implement the flash sort algorithm
        pass

    def _read_file(self) -> List[int]:
        with open(self.filename, 'r') as file:
            return [int(line.strip()) for line in file]

    def _write_file(self, data: List[int]) -> None:
        with open(self.filename + ".out", 'w') as file:
            for number in data:
                file.write(f"{number}\n")

def parse_memory(string: str) -> int:
    if string[-1].lower() == "k":
        return int(string[:-1]) * 1024
    elif string[-1].lower() == "m":
        return int(string[:-1]) * 1024 * 1024
    elif string[-1].lower() == "g":
        return int(string[:-1]) * 1024 * 1024 * 1024
    else:
        return int(string)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--mem", help="amount of memory to use for sorting", default="100M"
    )
    parser.add_argument(
        "filename", metavar="<filename>", nargs=1, help="name of file to sort"
    )
    args = parser.parse_args()

    sorter = FlashSorter(args.filename[0])
    data = sorter._read_file()
    sorted_data = sorter._flash_sort(data)
    sorter._write_file(sorted_data)

if __name__ == "__main__":
    main()
