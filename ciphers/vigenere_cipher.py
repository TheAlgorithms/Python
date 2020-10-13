class cipher:
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encryptMessage(self, key, message):
        """
        encryptMessage('HDarji', 'This is Harshil Darji from Dharmaj.')
        'Akij ra Odrjqqs Gaisq muod Mphumrs.'
        """
        return ob.translateMessage(key, message, "encrypt")

    def decryptMessage(self, key, message):
        """
        decryptMessage('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
        'This is Harshil Darji from Dharmaj.'
        """
        return ob.translateMessage(key, message, "decrypt")

    def translateMessage(self, key, message, mode):
        global translated
        translated=[]
        keyIndex = 0
        key = key.upper()

        for symbol in message:
            num = self.LETTERS.find(symbol.upper())
            if num != -1:
                if mode == "encrypt":
                    num += self.LETTERS.find(key[keyIndex])
                elif mode == "decrypt":
                    num -= self.LETTERS.find(key[keyIndex])

                num %= 26

                if symbol.isupper():
                    translated.append(self.LETTERS[num])
                elif symbol.islower():
                    translated.append(self.LETTERS[num].lower())

                keyIndex += 1
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                translated.append(symbol)
        return "".join(translated)


ob = cipher()

if __name__ == "__main__":
    while (1):
        mode = input("Encrypt/Decrypt/quit: ")

        if mode.lower()=="encrypt":
            mode = "encrypt"
            message = input("Enter message: ")
            key = input("Enter key : ")

            translated = ob.encryptMessage(key, message)
            print("{}ed message: ".format(mode.title()), translated)

        elif mode.lower()=="decrypt":
            mode = "decrypt"
            message = input("Enter message: ")
            key = input("Enter key [alphanumeric]: ")

            translated = ob.decryptMessage(key, message)
            print("{}ed message: ".format(mode.title()), translated)

        elif mode.lower().startswith("q"):
            break
            
        else:
            print("Please enter a proper option")


