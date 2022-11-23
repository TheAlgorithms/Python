import re
from collections import Counter

class Regex:
    def __init__(self, text):
        self.text = text.lower()
        self.filtered_text = self.patt_utils()

    def regex_patt(self):
        """This function finds the most common three-letter words in a text."""
        if len(self.filtered_text) > 3:
            regex_find = re.findall(r'\b([a-z]{3})\b', self.filtered_text)
            return regex_find

    def patt_find(self):
        """This function finds the most common three-letter words in a text."""
        if len(self.filtered_text) > 3:
            c = Counter(self.filtered_text.split())
            return c.most_common(3)

    def patt_utils(self):
        """This function removes all non-alphabetic characters from a text."""
        filtered_text = re.sub(r'[^a-z]', " ", self.text)
        return filtered_text

    def regexer(self):
        """This function finds the most common three-letter words in a text."""
        if len(self.filtered_text) > 3:
            return re.findall(r'\b([a-z]{3})\b', self.filtered_text)

    def run(self):
        """This function runs the program."""
        if len(self.filtered_text) < 3:
            return "Text too short, must be atleast 3 characters"
        else:
            return f"Regex pattern: \n{self.regex_patt()}"

text = input("Enter text: ")
print()
regex = Regex(text)
print(regex.run())
print()
print(f"Three-letter words: \n{regex.patt_find()}")
print()
print(f"Regex pattern: \n{regex.regexer()}")
