def validUtf8(data):
    lefttoCheck = 0
    for d in data:
        if lefttoCheck == 0:
            # Check if the first bit of the current number is 1 and the next three bits are 1.
            if (d >> 3) == 0b11110:
                lefttoCheck = 3  # If true, set lefttoCheck to 3 to indicate a 4-byte character.
            # Check if the first bit of the current number is 1 and the next two bits are 1.
            elif (d >> 4) == 0b1110:
                lefttoCheck = 2  # If true, set lefttoCheck to 2 to indicate a 3-byte character.
            # Check if the first bit of the current number is 1 and the next bit is 1.
            elif (d >> 5) == 0b110:
                lefttoCheck = 1  # If true, set lefttoCheck to 1 to indicate a 2-byte character.
            # Check if the first bit of the current number is 0.
            elif (d >> 7) == 0b0:
                lefttoCheck = 0  # If true, set lefttoCheck to 0 to indicate a single-byte character.
            else:
                return False  # Return False if none of the above conditions are met.
        else:
            # Check if the first two bits of the current number are 10.
            if (d >> 6) != 0b10:
                return False  # Return False if the first two bits are not 10.
            lefttoCheck -= 1  # Decrement lefttoCheck by 1 since we have checked a byte of a multi-byte character.
    return lefttoCheck == 0  # Return True if lefttoCheck is 0, indicating that all characters have been checked.

