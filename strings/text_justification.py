def text_justification(word: str, max_width: int) -> list:
    """
    Will format the string such that each line has exactly
    (max_width) characters and is fully (left and right) justified,
    and return the list of justified text.

    example 1:
    string = "This is an example of text justification."
    max_width = 16

    output = ['This    is    an',
              'example  of text',
              'justification.  ']

    >>> text_justification("This is an example of text justification.", 16)
    ['This    is    an', 'example  of text', 'justification.  ']

    example 2:
    string = "Two roads diverged in a yellow wood"
    max_width = 16
    output = ['Two        roads',
              'diverged   in  a',
              'yellow wood     ']

    >>> text_justification("Two roads diverged in a yellow wood", 16)
    ['Two        roads', 'diverged   in  a', 'yellow wood     ']

    Time complexity: O(m*n)
    Space complexity: O(m*n)
    """

    # Converting string into list of strings split by a space
    words = word.split()

    def justify(line: list, width: int, max_width: int) -> str:
        overall_spaces_count = max_width - width
        words_count = len(line)
        if len(line) == 1:
            # if there is only word in line
            # just insert overall_spaces_count for the remainder of line
            return line[0] + " " * overall_spaces_count
        else:
            spaces_to_insert_between_words = words_count - 1
            # num_spaces_between_words_list[i] : tells you to insert
            # num_spaces_between_words_list[i] spaces
            # after word on line[i]
            num_spaces_between_words_list = spaces_to_insert_between_words * [
                overall_spaces_count // spaces_to_insert_between_words
            ]
            spaces_count_in_locations = (
                overall_spaces_count % spaces_to_insert_between_words
            )
            # distribute spaces via round robin to the left words
            for i in range(spaces_count_in_locations):
                num_spaces_between_words_list[i] += 1
            aligned_words_list = []
            for i in range(spaces_to_insert_between_words):
                # add the word
                aligned_words_list.append(line[i])
                # add the spaces to insert
                aligned_words_list.append(num_spaces_between_words_list[i] * " ")
            # just add the last word to the sentence
            aligned_words_list.append(line[-1])
            # join the aligned words list to form a justified line
            return "".join(aligned_words_list)

    answer = []
    line: list[str] = []
    width = 0
    for inner_word in words:
        if width + len(inner_word) + len(line) <= max_width:
            # keep adding words until we can fill out max_width
            # width = sum of length of all words (without overall_spaces_count)
            # len(inner_word) = length of current inner_word
            # len(line) = number of overall_spaces_count to insert between words
            line.append(inner_word)
            width += len(inner_word)
        else:
            # justify the line and add it to result
            answer.append(justify(line, width, max_width))
            # reset new line and new width
            line, width = [inner_word], len(inner_word)
    remaining_spaces = max_width - width - len(line)
    answer.append(" ".join(line) + (remaining_spaces + 1) * " ")
    return answer


if __name__ == "__main__":
    from doctest import testmod

    testmod()
