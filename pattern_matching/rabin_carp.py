# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# dmnt is the number of characters in the input alphabet
dmnt = 256

# pat  -> would be pattern
# txt  -> given text
# prime_n    -> nth  prime number


def search(pattern: str,  text: str,  nth_prime_number: int) -> None:
    """
    The  Rabin-Carp alrternatively  named as rolling-has is an Algorithm for finding a pattern within a piece of text
    with complexity O(N) ->  N is the lenth of the text

    1. determine the length of the of the pettern sting and make a window size of that sting and try to overlap on the text string

    2. if the hash value of the pattern string and the selected text is not equal then move on to the next character and remove 1st careacter from the beginning. 

    3. continue this process untill  you reach the end of the string. 
    """
    pal_len = len(pattern)
    txt_len = len(text)
    start_index = 0
    end_index = 0
    pattern_hash = 0    # hash value for search pattern
    text_hash = 0    # hash value for given  txt
    h = 1

    # The value of h would be "pow(d, M-1)% q"
    for st_idx in range(pal_len-1):
        h = (h * dmnt) % nth_prime_number

    # Calculate the hash value of pattern and first window
    for st_idx in range(pal_len):
        p_hash = (dmnt * p_hash + ord(pattern[st_idx])) % nth_prime_number
        t_hash = (dmnt * t_hash + ord(text[st_idx])) % nth_prime_number

    # Slide the pattern over text one by one
    for st_idx in range(txt_len-pal_len + 1):
        # Check the hash values of current window of text and pattern if the hash values match then only check
        if p_hash == t_hash:
            # Check for characters one by one
            for en_idx in range(pal_len):
                if text[st_idx + en_idx] != pattern[en_idx]:
                    break

            en_idx += 1
            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if en_idx == pal_len:
                return True

        # Calculate the hash value for next window of text: Remove
        if st_idx < txt_len-pal_len:
            t_hash = (dmnt*(t_hash-ord(text[st_idx])*h) +
                      ord(text[st_idx + pal_len])) % nth_prime_number

            # We might get negative values of t, converting it to positive
            if t_hash < 0:
                t_hash = t_hash + nth_prime_number
    return False


# Driver program to test the above function
if __name__ == "__main__":
    prime_no = 101  # A prime number
    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert search(pattern, text1, prime_no) and not search(
        pattern, text2, prime_no)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert search(pattern, text, prime_no)

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert search(pattern, text, prime_no)

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert search(pattern, text, prime_no)

    # Test 5)
    text = "some random number isbas nanfsfsa  asjf ajfa fjasbfjkasf as jasfjas af"
    pattern = "some3"
    search(pattern, text, prime_no)
