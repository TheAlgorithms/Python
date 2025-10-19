def ascii_to_char(ascii_val: int) -> str:
    """Convert ASCII value to corresponding character."""
    return chr(ascii_val)


if __name__ == "__main__":
    num = int(input("Enter ASCII value: "))
    print("Character is:", ascii_to_char(num))
