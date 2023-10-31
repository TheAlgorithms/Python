import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    email = input("Enter email address: ")
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")
