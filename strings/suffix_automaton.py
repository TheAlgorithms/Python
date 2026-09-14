"""
Suffix Automaton (SAM) for String Processing.

Reference: https://en.wikipedia.org/wiki/Suffix_automaton
Reference: https://cp-algorithms.com/string/suffix-automaton.html

A Suffix Automaton is the minimal Deterministic Finite Automaton (DFA) that recognizes
all suffixes (and substrings) of a given string in O(N) time and O(N) space.
"""

from dataclasses import dataclass, field


@dataclass
class State:
    """
    State (node) in a Suffix Automaton.
    """

    length: int = 0
    link: int = -1
    next: dict[str, int] = field(default_factory=dict)


class SuffixAutomaton:
    """
    Suffix Automaton data structure.

    >>> sam = SuffixAutomaton("abacaba")
    >>> sam.contains("abac")
    True
    >>> sam.contains("caba")
    True
    >>> sam.contains("xyz")
    False
    >>> sam.count_distinct_substrings()
    21
    >>> sam.count_occurrences("aba")
    2
    >>> sam.count_occurrences("a")
    4
    >>> SuffixAutomaton("")
    Traceback (most recent call last):
        ...
    ValueError: Input string must not be empty.
    """

    def __init__(self, string: str) -> None:
        if not string:
            raise ValueError("Input string must not be empty.")

        self.states: list[State] = [State(length=0, link=-1)]
        self.last: int = 0
        self.string: str = string

        for char in string:
            self.extend(char)

    def extend(self, char: str) -> None:
        """
        Extend the Suffix Automaton by appending character char.
        Time Complexity: O(1) amortized
        """
        curr = len(self.states)
        self.states.append(State(length=self.states[self.last].length + 1))

        prev_state = self.last
        while prev_state != -1 and char not in self.states[prev_state].next:
            self.states[prev_state].next[char] = curr
            prev_state = self.states[prev_state].link

        if prev_state == -1:
            self.states[curr].link = 0
        else:
            next_state = self.states[prev_state].next[char]
            if self.states[prev_state].length + 1 == self.states[next_state].length:
                self.states[curr].link = next_state
            else:
                clone = len(self.states)
                self.states.append(
                    State(
                        length=self.states[prev_state].length + 1,
                        link=self.states[next_state].link,
                    )
                )
                self.states[clone].next = dict(self.states[next_state].next)

                while (
                    prev_state != -1
                    and self.states[prev_state].next.get(char) == next_state
                ):
                    self.states[prev_state].next[char] = clone
                    prev_state = self.states[prev_state].link

                self.states[next_state].link = clone
                self.states[curr].link = clone

        self.last = curr

    def contains(self, pattern: str) -> bool:
        """
        Check if pattern exists as a substring in O(|pattern|) time.

        >>> sam = SuffixAutomaton("banana")
        >>> sam.contains("nan")
        True
        >>> sam.contains("apple")
        False
        """
        curr = 0
        for char in pattern:
            if char not in self.states[curr].next:
                return False
            curr = self.states[curr].next[char]
        return True

    def count_distinct_substrings(self) -> int:
        """
        Compute total number of distinct substrings in O(N) time.

        >>> sam = SuffixAutomaton("abc")
        >>> sam.count_distinct_substrings()
        6
        >>> SuffixAutomaton("aaaa").count_distinct_substrings()
        4
        """
        total = 0
        for state in self.states[1:]:
            total += state.length - self.states[state.link].length
        return total

    def count_occurrences(self, pattern: str) -> int:
        """
        Count occurrences of pattern as a substring in the text in O(N + |pattern|) time

        >>> sam = SuffixAutomaton("banana")
        >>> sam.count_occurrences("an")
        2
        >>> sam.count_occurrences("na")
        2
        >>> sam.count_occurrences("banana")
        1
        >>> sam.count_occurrences("xyz")
        0
        """
        curr = 0
        for char in pattern:
            if char not in self.states[curr].next:
                return 0
            curr = self.states[curr].next[char]

        # Standard endpos size calculation via suffix link tree
        occurrences = [0] * len(self.states)
        order = sorted(
            range(len(self.states)),
            key=lambda state_index: self.states[state_index].length,
            reverse=True,
        )

        # Mark initial end positions of prefix states
        temp_last = 0
        for char in self.string:
            temp_last = self.states[temp_last].next[char]
            occurrences[temp_last] = 1

        # Push endpos sizes up the suffix link tree
        for state_index in order:
            if self.states[state_index].link != -1:
                occurrences[self.states[state_index].link] += occurrences[state_index]

        return occurrences[curr]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
