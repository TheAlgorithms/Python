import math
d = 10


def search(pattern, text, q):
    # pat -> pattern
    # txt -> text
    # q -> A prime number
    m = len(pattern)
    n = len(text)
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    i = 0
    j = 0

    # for i in range(m-1):
    #     h = (h*d) % q
    h = (math.pow(d, m-1)) % q

    # Calculate hash value for pattern and first window of text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

        # Slide the pattern over text one by one
    # Find the match
    for i in range(n-m+1):
      # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
          # Check for characters one by one
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == m:
                print("Pattern is found at position: " + str(i+1))

      # Calculate hash value for next window of text: Remove
                # leading digit, add trailing digit
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q


text = "ABCCDDAEFG"
pattern = "CDD"
q = 13
search(pattern, text, q)
