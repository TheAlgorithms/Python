"""
    Author : Sushan Shakya

    This script is used to generate Random Id for Mock data of variable length.
    The Id generated Includes numbers | lowercase | uppercase characters

    Modifications:
        Change [id_len] to change the length of id

        Change [generation_count] to change the number of Ids generated
"""

import random

def generate_random_number() -> str:
    return str(int(random.random() * 100))

def generate_uppercase() -> str:
    r = random.randint(65,90)
    return chr(r)

def generate_lowercase() -> str:
    r = random.randint(97,122) 
    return chr(r)

id_len = 10
generation_count = 100

def generate_id() -> str:
    res = ""
    while(len(res) < id_len):

        r = int(random.random() * 10) % 5
        s = int(random.random() * 10) % 6
        t = int(random.random() * 10) % 10
        for i in range(r):
            res += generate_random_number()

        for i in range(s):
            res += generate_uppercase()
        for i in range(t):
            res += generate_lowercase()

    return res[0:id_len]

ids = []

for i in range(generation_count):
    ids.append(generate_id())

print(",".join(ids))



