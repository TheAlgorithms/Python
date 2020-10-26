
"""
Created on Sun Oct 25 09:31:07 2020

@author: Krishna Chandu Akula

This file contains the code for counting set bits of a number
using Brain Kernighan Algorithm
"""

def num_of_set_bits(n):
    count = 0
    while n:
        n = n & (n - 1)
        count = count + 1
    return count


if __name__ == "__main__":

    assert 2 == num_of_set_bits(3)
    assert 1 == num_of_set_bits(64)
    assert 4 == num_of_set_bits(15)
