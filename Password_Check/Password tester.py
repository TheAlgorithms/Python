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
                print(format_ % password)

            if function(password):
                stop = True
                break
            else:
                attempts += 1
        size += 1

    return password, attempts


def getChars():

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
    input(
        "\n\n Password found: {}\n No Of Attempts: {}\n Time to found: {}\n".format(
            password, attempts, t
        )
    )
