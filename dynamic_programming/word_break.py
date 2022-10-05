def wordbreak(word, word_dict) -> bool:
    """
    word ---> Input word
    word_dict ---> Input dictionary
    >>> wordbreak('deepImpact',['deep,'Im','pact'])
    True
    >>> wordbreak('mangoinmango',['mango','in'])
    True
    >>> wordbreak('deepfacts',['deeps','fact'])
    False
    """
    dict_set = set(word_dict)
    start = [0]
    # start[0] is the equivalent of a base-case
    # from the recursive solution and start[-1] is the
    # overall solution to the complete problem
    for i in range(len(word)):
        for j in start:
            if word[j : i + 1] in dict_set:
                start.append(i + 1)  # start of next word in dict
                break  # - note [1]
    return start[-1] == len(word)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
