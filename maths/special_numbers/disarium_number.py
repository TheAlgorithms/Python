def is_disarium(num):
    """
    Check if a number is a Disarium number.
    A Disarium number is a number in which the sum of its digits
    powered with their respective positions is equal to the number itself.

    Example:
        135 -> 1¹ + 3² + 5³ = 135 ✅
    """
    digits = str(num)
    total = 0
    position = 1

    for i in digits:
        total += int(i) ** position
        position += 1

    return total == num


if __name__ == "__main__":
    test_numbers = [89, 135, 175, 518, 9, 10]
    for n in test_numbers:
        print(f"{n} → {'Disarium' if is_disarium(n) else 'Not Disarium'}")
