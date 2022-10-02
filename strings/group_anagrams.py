def signature(word: str) -> str:
    """
    >>> signature("python")
    'hnopty'
    >>> signature("anagram")
    'aaagmnr'
    >>> signature("cloud")
    'cdlou'
    """
    return "".join(sorted(word))


def group_anagrams(words: list) -> dict:
    """
    >>> group_anagrams(['cloud', 'python', 'could'])
    {'cdlou': ['cloud', 'could'], 'hnopty': ['python']}
    >>> group_anagrams(['strap', 'traps', 'maps'])
    {'aprst': ['strap', 'traps'], 'amps': ['maps']}
    >>> group_anagrams(['astro', 'plastic', 'kite'])
    {'aorst': ['astro'], 'acilpst': ['plastic'], 'eikt': ['kite']}
    """
    anagrams = defaultdict()
    for word in words:
        sign = signature(word)
        anagrams.setdefault(sign, []).append(word)
    return anagrams


def remove_non_anagrams(anagrams: dict) -> dict:
    """
    >>> remove_non_anagrams({'cdlou': ['cloud', 'could'], 'hnopty': ['python']})
    {'cdlou': ['cloud', 'could']}
    >>> remove_non_anagrams({'aprst': ['strap', 'traps'], 'amps': ['maps']})
    {'aprst': ['strap', 'traps']}
    >>> remove_non_anagrams({'aorst': ['astro'], 'acilpst': ['plastic'], 'eikt': ['kite']})
    {}
    """
    return {key: anagrams[key] for key in anagrams if len(anagrams[key]) > 1}


def isolate_anagrams(anagrams: dict) -> list:
    """
    >>> isolate_anagrams({'cdlou': ['cloud', 'could']})
    [['cloud', 'could']]
    >>> isolate_anagrams({'aprst': ['strap', 'traps']})
    [['strap', 'traps']]
    >>> isolate_anagrams({})
    []
    """
    return sorted([sorted(_) for _ in anagrams.values()])


if __name__ == "__main__":
    import doctest
    from collections import defaultdict

    data = [
        "could",
        "cloud",
        "areas",
        "arena",
        "artsy",
        "grips",
        "hello",
        "parts",
        "prigs",
        "strap",
        "traps",
    ]
    doctest.testfile("group_anagram.txt")
    isolate_anagrams(remove_non_anagrams(group_anagrams(data)))
