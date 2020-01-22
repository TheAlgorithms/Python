from src.dictionary import Dictionary


class LZW:
    def __init__(self):
        """
        LZW Constructor
        For more information, see https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
        """
        self.dictionary = Dictionary()

    def compression(self, text):
        """
        Compress the string with the LZW method

        :param text: The string that you want to compress
        :return: return the compress string in ASCII part into "_"
        """
        string = ""
        turn = 0
        while turn < len(text):
            i = 1
            save = text[turn]
            while (
                turn + i + 1 <= len(text)
                and self.dictionary.search(text[turn : turn + i]) != -1
            ):
                save = save + text[turn + i]
                i += 1
            if turn + i + 1 > len(text) and self.dictionary.search(save) != -1:
                string = string + str(self.dictionary.search(save))
                i += 1
            else:
                string = (
                    string + str(self.dictionary.search(save[0 : len(save) - 1])) + "_"
                )
            self.dictionary.add_to_dictionary(save)
            turn += i - 1
        return string

    def decompression(self, text):
        """
        Decompress a string with the method LZW

        :param text: The string that you want to decompress (in ASCII part into "_")
        :return: return the decompress string
        """
        string = ""
        turn = 0
        last_letter = 1
        save = ""
        compress_array = text.split("_")
        while turn < len(compress_array):
            i = 0
            string = string + self.dictionary.search_number(int(compress_array[turn]))
            if i + 1 <= len(text):
                save = save + self.dictionary.search_number(
                    int(compress_array[turn + i])
                )
            if self.dictionary.search(save) == -1:
                add_to_dictionary = True
                while last_letter < len(save) and add_to_dictionary:
                    if self.dictionary.search(save[0:last_letter]) == -1:
                        self.dictionary.add_to_dictionary(save[0:last_letter])
                        add_to_dictionary = False
                    last_letter += 1
                if add_to_dictionary:
                    self.dictionary.add_to_dictionary(save)
                    save = save[len(save) - 1]
                else:
                    save = save[1 : len(save)]
            turn += 1
            i += 1
        return string
