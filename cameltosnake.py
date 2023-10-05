def cameltosnake(camel_string: str) -> str:
    # If the input string is empty, return an empty string
    if not camel_string:
        return ""
    # If the first character of the input string is uppercase,
    # add an underscore before it and make it lowercase
    elif camel_string[0].isupper():
        return f"_{camel_string[0].lower()}{cameltosnake(camel_string[1:])}"
    # If the first character of the input string is lowercase,
    # simply return it and call the function recursively on the remaining string
    else:
        return f"{camel_string[0]}{cameltosnake(camel_string[1:])}"


def camel_to_snake(s):
    if len(s) <= 1:
        return s.lower()
    # Changing the first character of the input string to lowercase
    # and calling the recursive function on the modified string
    return cameltosnake(s[0].lower() + s[1:])


# Example usage
print(camel_to_snake("GeeksForGeeks"))  # Output: "geeks_for_geeks"
print(camel_to_snake("ThisIsInCamelCase"))  # Output: "this_is_in_camel_case"
