# The main purpose of this is to get secure password to defend against Bruteforce attacks.


import string
import random
import re

if __name__ == '__main__':
    s1 = string.ascii_uppercase  # including uppercase letters to the set.

    s2 = string.ascii_lowercase  # including lowercase letters to the set.

    s3 = string.digits  # including digits to the set.

    s4 = string.punctuation  # including symbols to the set.

    # declaring password length that useer will give for password generation.
    passlen = input("Enter password length max: 2 digit. \n")
    num_format = re.compile(r'[1-9][0-9]*$')
    it_is = re.match(num_format, passlen)

    if it_is:
        print("True")
        new_length= int(passlen)    # The input() will take it as string but we change it to  int because we are storing lenght.
        s = []  # creating our sets of numberals , alphabets and symbols.

        s.extend(list(s1))  # adding the elements of s1 to the set s.
        s.extend(list(s2))  # adding the elements of s2 to the set s.
        s.extend(list(s3))  # adding the elements of s3 to the set s.
        s.extend(list(s4))  # adding the elements of s4 to the set s.

        # It shuffles our set 's' so that each and everytime we ue we get different password.
        random.shuffle(s)

        print("The password is : \n")
        print("".join(s[0:new_length]))  # prints the password upto passlen= new length now.

    else:
            
        print(" Not a Valid lenght")
        # int() will handle gibberish and throw error.   
