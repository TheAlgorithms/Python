"""
LSB Steganography is steganography method to hide a message in the image file

I contribute this algorithm to celebrate my girl friend called Indriani A. Mentari, 
    her bachelor graduation. cheers

"""

import cv2

class lsb_steganography:
    def __init__(self, abjad, img_path):
        self.abjad = abjad
        self.img_path = img_path

    def set_message(self, message):
        self.message = message.lower() + "`"

    def int_to_binary(self, words):
        return format(words,'08b')

    def binary_to_int(self, words):
        return int(words,2)

    def preprocessing_encrypt_message(self):

        words_container = []

        for words in self.message:
            result = self.int_to_binary(self.abjad.find(words))
            for char in result:
                words_container.append(int(char))

        return words_container

    def preprocessing_decrypt_message(self):
        pass

    def preprocessing_image(self):
        img = cv2.imread(self.img_path,0)

        # for height in range(len(img)):
        #     for width in range(len(img[height])):
        #         print(width)
        #     print("---")
        
        return img


    def lsb(self):
        print(self.preprocessing_encrypt_message())


        


def main():
    abjad = "abcdefghijklmnopqrstuvwxyz 1234567890`"
    message = "Hello World"
    path = "image_assets/lsb.png"

    algo = lsb_steganography(abjad, path)
    algo.set_message(message)
    algo.lsb()




if __name__ == "__main__":
    main()