from __future__ import annotations


class SuffixAutomaton:
    """
    Suffix Automaton data structure for efficient substring counting and searching.

    Usage:
    sa = SuffixAutomaton()
    sa.extend('abc')
    terminal_states = sa.terminal()
    is_found = sa.find('ab')

    :param alpha: Number of characters in the alphabet
    (default is 26 for lowercase English letters)
    :param first: ASCII value of the first character in the alphabet (default is 'a')
    """

    def __init__(self, alpha: int = 26, first: int = ord("a")):
        self.alpha = alpha
        self.first = first
        self.substrings = 0
        self.last = 0
        self.st = [self.Node(0, -1, [0] * self.alpha)]

    class Node:
        def __init__(self, length: int, link: int, next_states: list[int]):
            self.len = length
            self.link = link
            self.next = next_states

    def extend(self, c: str) -> None:
        """
        Extend the suffix automaton with a new character.

        :param c: The character to extend with.

        >>> sa = SuffixAutomaton()
        >>> sa.add('aabaaab')
        >>> terminal_states = [7, 3, 0]
        >>> sa.terminal() == terminal_states
        True
        >>> sa.find('a')
        True
        >>> sa.find('b')
        True
        >>> sa.find('c')
        False
        >>> sa.find('aa')
        True
        >>> sa.find('ab')
        True
        >>> sa.find('aaaab')
        False
        >>> sa.find('bab')
        False
        >>> sa.find('baaaab')
        False
        >>> sa.find('baaaaab')
        False
        >>> sa.extend('xy')  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        ValueError: Invalid input to extend method. Only single characters are allowed.
        """
        if len(c) != 1:
            raise ValueError("The character to extend with must be a single character.")

        char_value = ord(c) - self.first
        cur = len(self.st)
        p, q = self.last, 0

        self.st.append(self.Node(self.st[p].len + 1, -1, [0] * self.alpha))

        while p != -1 and not self.st[p].next[char_value]:
            self.st[p].next[char_value] = cur
            p = self.st[p].link

        if p == -1:
            self.st[cur].link = 0
            self.substrings += self.st[cur].len
        else:
            q = self.st[p].next[char_value]

            if self.st[p].len + 1 == self.st[q].len:
                self.st[cur].link = q
                self.substrings += self.st[cur].len - self.st[q].len
            else:
                clone = len(self.st)
                self.st.append(
                    self.Node(self.st[p].len + 1, self.st[q].link, self.st[q].next[:])
                )
                self.substrings += self.st[clone].len - self.st[self.st[clone].link].len

                while p != -1 and self.st[p].next[char_value] == q:
                    self.st[p].next[char_value] = clone
                    p = self.st[p].link

                self.substrings -= self.st[q].len - self.st[self.st[q].link].len
                self.st[q].link = self.st[cur].link = clone
                self.substrings += (
                    self.st[q].len
                    - self.st[self.st[q].link].len
                    + self.st[cur].len
                    - self.st[self.st[cur].link].len
                )

        self.last = cur

    def add(self, s: str) -> None:
        """
        Add a string to the suffix automaton.

        :param s: The string to add.
        """
        for i in range(len(s)):
            self.extend(s[i])

    def terminal(self) -> list[int]:
        """
        Get the terminal states of the suffix automaton.

        :return: List of terminal states.
        """
        p = self.last
        terminal_states = []
        while p >= 0:
            terminal_states.append(p)
            p = self.st[p].link
        return terminal_states

    def find(self, s: str) -> bool:
        """
        Check if a string is present in the suffix automaton.

        :param s: The string to search for.
        :return: True if the string is found, False otherwise.
        """
        p = 0
        for j in range(len(s)):
            if not self.st[p].next[ord(s[j]) - self.first]:
                return False
            p = self.st[p].next[ord(s[j]) - self.first]
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
