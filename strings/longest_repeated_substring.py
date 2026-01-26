def longest_repeated_substring(s: str) -> str:
    """
    Longest repeated (overlapping allowed) substring in O(n) using a suffix automaton.
    Returns empty string if no repetition.
    """
    n = len(s)
    if n <= 1:
        return ""

    class State:
        __slots__ = ("next", "link", "length", "first_pos", "occ")

        def __init__(self):
            self.next = {}
            self.link = -1
            self.length = 0
            self.first_pos = -1
            self.occ = 0

    st = [State()]
    last = 0

    def sa_extend(c, pos):
        nonlocal last
        cur = len(st)
        st.append(State())
        st[cur].length = st[last].length + 1
        st[cur].first_pos = pos
        st[cur].occ = 1
        p = last
        while p >= 0 and c not in st[p].next:
            st[p].next[c] = cur
            p = st[p].link
        if p == -1:
            st[cur].link = 0
        else:
            q = st[p].next[c]
            if st[p].length + 1 == st[q].length:
                st[cur].link = q
            else:
                clone = len(st)
                st.append(State())
                st[clone].next = st[q].next.copy()
                st[clone].length = st[p].length + 1
                st[clone].link = st[q].link
                st[clone].first_pos = st[q].first_pos
                while p >= 0 and st[p].next.get(c) == q:
                    st[p].next[c] = clone
                    p = st[p].link
                st[q].link = clone
                st[cur].link = clone
        last = cur

    for i, ch in enumerate(s):
        sa_extend(ch, i)

    order = sorted(range(len(st)), key=lambda i: st[i].length, reverse=True)
    for v in order:
        if st[v].link != -1:
            st[st[v].link].occ += st[v].occ

    best_len = 0
    best_end = -1
    for state in st:
        if state.occ >= 2 and state.length > best_len:
            best_len = state.length
            best_end = state.first_pos
    if best_len == 0:
        return ""
    return s[best_end - best_len + 1 : best_end + 1]


if __name__ == "__main__":
    print(longest_repeated_substring("banana"))
