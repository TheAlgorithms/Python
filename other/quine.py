#!/bin/python3
"""
Quine:

A quine is a computer program which takes no input and produces a copy of its
own source code as its only output (disregarding this docstring and the shebang).

More info on: https://en.wikipedia.org/wiki/Quine_(computing)
"""
print((lambda quine: quine % quine)("print((lambda quine: quine %% quine)(%r))"))
