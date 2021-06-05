'''
@author : Suyash Shrivastava
'''
import sys

def switch_case_mapper(case_key, attr1, attr2):
    """
    >>> switch_case_mapper('add',1,2)
    3
    >>> switch_case_mapper('multiply',1,2)
    2
    >>> switch_case_mapper('divide',1,2)
    0.5
    >>> switch_case_mapper('modulo',1,2)
    1
    >>> switch_case_mapper('subtract',1,2)
    -1
    >>> switch_case_mapper('invalid case',1,2)
    'Case Not Found!'
    """
    method = getattr(sys.modules[__name__], case_key, lambda  x,y: "Case Not Found!")
    return method(attr1, attr2)

def add(attr1, attr2):
    return attr1+attr2

def subtract(attr1, attr2):
    return attr1-attr2

def multiply(attr1, attr2):
    return attr1*attr2

def modulo(attr1, attr2):
    return attr1%attr2

def divide(attr1, attr2):
    return attr1/attr2


if __name__ == "__main__":
    switch_case_mapper('multiply',1,2)
    switch_case_mapper('add',1,2)
    switch_case_mapper('subtract',1,2)
    switch_case_mapper('divide',1,2)
    switch_case_mapper('modulo',1,2)
    switch_case_mapper('invalid case',1,2)