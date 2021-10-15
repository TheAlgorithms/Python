# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
dmnt = 256

# pat  -> would be pattern
# txt  -> given text
# prime_n    -> nth  prime number


def search(pat, txt, prime_n):
    pal_len = len(pat)
    txt_len = len(txt)
    st_idx = 0
    en_idx = 0
    p_hash = 0    # hash value for search pattern
    t_hash = 0    # hash value for given  txt
    h = 1

    # The value of h would be "pow(d, M-1)% q"
    for st_idx in range(pal_len-1):
        h = (h * dmnt) % prime_n

    # Calculate the hash value of pattern and first window
    # of text
    for st_idx in range(pal_len):
        p_hash = (dmnt * p_hash + ord(pat[st_idx])) % prime_n
        t_hash = (dmnt * t_hash + ord(txt[st_idx])) % prime_n

    # Slide the pattern over text one by one
    for st_idx in range(txt_len-pal_len + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p_hash == t_hash:
            # Check for characters one by one
            for en_idx in range(pal_len):
                if txt[st_idx + en_idx] != pat[en_idx]:
                    break

            en_idx += 1
            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if en_idx == pal_len:
                print("Pattern found at index " + str(st_idx))
                return

        # Calculate the hash value for next window of text: Remove
        if st_idx < txt_len-pal_len:
            t_hash = (dmnt*(t_hash-ord(txt[st_idx])*h) +
                      ord(txt[st_idx + pal_len])) % prime_n

            # We might get negative values of t, converting it to
            # positive
            if t_hash < 0:
                t_hash = t_hash + prime_n
    print("No pattern was found")
    return


# Driver program to test the above function
txt = "some random number isbas nanfsfsa  asjf ajfa fjasbfjkasf as jasfjas af"
pat = "some3"
prime_no = 101  # A prime number
search(pat, txt, prime_no)
