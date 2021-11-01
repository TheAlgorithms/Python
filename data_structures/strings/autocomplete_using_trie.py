END = "#"


class Trie:
    def __init__(self):
        self._trie = {}

    def insert_word(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[END] = True

    def find_word(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []
        return self._elements(trie)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == END:
                sub_result = [" "]
            else:
                sub_result = [c + s for s in self._elements(v)]
            result.extend(sub_result)
        return tuple(result)


trie = Trie()
words = ("depart", "detergent", "daring", "dog", "deer", "deal")
for word in words:
    trie.insert_word(word)


def autocomplete_using_trie(s):
    """
    >>> trie = Trie()
    >>> for word in words:
    ...     trie.insert_word(word)
    ...
    >>> matches = autocomplete_using_trie("de")

    "detergent " in matches
    True
    "dog " in matches
    False
    """
    suffixes = trie.find_word(s)
    return tuple(s + w for w in suffixes)


def main():
    print(autocomplete_using_trie("de"))


if __name__ == "__main__":
    main()
