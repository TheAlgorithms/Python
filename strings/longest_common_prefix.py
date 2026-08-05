def longest_common_prefix(strs: list[str]) -> str:
    """
    :type strs: List[str]

    URL:
        https://en.wikipedia.org/wiki/Longest_common_prefix

    Args:
        strs (list[str]): A list of strings.


    Returns:
        str:The longest common prefix shared among all strings.
            Returns an empty string if there is none.

    Test cases:
    >>> longest_common_prefix(["flower","flow","flap"])
    'fl'
    >>> longest_common_prefix(["cats","dragon","dracula"])
    ''
    >>> longest_common_prefix(["marianne","mariachi"])
    'maria'
    >>> longest_common_prefix([])
    ''
    >>> longest_common_prefix(["","belly","belt"])
    ''
    >>> longest_common_prefix(["#hashtag","#hashbrown","#hash"])
    '#hash'
    """
    ans = ""
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]

    k = 0
    ref = strs[0]

    while k < len(ref):
        for ele in strs:
            if len(ele) < k + 1 or ref[k] != ele[k]:
                return ans
        ans += ele[k]
        k += 1
    return ans
