import re

def is_sri_lankan_number(phone_number):
    # Define a regex pattern for Sri Lankan phone numbers
    sri_lankan_pattern = re.compile(r"^(?:0|94|\+94|0{2}94)7(0|1|2|4|5|6|7|8)(-| |)\d{7}$")

    # Remove any non-numeric characters from the phone number
    raw_number = ''.join(filter(str.isdigit, phone_number))

    # Check if the cleaned number matches the Sri Lankan pattern
    return bool(sri_lankan_pattern.match(raw_number))

# Example usage:

phone_number = input("Enter the number to be checked  ") 
if is_sri_lankan_number(phone_number):
    print(f"The phone number {phone_number} belongs to Sri Lanka.")
else:
    print(f"The phone number {phone_number} does not belong to Sri Lanka.")
