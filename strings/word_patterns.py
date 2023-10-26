def get_word_pattern(word: str) -> str:
    """
    Returns numerical pattern of character appearances in given word
    >>> get_word_pattern("")
    ''
    >>> get_word_pattern(" ")
    '0'
    >>> get_word_pattern("pattern")
    '0.1.2.2.3.4.5'
    >>> get_word_pattern("word pattern")
    '0.1.2.3.4.5.6.7.7.8.2.9'
    >>> get_word_pattern("get word pattern")
    '0.1.2.3.4.5.6.7.3.8.9.2.2.1.6.10'
    >>> get_word_pattern()
    Traceback (most recent call last):
    ...
    TypeError: get_word_pattern() missing 1 required positional argument: 'word'
    >>> get_word_pattern(1)
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute 'upper'
    >>> get_word_pattern(1.1)
    Traceback (most recent call last):
    ...
    AttributeError: 'float' object has no attribute 'upper'
    >>> get_word_pattern([])
    Traceback (most recent call last):
    ...
    AttributeError: 'list' object has no attribute 'upper'
    """
    word = word.upper()
    next_num = 0
    letter_nums = {}
    word_pattern = []

    for letter in word:
        if letter not in letter_nums:
            letter_nums[letter] = str(next_num)
            next_num += 1
        word_pattern.append(letter_nums[letter])
    return ".".join(word_pattern)


if __name__ == "__main__":
    import pprint
    import time

    start_time = time.time()
    with open("dictionary.txt") as in_file:
        word_list = in_file.read().splitlines()

    all_patterns: dict = {}
    for word in word_list:
        pattern = get_word_pattern(word)
        if pattern in all_patterns:
            all_patterns[pattern].append(word)
        else:
            all_patterns[pattern] = [word]

    with open("word_patterns.txt", "w") as out_file:
        out_file.write(pprint.pformat(all_patterns))

    total_time = round(time.time() - start_time, 2)
    print(f"Done!  {len(all_patterns):,} word patterns found in {total_time} seconds.")
    # Done!  9,581 word patterns found in 0.58 seconds.
