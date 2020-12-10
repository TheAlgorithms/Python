# numpy should be install in you python environment
import numpy as np

def split(word):
    return list(word)

def decrypt(text, size):
    ptext = ''
    text = split(text)
    output = np.array(text)
    output.resize(size, size)
    output = output.transpose()
    output = output.flatten()
    for letter in output:
        if letter != '@':
            ptext += letter
    return ptext


def encrypt(text, size):
    if len(text) > size * size:
        return 'Cannot be encrypted [text size exceed array limits]'
    else:
        cypher = ''
        text = split(text)
        output = np.array(text)
        output.resize(size, size)
        for i in range(0, size):
            for j in range(0, size):
                if output[i][j] == '':
                    output[i][j] = '@'
        output = output.transpose()
        output = output.flatten()
        for letter in output:
            cypher += letter
        return cypher
