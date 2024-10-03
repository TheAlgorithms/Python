from __future__ import annotations
from collections import deque
from typing import List, Dict


class State:
    """Represents a state in the Aho-Corasick automaton."""

    def __init__(self, value: str):
        self.value = value
        self.next_states: List[int] = []
        self.fail_state: int = 0
        self.output: List[str] = []


class Automaton:
    def __init__(self, keywords: List[str]):
        self.adlist: List[State] = [State("")]  # Initial root state
        for keyword in keywords:
            self.add_keyword(keyword)
        self.set_fail_transitions()

    def find_state_by_character(self, current_state: int, char: str) -> int | None:
        """Find the next state for the given character."""
        for state in self.adlist[current_state].next_states:
            if char == self.adlist[state].value:
                return state
        return None

    def add_keyword(self, keyword: str) -> None:
        """Add a keyword to the automaton."""
        current_state = 0
        for character in keyword:
            next_state = self.find_state_by_character(current_state, character)
            if next_state is None:
                new_state = State(character)
                self.adlist.append(new_state)
                self.adlist[current_state].next_states.append(len(self.adlist) - 1)
                current_state = len(self.adlist) - 1
            else:
                current_state = next_state
        self.adlist[current_state].output.append(keyword)

    def set_fail_transitions(self) -> None:
        """Set fail transitions for the automaton states."""
        q: deque = deque()
        for node in self.adlist[0].next_states:
            q.append(node)
            self.adlist[node].fail_state = 0

        while q:
            r = q.popleft()
            for child in self.adlist[r].next_states:
                q.append(child)
                state = self.adlist[r].fail_state
                while (
                    self.find_state_by_character(state, self.adlist[child].value)
                    is None
                    and state != 0
                ):
                    state = self.adlist[state].fail_state

                fail_state = self.find_state_by_character(
                    state, self.adlist[child].value
                )
                self.adlist[child].fail_state = (
                    fail_state if fail_state is not None else 0
                )
                self.adlist[child].output.extend(
                    self.adlist[self.adlist[child].fail_state].output
                )

    def search_in(self, string: str) -> Dict[str, List[int]]:
        """
        Search for keywords in the given string.

        Returns a dictionary with keywords and the list of their occurrences.

        Example:
        >>> A = Automaton(["what", "hat", "ver", "er"])
        >>> A.search_in("whatever, err ... , wherever")
        {'what': [0], 'hat': [1], 'ver': [5, 25], 'er': [6, 10, 22, 26]}
        """
        result: Dict[str, List[int]] = {}
        current_state = 0

        for i in range(len(string)):
            while (
                self.find_state_by_character(current_state, string[i]) is None
                and current_state != 0
            ):
                current_state = self.adlist[current_state].fail_state

            next_state = self.find_state_by_character(current_state, string[i])
            if next_state is None:
                current_state = 0
            else:
                current_state = next_state
                for key in self.adlist[current_state].output:
                    if key not in result:
                        result[key] = []
                    result[key].append(i - len(key) + 1)

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
