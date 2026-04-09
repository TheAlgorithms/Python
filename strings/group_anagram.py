def group_anagrams(strs:list[str]) -> list[list[str]]:
    """ Group word that are anagrams.
    Two words are anagram if they contain the same
    character in a different order.
    :param words: List of input strings
    :return :List of grouped anagrams
    """
    res={}
    for word in strs:
        key="".join(sorted(word)) #fixed key
        if key not in res:
            res[key]=[]
        res(key.append(word)) #fixed syntax
    return list(res.values()) #fixed function call
if __name__ == "__main__"
print(group_anagrams["eat","tea","tan","ate","nat","bat"])
