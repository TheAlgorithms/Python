# Acronym
"""
Given a string s representing a phrase, return its acronym. Acronyms should be capitalized and should not include the word "and".

Example 1
Input

s = "For your information"
Output

"FYI"
Example 2
Input

s = "National Aeronautics and Space Administration"
Output

"NASA"
"""

import unittest


def acronym(s):
    acronym = ""
    for word in s.split():
        if(word!="and"):
            acronym = acronym + word[0].upper()
    return acronym

# DO NOT TOUCH THE BELOW CODE


class TestAcronym(unittest.TestCase):

    def test_01(self):
        input_string = "For your information"
        output_string = "FYI"

        self.assertEqual(acronym(input_string), output_string)

    def test_02(self):
        input_string = "National Aeronautics and Space Administration"
        output_string = "NASA"

        self.assertEqual(acronym(input_string), output_string)

    def test_03(self):
        input_string = "As soon as possible"
        output_string = "ASAP"

        self.assertEqual(acronym(input_string), output_string)

    def test_04(self):
        input_string = "United Nations Educational, Scientific and Cultural Organization"
        output_string = "UNESCO"

        self.assertEqual(acronym(input_string), output_string)


if __name__ == '__main__':
    unittest.main(verbosity=2)
