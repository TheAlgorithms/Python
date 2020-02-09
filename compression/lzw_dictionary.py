class Dictionary:
    def __init__(self):
        """
        Dictionary constructor
        """
        self.dictionary = dict()

    def search(self, letter: str):
        """
        Search a char or a string in dictionary
        :param letter:  char or string that you want to search
        :return: the ASCII code letter or -1/-2 if it doesn't exist
        """

        if len(letter) == 1:
            return ord(letter)
        else:
            if letter in self.dictionary:
                return self.dictionary.get(letter)
            elif letter == "":
                return -2
            else:
                return -1

    def add_to_dictionary(self, add: str):
        """
        Add a string to dictionary with the following ASCII code (start at 257)
        :param add: string that you want to add to dictionary
        """
        self.dictionary[add] = str(257 + len(self.dictionary))

    def print_dictionary(self):
        """
        Show the dictionary entries
        """
        for key, word in enumerate(self.dictionary):
            print(str(key) + " : " + word)

    def search_number(self, number: int):
        """
        Search and return a letter or a string with it ASCII code
        :param number: ASCII code number
        :return: letter or a string of the ASCII code
        """
        if number < 256:
            return str(chr(number))
        else:
            for key, word in self.dictionary.items():
                if int(word) == number:
                    return key
