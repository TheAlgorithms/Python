"""
LSB-Steganography is a steganography technique in which
we hide messages inside an image by replacing
Least significant bit of image with the bits of message to be hidden.
By modifying only the first most right bit of an image
we can insert our secret message
and it also make the picture unnoticeable,
but if our message is too large it
will start modifying the second right most bit and so on and an
attacker can notice the changes in picture.

source :
https://www.cybrary.it/blog/0p3n/hide-secret-message-inside-image-using-lsb-steganography/


Author: Seta
Github : https://github.com/SetaMurdha
Date: 2022.10.06

Author Note : I contribute this simple algorithm to celebrate my friend
    called Indriani A. Mentari for her bachelor graduation. *cheerss

"""

import cv2
import numpy as np


class LsbSteganography:
    """
    >>> path_encrypt = 'image_assets/original_image2.png'
    >>> path_decrypt = 'result.png'
    >>> abjad = 'abcdefghijklmnopqrstuvwxyz 1234567890`!?'
    >>> encrypt = LsbSteganography('abjad', 'path_encrypt')
    >>> encrypt.int_to_binary(23)
    '00010111'

    >>> encrypt.binary_to_int('10111001')
    185

    >>> encrypt.set_message('halo','`')
    >>> encrypt.preprocessing_encrypt_message()
    ['0', '0', '0', '0', '0', '1', '1', '1', '0', '0',
    '0', '0', '0', '0', '0', '0', '0', '0', '0',
    '0', '1', '0', '1', '1', '0', '0', '0', '0',
    '1', '1', '1', '0', '0', '0', '1', '0', '0',
    '1', '0', '1']

    >>> encrypt.preprocessing_image()
    [['11111111', '11111111',
    '11111111', '11111111',
    '11111111', '11111111',
    '11111111', '11111111'],
    ['11111111', '11001101',
    '00000000', '00000000',
    '00000000', '00000000',
    '11001101', '11111111'],
    ['11111111', '00000000',
    '10111000', '00000000',
    '00000000', '10111000',
    '00000000', '11111111'],
    ['11111111', '00000000',
    '00000000', '11001101',
    '11001101', '00000000',
    '00000000', '11111111'],
    ['11111111', '11111111',
    '11111111', '00000000',
    '00000000', '11111111',
    '11111111', '11111111'],
    ['11111111', '00000000',
    '00000000', '00000000',
    '00000000', '00000000',
    '00000000', '11111111'],
    ['11001101', '11111111',
    '00000000', '11001101',
    '11001101', '00000000',
    '11111111', '11001101'],
    ['11111111', '11111111',
    '00000000', '11001101',
    '11001101', '00000000',
    '11111111', '11111111']]

    >>> encrypt.lsb_encrypt()
    Encrypting....
    [['11111110', '11111110',
    '11111110', '11111110',
    '11111110', '11111111',
    '11111111', '11111111'],
    ['11111110', '11001100',
    '00000000', '00000000',
    '00000000', '00000000',
    '11001100', '11111110'],
    ['11111110', '00000000',
    '10111000', '00000000',
    '00000001', '10111000',
    '00000001', '11111111'],
    ['11111110', '00000000',
    '00000000', '11001100',
    '11001101', '00000001',
    '00000001', '11111110'],
    ['11111110', '11111110',
    '11111111', '00000000',
    '00000000', '11111111',
    '11111110', '11111111'],
    ['11111111', '00000000',
    '00000000', '00000000',
    '00000000', '00000000',
    '00000000', '11111111'],
    ['11001101', '11111111',
    '00000000', '11001101',
    '11001101', '00000000',
    '11111111', '11001101'],
    ['11111111', '11111111',
    '00000000', '11001101',
    '11001101', '00000000',
    '11111111', '11111111']]

    >>> encrypt.generate_encrypted_image()
    Encrypting....
    save success

    >>> algo_decrypt = LsbSteganography('abjad', 'path_decrypt')
    >>> print(algo_decrypt.lsb_decrypt('`'))
    decrypting....
    halo

    >>> main()
    Encrypting....
    save success
    decrypting....
    hello world

    """

    def __init__(self, abjad: str, img_path: str) -> None:
        self.abjad = abjad
        self.img_path = img_path

    def set_message(self, message: str, key: str) -> None:
        self.message = message.lower() + key

    def int_to_binary(self, words: int) -> str:
        return format(words, "08b")

    def binary_to_int(self, words: str) -> int:
        return int(words, 2)

    def preprocessing_encrypt_message(self) -> list:
        """
        Convert every character -->
        index in abjad (decimals)-->
        binary items in list (binary)

        """
        words_container = []

        for words in self.message:
            result = self.int_to_binary(self.abjad.find(words))
            for char in result:
                words_container.append(char)

        return words_container

    def preprocessing_image(self) -> list:

        """
        convert image to greyscale and every pixels to binary
        """

        result_binary = []

        img = cv2.imread(self.img_path, 0)

        for height in range(len(img)):
            result_width = []
            for width in range(len(img[height])):
                binary_width = self.int_to_binary(img[height][width])
                result_width.append(binary_width)

            result_binary.append(result_width)

        return result_binary

    def lsb_encrypt(self) -> list:
        """
        #Encrypting message to image pixels
        """

        print("Encrypting....")
        image_pixel = self.preprocessing_image()

        i = 0
        while i < len(self.preprocessing_encrypt_message()):
            for height in range(len(self.preprocessing_image())):
                for width in range(len(self.preprocessing_image()[height])):
                    if i < len(self.preprocessing_encrypt_message()):

                        words = list(self.preprocessing_image()[height][width])
                        words[-1] = self.preprocessing_encrypt_message()[i]
                        new_binary = "".join(words)
                        image_pixel[height][width] = new_binary
                        i += 1
                    else:
                        break

                if i >= len(self.preprocessing_encrypt_message()):
                    break

        return image_pixel

    def generate_encrypted_image(self) -> None:

        """
        #Create image from encrypted pixels

        """

        image_pixel = self.lsb_encrypt()

        final_pixel = []

        for height in range(len(image_pixel)):
            result_width = []
            for width in range(len(image_pixel[height])):
                pixel_width = self.binary_to_int(image_pixel[height][width])
                result_width.append(pixel_width)

            final_pixel.append(result_width)
        ar = np.asarray(final_pixel)
        cv2.imwrite("result.png", ar)
        print("save success")

    def lsb_decrypt(self, key: str) -> str:
        """
        Decrypting images
        """
        image_pixel = self.preprocessing_image()
        print("decrypting....")
        words = ""
        for height in range(len(image_pixel)):
            for width in range(len(image_pixel[height])):
                words += image_pixel[height][width][-1]

        words_character = []
        for index in range(0, len(words), 8):
            int_index = self.binary_to_int(words[index : index + 8])
            new_word = self.abjad[int_index]
            if new_word == key:
                break
            else:
                words_character.append(new_word)
        final_result = "".join(words_character)
        return final_result


def main():
    abjad = "abcdefghijklmnopqrstuvwxyz 1234567890`!?"
    message = "Hello World"
    path = "image_assets/original_image.png"
    path_decrypt = "result.png"
    key = "`"

    algo_encrypt = LsbSteganography(abjad, path)
    algo_encrypt.set_message(message, key)
    algo_encrypt.generate_encrypted_image()

    algo_decrypt = LsbSteganography(abjad, path_decrypt)
    print(algo_decrypt.lsb_decrypt(key))


if __name__ == "__main__":
    main()
