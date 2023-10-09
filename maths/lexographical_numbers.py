"""
Given an integer n, return all the numbers in the range [1, n]
sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.

Leetcode reference: https://leetcode.com/problems/lexicographical-numbers/
"""

def lexical_order(n: int) -> list[int]:
        """
        >>> lexicalOrder(13)
        [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

        >>> lexicalOrder(2)
        [1, 2]
        """

        """ Lexicographical order is a method for ordering strings or sequences
        of characters according to their position in the alphabet.
        """

        numbers=[str(i) for i in range(1,n+1)]
        numbers.sort()
        res=list(map(int, numbers))
        return res

if __name__ == "__main__":
    from doctest import testmod

    testmod()
