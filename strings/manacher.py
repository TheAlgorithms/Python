def palindromic_string(input_string: str) -> str:
    """
    >>> palindromic_string('abbbaba')
    'abbba'
    >>> palindromic_string('ababa')
    'ababa'
    >>> palindromic_string('abb')
    'bb'
    >>> palindromic_string('caccaaac')
    'caaac'
    >>> palindromic_string('abcbbaab')
    'baab'
    >>> palindromic_string('')
    ''

    Manacher's algorithm which finds Longest palindromic Substring in linear time.

    1. first this convert input_string("xyx") into new_string("x|y|x") where odd
        positions are actual input characters.
    2. for each character in new_string it find corresponding length and
        store the length and left,right to store previously calculated info.
        (please look the explanation for details)

    3. return corresponding output_string by removing all "|"

    Note that lengths in new_input_string are not proportional to lengths in
    input_string: the palindrome of center j and radius k spans the new indices
    [j - k + 1, j + k - 1] and covers only the even ones, so its original length
    is (2 * k - 1) // 2 or (2 * k - 1) // 2 + 1. Comparing transformed lengths
    directly makes even-length palindromes lose ties against odd-length ones,
    which is why the best palindrome is tracked in original coordinates.
    """
    if not input_string:
        return ""

    # if input_string is "aba" than new_input_string become "a|b|a"
    new_input_string = ""

    # append each character + "|" in new_string for range(0, length-1)
    for i in input_string[: len(input_string) - 1]:
        new_input_string += i + "|"
    # append last character
    new_input_string += input_string[-1]

    # we will store the starting and ending of previous furthest ending palindromic
    # substring
    left, right = 0, 0

    # length[i] shows the length of palindromic substring with center i
    length = [1 for i in range(len(new_input_string))]

    # best palindrome found so far, in coordinates of input_string
    max_length = 0
    start = 0

    # for each character in new_string find corresponding palindromic string
    for j in range(len(new_input_string)):
        k = 1 if j > right else min(length[left + right - j] // 2, right - j + 1)
        while (
            j - k >= 0
            and j + k < len(new_input_string)
            and new_input_string[k + j] == new_input_string[j - k]
        ):
            k += 1

        length[j] = 2 * k - 1

        # does this string is ending after the previously explored end (that is right) ?
        # if yes the update the new right to the last index of this
        if j + k - 1 > right:
            left = j - k + 1
            right = j + k - 1

        # update max_length and start position using the length in input_string:
        # only even indices of new_input_string hold original characters
        first = j - k + 1 if (j - k + 1) % 2 == 0 else j - k + 2
        last = j + k - 1 if (j + k - 1) % 2 == 0 else j + k - 2
        if first > last:
            continue
        original_length = (last - first) // 2 + 1
        if max_length < original_length:
            max_length = original_length
            start = first // 2

    return input_string[start : start + max_length]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

"""
...a0...a1...a2.....a3......a4...a5...a6....

consider the string for which we are calculating the longest palindromic substring is
shown above where ... are some characters in between and right now we are calculating
the length of palindromic substring with center at a5 with following conditions :
i) we have stored the length of palindromic substring which has center at a3
    (starts at left ends at right) and it is the furthest ending till now,
    and it has ending after a6
ii) a2 and a4 are equally distant from a3 so char(a2) == char(a4)
iii) a0 and a6 are equally distant from a3 so char(a0) == char(a6)
iv) a1 is corresponding equal character of a5 in palindrome with center a3 (remember
    that in below derivation of a4==a6)

now for a5 we will calculate the length of palindromic substring with center as a5 but
can we use previously calculated information in some way?
Yes, look the above string we know that a5 is inside the palindrome with center a3 and
previously we have calculated that
a0==a2 (palindrome of center a1)
a2==a4 (palindrome of center a3)
a0==a6 (palindrome of center a3)
so a4==a6

so we can say that palindrome at center a5 is at least as long as palindrome at center
a1 but this only holds if a0 and a6 are inside the limits of palindrome centered at a3
so finally ..

len_of_palindrome__at(a5) = min(len_of_palindrome_at(a1), right-a5)
where a3 lies from left to right and we have to keep updating that

and if the a5 lies outside of left,right boundary we calculate length of palindrome with
bruteforce and update left,right.

it gives the linear time complexity just like z-function
"""
