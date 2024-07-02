def indian_number_comma(number: str) -> str:
    """
    Returns the string with comma separated as per indian number system
    :param number:
    :return: number_with_comma
    >>> indian_number_comma("6789")
    6,789
    >>> indian_number_comma("789")
    789
    >>> indian_number_comma("7980999")
    79,80,999
    """
    last_3_digits = number[-3:]
    # store the numbers before 3 digits
    before_3 = number[:-3]
    # converts the string into of 2-2 characters
    split_list = [before_3[i : i + 2] for i in range(0, len(before_3), 2)]
    # add the separated last digits to the list
    split_list.append(last_3_digits)
    # join the whole list around ,
    result = ",".join(split_list)
    return result


if __name__ == "__main__":
    assert indian_number_comma("6789"), "6,789"
    assert indian_number_comma("789"), "789"
    assert indian_number_comma("7980999"), "79,80,999"
