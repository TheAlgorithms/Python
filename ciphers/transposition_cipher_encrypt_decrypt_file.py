import os
import sys
import time

from . import transposition_cipher as trans_cipher


def main() -> None:
    input_file = "./prehistoric_men.txt"
    output_file = "./Output.txt"
    key = int(input("Enter key: "))
    mode = input("Encrypt/Decrypt [e/d]: ")

    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist. Quitting...")
        sys.exit()
    if os.path.exists(output_file):
        print(f"Overwrite {output_file}? [y/n]")
        response = input("> ")
        if not response.lower().startswith("y"):
            sys.exit()

    start_time = time.time()
    if mode.lower().startswith("e"):
        with open(input_file) as f:
            content = f.read()
        translated = trans_cipher.encrypt_message(key, content)
    elif mode.lower().startswith("d"):
        with open(output_file) as f:
            content = f.read()
        translated = trans_cipher.decrypt_message(key, content)

    with open(output_file, "w") as output_obj:
        output_obj.write(translated)

    total_time = round(time.time() - start_time, 2)
    print(("Done (", total_time, "seconds )"))


if __name__ == "__main__":
    main()
