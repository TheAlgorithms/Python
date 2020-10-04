import json
import sys


def touch_file(file_name):
    try:
        with open(file_name):
            pass
    except FileNotFoundError:
        try:
            with open(file_name, "w"):
                pass
        except IOError as ioe:
            print(ioe)
            sys.stdout.flush()
            print("Unable to create file {}".format(file_name))
            sys.stdout.flush()
    except IOError as ioe:
        print(ioe)
        sys.stdout.flush()
        print("Unable to read file {}".format(file_name))
        sys.stdout.flush()


def clear_file(file_name):
    try:
        with open(file_name, "w"):
            pass
    except IOError as ioe:
        print(ioe)
        sys.stdout.flush()
        print("Unable to create file {}".format(file_name))
        sys.stdout.flush()


def dump_json_to_file(data, file_name):
    touch_file(file_name)
    with open(file_name, "w") as write_file:
        write_file.write(json.dumps(data, indent=4))
        write_file.write("\n")


def load_json_from_file(file_name):
    touch_file(file_name)
    with open(file_name) as readfile:
        content = readfile.read()
    if content == "":
        content = str(dict())
    content = json.loads(content)
    return content


def read_lines_strip_return(file_name, split=None, index=None):
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
    except FileNotFoundError:
        return "FileNotFoundError: {0}".format(file_name)
    except IOError as ioe:
        print(ioe)
        sys.stdout.flush()
        print("Unable to read file {}".format(file_name))
        sys.stdout.flush()


def read_file(file_name):
    try:
        with open(file_name) as readfile:
            return readfile.read().strip()
    except FileNotFoundError:
        return "FileNotFoundError: {0}".format(file_name)
    except IOError as ioe:
        print(ioe)
        sys.stdout.flush()
        print("Unable to read file {}".format(file_name))
        sys.stdout.flush()


def append_line_to_file(file_name, content):
    touch_file(file_name)
    with open(file_name, "a") as append_file:
        append_file.write(content + "\n")


def append_line_to_file_if_doesnt_exist(file_name, content):
    touch_file(file_name)
    lines = read_lines_strip_return(file_name)
    if content not in lines:
        with open(file_name, "a") as append_file:
            append_file.write(content + "\n")


def check_file_exists(file_name):
    try:
        with open(file_name):
            pass
        return True
    except FileNotFoundError:
        return False
    except IOError as ioe:
        print(ioe)
        sys.stdout.flush()
        print("Unable to read file {}".format(file_name))
        sys.stdout.flush()
        return False


def convert_int_to_dotted_str(number):
    res = list()
    for digit in str(number):
        res.append(digit)
    return ".".join(res)


def convert_dotted_str_to_int(dotted_str):
    return int("".join(dotted_str.split(".")))
