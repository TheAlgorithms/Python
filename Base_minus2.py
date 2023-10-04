def decimal_to_base_minus_2(n):
    if n == 0:
        return "0"

    result = ""

    while n != 0:
        remainder = n % (-2)
        n = -(n // (-2))

        if remainder < 0:
            remainder += 2
            n += 1

        result = str(remainder) + result

    return result


# Example usage:
decimal_number = 13
base_minus_2 = decimal_to_base_minus_2(decimal_number)
print(f"{decimal_number} in base -2 is {base_minus_2}")
