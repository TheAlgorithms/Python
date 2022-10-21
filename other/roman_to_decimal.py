# Progam to convert roman numerals to decimal

# Taking the number in roman numerals as input
roman = input().strip()

# Storing values in a dictionary
d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 1000}

# Initializing some values
decimal = 0
largest = d[roman[-1]]

# In case only one digit is given as input, we just output its value
if len(roman) == 1:
    decimal = d[roman]
    print(decimal)

else:
    # Iterating though the roman number input backwards
    # here, we store the largest single digit occured so far in 'largest'
    for i in range(len(roman) - 1, -1, -1):

        # If we encounter a digit less than the largest so far, we subtract that
        # digit's value from the integer value so far
        if d[roman[i]] < largest:
            decimal -= d[roman[i]]

        # Otherwise we simply add the value of the current digit to the integer
        # value so far, and update the value of largest
        else:
            decimal += d[roman[i]]
            largest = d[roman[i]]

    print(decimal)
