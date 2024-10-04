import os
import sys
import time

from . import transposition_cipher as trans_cipher

def main() -> None:
    input_file = "./prehistoric_men.txt"
    output_file = "./Output.txt"
    
    try:
        key = int(input("Enter key (integer): "))
    except ValueError:
        print("Invalid key. Please enter an integer.")
        sys.exit()

    mode = input("Encrypt/Decrypt [e/d]: ").strip().lower()
    if mode not in ['e', 'd']:
        print("Invalid mode. Please enter 'e' for encrypt or 'd' for decrypt.")
        sys.exit()

    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist. Quitting...")
        sys.exit()

    if os.path.exists(output_file):
        response = input(f"Overwrite {output_file}? [y/n]: ").strip().lower()
        if not response.startswith("y"):
            print("Operation cancelled.")
            sys.exit()

    start_time = time.time()

    try:
        if mode == "e":
            with open(input_file, 'r') as f:
                content = f.read()
            translated = trans_cipher.encrypt_message(key, content)
        elif mode == "d":
            with open(output_file, 'r') as f:
                content = f.read()
            translated = trans_cipher.decrypt_message(key, content)
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit()

    try:
        with open(output_file, "w") as output_obj:
            output_obj.write(translated)
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit()

    total_time = round(time.time() - start_time, 2)
    print(f"Done in {total_time} seconds.")

if __name__ == "__main__":
    main()