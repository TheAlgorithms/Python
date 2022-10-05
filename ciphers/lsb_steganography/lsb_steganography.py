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
                words_container.append(char)

        return words_container

    def preprocessing_decrypt_message(self):
        pass

    def preprocessing_image(self):

        result_binary = []

        img = cv2.imread(self.img_path,0)

        for height in range(len(img)):
            result_width = []
            for width in range(len(img[height])):
                binary_width = self.int_to_binary(img[height][width])
                result_width.append(binary_width)

            result_binary.append(result_width)
        
        return result_binary


    def lsb_encrypt(self):
        
        i = 0
        while i <= len(self.preprocessing_encrypt_message()):
            for height in range(len(self.preprocessing_image())):
                for width in range(len(self.preprocessing_image()[height])):
                    if(i<=len(self.preprocessing_encrypt_message())):
                        print(str(i)+" = "+self.preprocessing_image()[height][width])
                        i+=1
                    else:
                        break    
            print("-----")

        print(self.preprocessing_image())


        


def main():
    abjad = "abcdefghijklmnopqrstuvwxyz 1234567890`"
    message = "Hello World"
    path = "image_assets/lsb.png"

    algo = lsb_steganography(abjad, path)
    algo.set_message(message)
    algo.lsb_encrypt()




if __name__ == "__main__":
    main()