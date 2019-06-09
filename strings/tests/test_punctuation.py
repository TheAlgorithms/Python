# test_punctuation.py
"""
If testing this within PyCharm, set the following:
1. Script path -- 'location where slash is stored'
2. Parameters -- run -vv -k tag:punctuation ..
3. Working directory -- set to location where this file is stored

If running from the command prompt, use the following:
slash run -vv -k tag:punctuation INSERT_PATH_TO_THIS_FILE_HERE_WITH_FILE_NAME.py
"""

import os
import slash
from .. import parse_punctuation

filepath = os.path.realpath(__file__).replace("\\", "/")
curr_dir = '/'.join(filepath.split("/")[:-1])


@slash.tag('punctuation')
def test_punc_random():
    with open(f'{curr_dir}/without_random_punctuation.txt') as file_out:
        output = file_out.read()
    remove_punct = parse_punctuation.remove_punc(f'{curr_dir}/with_random_punctuation.txt')
    assert remove_punct == output


@slash.tag('punctuation')
def test_punc():
    with open(f'{curr_dir}/without_story_punctuation.txt') as file_out:
        output = file_out.read()
    remove_punct = parse_punctuation.remove_punc(f'{curr_dir}/with_story_punctuation.txt')
    assert remove_punct == output


@slash.tag('punctuation')
def test_punc_and_ctrl_char():
    with open(f'{curr_dir}/without_story_punctuation_and_control_char.txt') as file_out:
        output = file_out.read()
    remove_punct = parse_punctuation.remove_punc(f'{curr_dir}/with_story_punctuation_and_control_char.txt',
                                                 remove_ctrl_char=True)
    assert remove_punct == output
