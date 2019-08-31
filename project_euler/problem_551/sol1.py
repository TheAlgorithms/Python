"""
Sum of digits sequence
Problem 551

Let a(0), a(1),... be an interger sequence defined by:
     a(0) = 1
     for n >= 1, a(n) is the sum of the digits of all preceding terms

The sequence starts with 1, 1, 2, 4, 8, ...
You are given a(10^6) = 31054319.

Find a(10^15)
"""

ks = [k for k in range(2, 20+1)]
base = [10 ** k for k in range(ks[-1] + 1)]
memo = {}


def next_term(a_i, k, i, n):
    """
    Calculates and updates a_i in-place to either the n-th term or the
    smallest term for which c > 10^k when the terms are written in the form:
            a(i) = b * 10^k + c

    For any a(i), if digitsum(b) and c have the same value, the difference
    between subsequent terms will be the same until c >= 10^k.  This difference
    is cached to greatly speed up the computation.

    Arguments:
    a_i -- array of digits starting from the one's place that represent 
           the i-th term in the sequence
    k --  k when terms are written in the from a(i) = b*10^k + c.
          Term are calulcated until c > 10^k or the n-th term is reached.
    i -- position along the sequence
    n -- term to caluclate up to if k is large enough

    Return: a tuple of difference between ending term and starting term, and
    the number of terms calculated. ex. if starting term is a_0=1, and
    ending term is a_10=62, then (61, 9) is returned.
    """
    # ds_b - digitsum(b)
    ds_b = 0
    for j in range(k, len(a_i)):
        ds_b += a_i[j]
    c = 0
    for j in range(min(len(a_i), k)):
        c += a_i[j] * base[j]

    diff, dn = 0, 0
    max_dn = n - i

    sub_memo = memo.get(ds_b)

    if sub_memo != None:
        jumps = sub_memo.get(c)

        if jumps != None and len(jumps) > 0:
            # find and make the largest jump without going over
            max_jump = -1
            for _k in range(len(jumps) - 1, -1, -1):
                if jumps[_k][2] <= k and jumps[_k][1] <= max_dn:
                    max_jump = _k
                    break

            if max_jump >= 0:
                diff, dn, _kk = jumps[max_jump]
                # since the difference between jumps is cached, add c
                new_c = diff + c
                for j in range(min(k, len(a_i))):
                    new_c, a_i[j] = divmod(new_c, 10)
                if new_c > 0:
                    add(a_i, k, new_c)

        else:
            sub_memo[c] = []
    else:
        sub_memo = {c: []}
        memo[ds_b] = sub_memo

    if dn >= max_dn or c + diff >= base[k]:
        return diff, dn

    if k > ks[0]:
        while True:
            # keep doing smaller jumps
            _diff, terms_jumped = next_term(a_i, k - 1, i + dn, n)
            diff += _diff
            dn += terms_jumped

            if dn >= max_dn or c + diff >= base[k]:
                break
    else:
        # would be too small a jump, just compute sequential terms instead
        _diff, terms_jumped = compute(a_i, k, i + dn, n)
        diff += _diff
        dn += terms_jumped

    jumps = sub_memo[c]

    # keep jumps sorted by # of terms skipped
    j = 0
    while j < len(jumps):
        if jumps[j][1] > dn:
            break
        j += 1

    # cache the jump for this value digitsum(b) and c
    sub_memo[c].insert(j, (diff, dn, k))
    return (diff, dn)


def compute(a_i, k, i, n):
    """
    same as next_term(a_i, k, i, n) but computes terms without memoizing results.
    """
    if i >= n:
        return 0, i
    if k > len(a_i):
        a_i.extend([0 for _ in range(k - len(a_i))])

    # note: a_i -> b * 10^k + c
    # ds_b -> digitsum(b)
    # ds_c -> digitsum(c)
    start_i = i
    ds_b, ds_c, diff = 0, 0, 0
    for j in range(len(a_i)):
        if j >= k:
            ds_b += a_i[j]
        else:
            ds_c += a_i[j]

    while i < n:
        i += 1
        addend = ds_c + ds_b
        diff += addend
        ds_c = 0
        for j in range(k):
            s = a_i[j] + addend
            addend, a_i[j] = divmod(s, 10)

            ds_c += a_i[j]

        if addend > 0:
            break

    if addend > 0:
        add(a_i, k, addend)
    return diff, i - start_i


def add(digits, k, addend):
    """
    adds addend to digit array given in digits
    starting at index k
    """
    for j in range(k, len(digits)):
        s = digits[j] + addend
        if s >= 10:
            quotient, digits[j] = divmod(s, 10)
            addend = addend // 10 + quotient
        else:
            digits[j] = s
            addend = addend // 10

        if addend == 0:
            break

    while addend > 0:
        addend, digit = divmod(addend, 10)
        digits.append(digit)


def solution(n):
    """
    returns n-th term of sequence

    >>> solution(10)
    62

    >>> solution(10**6)
    31054319

    >>> solution(10**15)
    73597483551591773
    """

    digits = [1]
    i = 1
    dn = 0
    while True:
        diff, terms_jumped = next_term(digits, 20, i + dn, n)
        dn += terms_jumped
        if dn == n - i:
            break

    a_n = 0
    for j in range(len(digits)):
        a_n += digits[j] * 10 ** j
    return a_n


if __name__ == "__main__":
    print(solution(10 ** 15))
