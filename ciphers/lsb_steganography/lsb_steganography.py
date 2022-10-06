"""
LSB Steganography is steganography method to hide a message in the image file

I contribute this algorithm to celebrate my girl friend called Indriani A. Mentari, 
    her bachelor graduation. cheers

"""

import cv2
import numpy as np

class lsb_steganography:
    def __init__(self, abjad, img_path):
        self.abjad = abjad
        self.img_path = img_path

    def set_message(self, message, key):
        self.message = message.lower() + key 

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
        
        image_pixel = self.preprocessing_image()

        i = 0
        while i < len(self.preprocessing_encrypt_message()):
            for height in range(len(self.preprocessing_image())):
                for width in range(len(self.preprocessing_image()[height])):
                    if(i<len(self.preprocessing_encrypt_message())):

                        words = list(self.preprocessing_image()[height][width])
                        words[-1] = self.preprocessing_encrypt_message()[i]
                        new_binary = ''.join(words)
                        image_pixel[height][width] = new_binary
                        i+=1
                    else:
                        break  

                if(i>=len(self.preprocessing_encrypt_message())):
                    break  

        return image_pixel

    def generate_encrypted_image(self):
        image_pixel = self.lsb_encrypt()

        final_pixel = []

        for height in range(len(image_pixel)):
            result_width = []
            for width in range(len(image_pixel[height])):
                pixel_width = self.binary_to_int(image_pixel[height][width])
                result_width.append(pixel_width)

            final_pixel.append(result_width)
        ar = np.asarray(final_pixel)
        cv2.imwrite("Result.png", ar)
        print("save success")
    
        
    def lsb_decrypt(self, key):
        image_pixel = self.preprocessing_image()
        words = ''
        for height in range(len(image_pixel)):
            for width in range(len(image_pixel[height])):
                words += image_pixel[height][width][-1]

        words_character = []
        for index in range(0, len(words), 8):
            int_index = self.binary_to_int(words[index:index+8])
            new_word = self.abjad[int_index]
            if new_word == key:
                break
            else:
                words_character.append(new_word)
        final_result = ''.join(words_character)
        return final_result

def main():
    abjad = "abcdefghijklmnopqrstuvwxyz 1234567890`"
    message = "Hello Goddamn Fucking World"
    path = "image_assets/original_image.png"
    path_decrypt = "Result.png"
    key = '`'

    algo_encrypt = lsb_steganography(abjad, path)
    algo_encrypt.set_message(message,key)
    algo_encrypt.generate_encrypted_image()

    algo_decrypt = 
    print(algo.lsb_decrypt(key))


if __name__ == "__main__":
    main()