# test_punctuation.py

import slash
from .. import parse_punctuation


@slash.tag('punctuation')
def test_punc_random():
    with open("without_random_punctuation.txt") as file_out:
        output = file_out.read()
    remove_punct = parse_punctuation.remove_punc("with_random_punctuation.txt")
    assert remove_punct == output


@slash.tag('punctuation')
def test_punc():
    with open('without_story_punctuation.txt') as file_out:
        output = file_out.read()
    remove_punct = parse_punctuation.remove_punc("with_story_punctuation.txt")
    assert remove_punct == output


@slash.tag('punctuation')
def test_punc_and_ctrl_char():
    with open('without_story_punctuation_and_control_char.txt') as file_out:
        output = file_out.read()
    remove_punct = parse_punctuation.remove_punc("with_story_punctuation_and_control_char.txt", remove_ctrl_char=True)
    assert remove_punct == output