def anagram(_list):
    char_map = {}
    anagrams = []
    for each in _list:
        char_map[each] = {'is_visited': 0}
        for char in each:
            if char not in char_map[each]:
                char_map[each][char] = 1
            else:
                char_map[each][char] += 1

    _keys = list(char_map.keys())
    for itr1 in range(0, len(_keys)):
        res = []
        for itr2 in range(itr1 + 1, len(_keys)):
            if char_map[_keys[itr1]] == char_map[_keys[itr2]] and char_map[_keys[itr2]]['is_visited'] == 0:
                res.append(_keys[itr1])
                res.append(_keys[itr2])
                char_map[_keys[itr2]]['is_visited'] = 1
        _set = list(set(res))
        if len(_set) != 0:
            anagrams.append(_set)
    print(anagrams)


if __name__ == "__main__":
    _list = ['could', 'cloud', 'areas', 'arena', 'artsy', 'grips', 'hello', 'parts', 'prigs', 'strap', 'traps']
    anagram(_list)
