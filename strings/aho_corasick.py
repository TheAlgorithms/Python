from __future__ import annotations

from collections import deque


class Automaton:
    def __init__(self, keywords: list[str]):
        self.adlist: list[dict] = []
        self.adlist.append(
            {"value": "", "next_states": [], "fail_state": 0, "output": []}
        )

        for keyword in keywords:
            self.add_keyword(keyword)
        self.set_fail_transitions()

    def find_next_state(self, current_state: int, char: str) -> int | None:
        for state in self.adlist[current_state]["next_states"]:
            if char == self.adlist[state]["value"]:
                return state
        return None

    def add_keyword(self, keyword: str) -> None:
        current_state = 0
        for character in keyword:
            next_state = self.find_next_state(current_state, character)
            if next_state is None:
                self.adlist.append(
                    {
                        "value": character,
                        "next_states": [],
                        "fail_state": 0,
                        "output": [],
                    }
                )
                self.adlist[current_state]["next_states"].append(len(self.adlist) - 1)
                current_state = len(self.adlist) - 1
            else:
                current_state = next_state
        self.adlist[current_state]["output"].append(keyword)

    def set_fail_transitions(self) -> None:
        q: deque = deque()
        for node in self.adlist[0]["next_states"]:
            q.append(node)
            self.adlist[node]["fail_state"] = 0
        while q:
            r = q.popleft()
            for child in self.adlist[r]["next_states"]:
                q.append(child)
                state = self.adlist[r]["fail_state"]
                while (
                    self.find_next_state(state, self.adlist[child]["value"]) is None
                    and state != 0
                ):
                    state = self.adlist[state]["fail_state"]
                self.adlist[child]["fail_state"] = self.find_next_state(
                    state, self.adlist[child]["value"]
                )
                if self.adlist[child]["fail_state"] is None:
                    self.adlist[child]["fail_state"] = 0
                self.adlist[child]["output"] = (
                    self.adlist[child]["output"]
                    + self.adlist[self.adlist[child]["fail_state"]]["output"]
                )

    def search_in(self, string: str) -> dict[str, list[int]]:
        """
        >>> A = Automaton(["what", "hat", "ver", "er"])
        >>> A.search_in("whatever, err ... , wherever")
        {'what': [0], 'hat': [1], 'ver': [5, 25], 'er': [6, 10, 22, 26]}
        """
        result: dict = {}  # returns a dict with keywords and list of its occurrences
        current_state = 0
        for i in range(len(string)):
            while (
                self.find_next_state(current_state, string[i]) is None
                and current_state != 0
            ):
                current_state = self.adlist[current_state]["fail_state"]
            next_state = self.find_next_state(current_state, string[i])
            if next_state is None:
                current_state = 0
            else:
                current_state = next_state
                for key in self.adlist[current_state]["output"]:
                    if key not in result:
                        result[key] = []
                    result[key].append(i - len(key) + 1)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
