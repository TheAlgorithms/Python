def binary_to_excess3(binary_str: str) -> str:
    """
    Convert a binary number (as a string) to its Excess-3 code.

    Args:
        binary_str (str): Binary number as a string (e.g., "1010").

    Returns:
        str: Excess-3 code as a binary string.

    Example:
        >>> binary_to_excess3("1010")
        '1101'
    """
    # Convert binary to decimal
    decimal_value = int(binary_str, 2)

    # Add 3 (Excess-3 encoding)
    excess3_value = decimal_value + 3

    # Convert back to 4-bit binary
    excess3_binary = format(excess3_value, "04b")

    return excess3_binary


if __name__ == "__main__":
    binary_input = input("Enter a 4-bit binary number: ")
    excess3_output = binary_to_excess3(binary_input)
    print(f"Excess-3 code of {binary_input} is: {excess3_output}")
