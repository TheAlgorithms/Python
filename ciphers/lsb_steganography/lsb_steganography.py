"""
LSB Steganography is steganography method to hide a message in the image file

I contribute this algorithm to celebrate my girl friend called Indriani A. M., her bachelor graduation. cheers
"""

import cv2

class lsb_steganography:
    def __init__(self, abjad, img_path):
        self.abjad = abjad
        self.img_path = img_path

    def set_message(self, message):
        self.message = message.lower() + "`"

    def preprocessing_image(self):
        img = cv2.imread(self.img_path,0)
        
        return img

    def preprocessing_message(self):

        words_container = []

        for words in self.message:
            result = self.abjad.find(words)
            words_container.append(result)

        return words_container

    def lsb(self):
        print(self.preprocessing_image())


        


def main():
    abjad = "abcdefghijklmnopqrstuvwxyz 1234567890`"
    message = "Hello World"
    path = "image_assets/lsb.png"

    algo = lsb_steganography(abjad, path)
    algo.set_message(message)
    algo.lsb()




if __name__ == "__main__":
    main()