from cryptography.fernet import Fernet

# -----------colour codes----------------#
bold_yellow = "\u001b[1m \u001b[33m"
bold_red = "\u001b[1m \u001b[31m"
bold_green = "\u001b[1m \u001b[32m"
bold_blue = "\u001b[1m \u001b[34m"
cyan = "\u001b[36m"
green = "\u001b[32m"
blue = "\u001b[34m"
reset = "\u001b[0m"
# --------------------------------------#

# ------------------------------------------------------- #
banner = """
\t    ____              ______                     __     
\t   / __ \__  __      / ____/__  _________  ___  / /_    
\t  / /_/ / / / /_____/ /_  / _ \/ ___/ __ \/ _ \/ __/    
\t / ____/ /_/ /_____/ __/ /  __/ /  / / / /  __/ /_      
\t/_/    \__, /     /_/    \___/_/  /_/ /_/\___/\__/      
\t      /____/                                                     
"""
# ------------------------------------------------------- #
    

# Main function start
def main():
    print("\033c")
    print(f"{bold_blue}{banner}{reset}")
    inp = input(f"\nWhat do you want?\n\n\t{bold_yellow}1. Fernet Encode\n\t 2. Fernet Decode\n\t{reset}{bold_red}0. Exit\n\n{reset}Choose: {cyan}")
    if inp == "1":
        # Will generate a Fernet Key
        key = Fernet.generate_key()
        f = Fernet(key)

        # Will print the generated key
        print(f"\n{reset}Generated key is: {cyan}{key.decode('utf8')}{reset}")

        txt = input(f"\nEnter text to encode: {green}")

        # Encrypt text using Fernet
        token = f.encrypt(bytes(txt,'utf8'))

        # print the encrypted token
        print(f"{reset}\nYour token is: {cyan} {token.decode('utf8')} {reset}")

    elif inp == "2":
        try:
            # For taking token and key as input
            token = bytes(input(f"{reset}\nEnter fernet token: {cyan}"),'utf8')
            key = bytes(input(f"{reset}Enter the key: {cyan}"),'utf8')

            # For decoding fernet
            decoded_txt = Fernet(key).decrypt(token).decode('utf8')

            # For printing decoded message
            print(f"\n{reset}Decoded message is: {bold_green}{decoded_txt}{reset}")

        except Exception as e:
            print(f"{bold_red}\nCan't decode!!")
            print(e, reset)
            print("\nTry again!!")

        finally:
            print("\nThank you!!")

    elif inp == "0":
        exit(f"\n{bold_blue}Thank you! byee.{reset}")

    else:
        print(bold_red,"\nWrong input!!", reset)
        input(f"\n{blue}Press enter to continue...{reset}")
        print("\033c")
        main()

if __name__ == "__main__":
    main()
