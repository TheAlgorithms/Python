# global variable for positions found for the pattern
positions = []
def compute_prefix_array(pattern):
    m = len(pattern)
    prefix_array = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_array[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_array[length - 1]
            else:
                prefix_array[i] = 0
                i += 1

    return prefix_array


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    if m == 0:
        return positions

    prefix_array = compute_prefix_array(pattern)
    i, j = 0, 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                positions.append([(i - j), pattern])
                j = prefix_array[j - 1]
        else:
            if j != 0:
                j = prefix_array[j - 1]
            else:
                i += 1

    return positions

def find_no_start_or_end(pat, text):
    if not pat.startswith("^"):
        if not pat.endswith("$"):
            return kmp_search(text, pat)
def find_end_exists(pat, text):
    if pat.endswith("$"):
        pattern_without_end = pat[:-1]
        i = len(text) - len(pattern_without_end)
        pattern_found_at_end = True
        for char in pattern_without_end:
            if i >= len(text) or text[i] != char:
                pattern_found_at_end = False
                break
            i += 1
        if pattern_found_at_end:
            return [[(len(text) - len(pattern_without_end)), pattern_without_end]]
    return None

def find_start_exists(pat, text):
    if pat.startswith("^"):
        pattern_without_start = pat[1:]
        i = 0
        pattern_found_in_start = True
        for char in pattern_without_start:
            if i >= len(text) or text[i] != char:
                pattern_found_in_start = False
                break
            i += 1

        if pattern_found_in_start:
            return [[0, pattern_without_start]]
    return None

def find_both_start_and_end_exists(pat, text, dot_replaced_patterns=None):
    global positions
    if pat.startswith("^") and pat.endswith("$"):
        pattern_without_start_and_end = pat[1:-1]
        if pattern_without_start_and_end == text:
            positions.extend([0, pattern_without_start_and_end])
    else:
        if dot_replaced_patterns:
            for pattern in dot_replaced_patterns:
                start_positions = find_start_exists(pattern, text)
                if start_positions is not None:
                    positions.extend(start_positions)

                end_positions = find_end_exists(pattern, text)
                if end_positions is not None:
                    positions.extend(end_positions)

                no_start_or_end_positions = find_no_start_or_end(pattern, text)
                if no_start_or_end_positions is not None:
                    positions.extend(no_start_or_end_positions)
        else:
            start_positions = find_start_exists(pat, text)
            if start_positions is not None:
                positions.extend(start_positions)

            end_positions = find_end_exists(pat, text)
            if end_positions is not None:
                positions.extend(end_positions)

            no_start_or_end_positions = find_no_start_or_end(pat, text)
            if no_start_or_end_positions is not None:
                positions.extend(no_start_or_end_positions)


def generate_patterns_for_dot_digit_avalible(pat):
    dot_digit_replaced_patterns = []

    if "." in pat and "\\d" in pat:
        for ascii_val in range(128):
            char = chr(ascii_val)
            if char != '\n':
                dot_digit_replaced_patterns.append(pat.replace('.', char).replace('\\d', char))

            for digit_val in range(10):
                digit = str(digit_val)
                dot_digit_replaced_patterns.append(pat.replace('.', digit).replace('\\d', digit))
    elif "." in pat:
        for ascii_val in range(128):
            char = chr(ascii_val)
            if char != '\n':
                dot_digit_replaced_patterns.append(pat.replace('.', char))
    elif "\\d" in pat:
        for digit_val in range(10):
            digit = str(digit_val)
            dot_digit_replaced_patterns.append(pat.replace('\\d', digit))
    else:
        dot_digit_replaced_patterns.append(pat)

    return dot_digit_replaced_patterns


def find_or_exists(pat, text):
    if "|" in pat:
        sub_patterns = pat.split("|")
        for item in sub_patterns:
             dot_digit_replaced_patterns = generate_patterns_for_dot_digit_avalible(item)
             find_both_start_and_end_exists(item, text, dot_digit_replaced_patterns)
    else:
        dot_digit_replaced_patterns = generate_patterns_for_dot_digit_avalible(pat)
        find_both_start_and_end_exists(pat, text, dot_digit_replaced_patterns)

#main---------------------------------------------------------------------------------
def main(positions):
    with open('text.txt', 'r') as inputText:
        text = inputText.read()

    with open('pattern.txt', 'r') as inputPattern:
        pattern = inputPattern.read()

    find_or_exists(pattern, text)

    positions = list(set(tuple(pos) for pos in positions))
    sorted_positions = sorted(positions, key=lambda pos: pos[0])

    if sorted_positions:
        print("Patterns found at positions:", sorted_positions)
    else:
        print("Patterns not found in the text.")

if __name__ == '__main__':
    main(positions)

