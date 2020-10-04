import json
import sys

# A utility file for all basic plain text and JSON file IO


def touch_file(file_name: str) -> None:
    """
    Touch file:
    Checks if the file file_name exist else tries to create it.
    Similar to touch command on linux.
    """
    try:
        with open(file_name):
            pass
    except FileNotFoundError:
        try:
            with open(file_name, "w"):
                pass
        except IOError as ioe:
            sys.exit("{}: Unable to create {}".format(ioe, file_name))
    except IOError as ioe:
        sys.exit("{}: Unable to read file {}".format(ioe, file_name))


def clear_file(file_name: str) -> None:
    """
    Clear file:
    A utility function to clear the contents of the file file_name.
    """
    try:
        with open(file_name, "w"):
            pass
    except IOError as ioe:
        sys.exit("{}: Unable to create file {}".format(ioe, file_name))


def dump_json_to_file(data: object, file_name: str) -> None:
    """
    Dump JSON to file:
    - Creates the file file_name if it doesn't exist already.
    - Clears the content of the file file_name.
    - Converts the data object into JSON format and dumps it into the file file_name.
    """
    touch_file(file_name)
    with open(file_name, "w") as write_file:
        write_file.write(json.dumps(data, indent=4) + "\n")


def load_json_from_file(file_name: str) -> str:
    """
    Load JSON from file:
    - Creates the file file_name if it doesn't exist already.
    - Read the content of the file file_name.
    - Converts the data inside the file_name into JSON format and returns it.
    - Returns str representation of an empty dict if the file is empty.
    """
    touch_file(file_name)
    with open(file_name) as readfile:
        return readfile.read() or str({})


def read_lines_strip_return(
    file_name: str, split: str = None, index: int = None
) -> list:
    """
    Read Lines from file:
    - Read the content of the file file_name using readlines.
    - If the parameter split is specified then each line is split using it.
    - If the index is specified, index from the above split line is returned.
    - Returns list of lines from file_name matching the split and index conditions.
    """
    try:
        with open(file_name) as readfile:
            lines = readfile.readlines()
            res = list()
            for line in lines:
                line = line.strip()
                if line != "":
                    if split is not None:
                        line = line.split(split)
                        if index is None:
                            res.append(line)
                        else:
                            res.append(line[index])
                    else:
                        res.append(line)
        return res
    except FileNotFoundError as fn_fe:
        sys.exit("{}: {}".format(fn_fe, file_name))
    except IOError as ioe:
        sys.exit("{}: Unable to read file {}".format(ioe, file_name))


def read_file(file_name: str) -> str:
    """
    Read file:
    - Read the content of the file file_name using read and returns it.
    """
    try:
        with open(file_name) as readfile:
            return readfile.read().strip()
    except FileNotFoundError as fn_fe:
        sys.exit("{}: {}".format(fn_fe, file_name))
    except IOError as ioe:
        sys.exit("{}: Unable to read file {}".format(ioe, file_name))


def append_line_to_file(file_name: str, line: str) -> None:
    """
    Append Line to file:
    - Checks if the file exists and creates if not.
    - Opens the file in append mode and appends the line at the ending of file_name.
    """
    touch_file(file_name)
    with open(file_name, "a") as append_file:
        append_file.write(line + "\n")


def append_line_to_file_if_doesnt_exist(file_name: str, line: str) -> None:
    """
    Append Line to file only if not exists:
    - Checks if the file exists and creates if not.
    - Checks if the line already exists in the file file_name.
    - Only appends the line if nor already present in file_name.
    """
    touch_file(file_name)
    lines = read_lines_strip_return(file_name)
    if line not in lines:
        with open(file_name, "a") as append_file:
            append_file.write(line + "\n")


def check_file_exists(file_name: str) -> bool:
    """
    Check if file exists:
    - Checks whether the file file_name exists or not.
    """
    try:
        with open(file_name):
            pass
        return True
    except FileNotFoundError:
        return False
    except IOError:
        return False


def convert_int_to_dotted_str(number: int) -> str:
    """
    Convert int into dotted str:
    - This function takes an integer and converts it into a dotted str.
    - Useful in converting a number into version.
    - Eg: 123 -> "1.2.3"
    """
    res = list()
    for digit in str(number):
        res.append(digit)
    return ".".join(res)


def convert_dotted_str_to_int(dotted_str: str) -> int:
    """
    Convert dotted str into int:
    - This function takes a dotted str and converts into an int.
    - Useful in converting version into a number.
    - Eg: "1.2.3" -> 123
    """
    return int("".join(dotted_str.split(".")))
