def has_unique_chars(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True


# Example
s = "abcdefga"
print("Unique Characters:", has_unique_chars(s))
