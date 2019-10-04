def get_sex(sex="unknown"):  # default initialization.
    if sex is "m":
        sex = "male"
    elif sex is "f":
        sex = "female"
    print(sex)


get_sex("f")
get_sex("m")
get_sex()

'''
def get_sex(sex):
    if sex is "m":
        sex = "male"
    elif sex is "f":
        sex = "female"
    else:
        sex = "unknown"
    print(sex)


get_sex("f")
get_sex("m")
get_sex(" ")
'''
