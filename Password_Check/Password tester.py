from itertools import product


def findPassword(chars, function, show=50, format_="%s"):

    password = None
    attempts = 0
    size = 1
    stop = False

    while not stop:

        for pw in product(chars, repeat=size):

            password = "".join(pw)

            if attempts % show == 0:
                """
                condition runs every time when a new password is generated and not equal to given password.
                """
                print(format_ % password)

            if function(password):
                """
                condition runs every time when a new password is generated and  equal to given password.
                """
                stop = True
                break
            else:
                attempts += 1
        size += 1

    return password, attempts


def getChars():
    """
    Function to generate password similar to given password by tring all posible combimations.
    """
    chars = []

    for id_ in range(ord("A"), ord("Z") + 1):
        chars.append(chr(id_))

    for id_ in range(ord("a"), ord("z") + 1):
        chars.append(chr(id_))
    for number in range(10):
        chars.append(str(number))

    return chars


if __name__ == "__main__":

    import datetime
    import time

    logo_shiv = """
    #----------------------------------#
    #----------------------------------#
    #   PROJECT Password tester        #
    #   AUTHOR:- SHIVAM SINGH          #
    #----------------------------------#
    #----------------------------------#
    # this is made for password testing #
    # purpose only so please do't       #
    #        misuse  this               #
    #-----------------------------------#"""
    print(logo_shiv)
    pw = input("\n Please enter the password which you want to check: ")
    print("\n")

    def testFunction(password):
        """
        function to check whether the generated password match to given password or not.
        if match return true else return false
        """
        global pw
        if password == pw:
            return True
        else:
            return False

    chars = getChars()

    t = time.process_time()

    password, attempts = findPassword(
        chars, testFunction, show=1000, format_=" Trying %s"
    )

    t = datetime.timedelta(seconds=int(time.process_time() - t))
    print(
        f"\n\n Password found: {password}\n No Of Attempts: {attempts}\n Time to found: {t}\n"
    )
