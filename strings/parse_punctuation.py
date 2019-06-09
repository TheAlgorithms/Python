# parse_punctuation.py

import codecs
import string


def remove_punc(path, remove_ctrl_char=False):
    """
    :param path: text file path
    :type path: str
    :param remove_ctrl_char: remove control characters (\n, \r, \t)
    :type remove_ctrl_char: bool
    :return: string

    Takes a string file and removes punctuation from string.punctuation
    The dash is replaced with a space to preserve hyphenated words
    """
    text_string = _open_file(path)
    if text_string is not None:
        str_parse = string.punctuation.translate({ord('-'): None})
        trans_dict = str.maketrans({key: None for key in str_parse})
        trans_dict[ord('-')] = ' '
        if remove_ctrl_char:
            return _remove_ctrl_char(text_string.translate(trans_dict))
        return text_string.translate(trans_dict)
    else:
        raise OSError()


def _open_file(path):
    with codecs.open(path.replace("\\", "/"), encoding='utf-8', mode='r') as txtfile:
        tem = txtfile.read()
    return tem


def _remove_ctrl_char(string_in):
    if string_in is not None:
        control_characters = str.maketrans("\n\t\r", "   ")
        return string_in.translate(control_characters)
