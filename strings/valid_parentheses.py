import argparse
import textwrap
import re
from typing import Tuple, Dict


# Stack data-structure implementation
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


# Initialize stack
stack = Stack()


# Initializes defaults for regex and symbols
def initialize_default_regex_and_symbols() -> Tuple[str, Dict[str, str]]:
    return "^\\{\\}\\[\\]\\(\\)]*", {"{": "}", "[": "]", "(": ")"}


# Removes non parentheses-symbol characters from line
def sanitize_line(_line, _regex) -> str:
    return re.subn(_regex, "", _line)[0]


# Validates line against provided symbol dictionary
def validate_line(_line, _regex, _symbol_dict):
    __line = sanitize_line(_line, _regex)
    # Converts _line string to character array
    char_list = list(__line)
    for x in char_list:
        # If character is left parentheses
        # we are pushing it to the stack.
        # If it is right parentheses
        # we are pulling from stack and checking left parentheses.
        if x in _symbol_dict.keys():
            stack.push(x)
        else:
            # If we consumed all left parentheses from stack,
            # that means that parentheses on the right are not paired.
            if stack.is_empty():
                raise Exception("Submitted input contain non valid parentheses.")
            stack_key = stack.pop()
            # We get matching right parentheses for our left stack parentheses.
            stack_value = _symbol_dict.get(stack_key)
            # If matching right parentheses isn't equal
            # to our current right character we break.
            if not stack_value == x:
                raise Exception("Submitted input contain non valid parentheses.")


def validate_file(_file_path, _regex, _symbol_dict):
    file = open(_file_path, 'r')
    lines = file.readlines()

    # Strips the newline character
    for line in lines:
        validate_line(line, _regex, _symbol_dict)


def initialize_regex_and_symbols(_parentheses_symbol_param_arr) -> Tuple[str, Dict[str, str]]:
    _regex = ""
    _symbol_dict = {}
    for i in range(len(_parentheses_symbol_param_arr)):
        if not i % 2 == 0:
            _symbol_dict[_parentheses_symbol_param_arr[i - 1]] = _parentheses_symbol_param_arr[i]
        _regex += "\\" + _parentheses_symbol_param_arr[i]

    return "[^" + _regex + "]*", _symbol_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Open close contract checker',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            '''Example:
            -s "{some text[ some (other)] text}" # scan line usig default symbol set
            -s "{some text{ some other text}}" -l "{" -r "}" # scan line using custom symbol set
            -f "C:/Users/Username/Folder/file.txt" # scan file using default symbol set
            -f "C:/Users/Username/Folder/file.json" -l "{" -r "}" # scan file using custom symbol set'''))

    parser.add_argument('-s', '--string', help='read from line string')
    parser.add_argument('-f', '--file', help='read from file')
    parser.add_argument('-l', '--left', nargs='*', help='left symbol')
    parser.add_argument('-p', '--parentheses', nargs='*', help='parentheses symbols')

    args = vars(parser.parse_args())
    line_param = args['string']
    file_path_param = args["file"]
    parentheses_symbol_param = args["parentheses"]
    parentheses_symbol_param_arr = parentheses_symbol_param[0].split(",")

    if parentheses_symbol_param:
        if len(parentheses_symbol_param_arr) % 2 == 0:
            regex, symbol_dict = initialize_regex_and_symbols(parentheses_symbol_param_arr)
        else:
            regex, symbol_dict = initialize_default_regex_and_symbols()
        if line_param:
            validate_line(line_param, regex, symbol_dict)
        elif file_path_param:
            validate_file(file_path_param, regex, symbol_dict)
        if not stack.is_empty():
            raise Exception("Submitted input contain non valid parentheses.")
