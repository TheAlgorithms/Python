def strong_password_detection(password):

    AllowedSymbols = ['#', '@', '$', '_', '*', '-']
    flag = 1
    # length of the entered password should be at least 6
    if len(password) < 6:
        print('length of the entered password should be at least 6')
        flag = 0
    # length of the entered password should be not be greater than 15
    if len(password) > 15:
        print('length of the entered password should be not be greater than 15')
        flag = 0
    # The entered password should have at least one numeral
    if not any(char.isdigit() for char in password):
        print('The entered password should have at least one numeral')
        flag = 0
    # Password should have at least one lowercase letter
    if not any(char.islower() for char in password):
        print('the entered password should have at least one lowercase letter')
        flag = 0
    # The entered password should have at least one uppercase letter
    if not any(char.isupper() for char in password):
        print('The entered password should have at least one uppercase letter')
        flag = 0
    # The entered password should have at least one of the symbols $@#_*
    if not any(char in AllowedSymbols for char in password):
        print('The entered password should have at least one of the symbols $@#_*')
        flag = 0
    if flag:
        return flag


def main():
    password = input()

    if (strong_password_detection(password)):
        print("The entered password is strong !!")
    else:
        print("The entered password is weak !!")


if __name__ == '__main__':
    main()
