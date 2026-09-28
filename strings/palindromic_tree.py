"""Count distinct palindromic substrings with a palindromic tree (Eertree).

https://codeforces.com/blog/entry/13959
"""


def count_distinct_palindromic_substrings(text: str) -> int:
    """Return the number of different nonempty palindromic substrings.

    Each new tree node represents one distinct palindrome. The two initial
    nodes have lengths -1 and 0 and do not count as substrings. Dictionary
    transitions give expected O(n) time and O(n) space.

    >>> count_distinct_palindromic_substrings("banana")
    6
    >>> count_distinct_palindromic_substrings("ababa")
    5
    >>> count_distinct_palindromic_substrings("aaaa")
    4
    >>> count_distinct_palindromic_substrings("abc")
    3
    >>> count_distinct_palindromic_substrings("あいあ")
    3
    >>> count_distinct_palindromic_substrings("")
    0
    >>> count_distinct_palindromic_substrings(123)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # The -1 root always extends; the 0 root is the empty palindrome.
    lengths = [-1, 0]
    suffix_links = [0, 0]
    transitions: list[dict[str, int]] = [{}, {}]
    longest_suffix = 1

    for position, character in enumerate(text):
        current = longest_suffix
        while (
            position - 1 - lengths[current] < 0
            or text[position - 1 - lengths[current]] != character
        ):
            current = suffix_links[current]

        if character in transitions[current]:
            longest_suffix = transitions[current][character]
            continue

        new_node = len(lengths)
        new_length = lengths[current] + 2
        lengths.append(new_length)
        suffix_links.append(1)
        transitions.append({})
        transitions[current][character] = new_node

        if new_length > 1:
            candidate = suffix_links[current]
            while (
                position - 1 - lengths[candidate] < 0
                or text[position - 1 - lengths[candidate]] != character
            ):
                candidate = suffix_links[candidate]
            suffix_links[new_node] = transitions[candidate][character]

        longest_suffix = new_node

    return len(lengths) - 2
