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


def int_to_binary(words: int) -> str:
    return format(words, "08b")


def binary_to_int(words: str) -> int:
    return int(words, 2)


def lsb_encrypt(message: str, abjad: str, img_path: str, key: str) -> str:
    """
    Encrypting message to image pixels
    """
    print("Encrypting....")

    words_container = []

    message += key
    for words in message:
        result = int_to_binary(abjad.find(words.lower()))
        for char in result:
            words_container.append(char)

    result_binary = []

    img = cv2.imread(img_path, 0)

    for height in range(len(img)):
        result_width = []
        for width in range(len(img[height])):
            binary_width = int_to_binary(img[height][width])
            result_width.append(binary_width)

        result_binary.append(result_width)
    image_pixel = result_binary
    i = 0
    while i < len(words_container):
        for height in range(len(result_binary)):
            for width in range(len(result_binary[height])):
                if i < len(words_container):

                    words = list(result_binary[height][width])
                    words[-1] = words_container[i]
                    new_binary = "".join(words)
                    image_pixel[height][width] = new_binary
                    i += 1
                else:
                    break

            if i >= len(words_container):
                break

    final_pixel = []

    for height in range(len(image_pixel)):
        result_width = []
        for width in range(len(image_pixel[height])):
            pixel_width = image_pixel[height][width]

            result_width.append(binary_to_int(pixel_width))

        final_pixel.append(result_width)
    ar = np.asarray(final_pixel)
    cv2.imwrite("result.png", ar)
    return "save success"


def lsb_decrypt(img_path: str, abjad: str, key: str) -> str:
    """
    Decrypting images
    """
    print("decrypting....")

    result_binary = []

    img = cv2.imread(img_path, 0)

    for height in range(len(img)):
        result_width = []
        for width in range(len(img[height])):
            binary_width = int_to_binary(img[height][width])
            result_width.append(binary_width)

        result_binary.append(result_width)
    image_pixel = result_binary

    words = ""
    for height in range(len(image_pixel)):
        for width in range(len(image_pixel[height])):
            words += image_pixel[height][width][-1]

    words_character = []
    for index in range(0, len(words), 8):
        int_index = binary_to_int(words[index : index + 8])
        new_word = abjad[int_index]
        if new_word == key:
            break
        else:
            words_character.append(new_word)
    final_result = "".join(words_character)
    return final_result


def main() -> None:
    """
    >>> img_path = "image_data/lena_small.jpg"
    >>> img_path_decrypt = "result.png"
    >>> key = "`"
    >>> abjad = "abcdefghijklmnopqrstuvwxyz 1234567890`!?"
    >>> lsb_encrypt("Hello", abjad, img_path, key)
    Encrypting....
    'save success'
    >>> lsb_decrypt(img_path_decrypt, abjad, key)
    decrypting....
    'hell'
    >>> main()
    Encrypting....
    save success



    """
    abjad = "abcdefghijklmnopqrstuvwxyz 1234567890`!?"
    message = "hello"
    path = "image_data/lena_small.jpg"
    path_decrypt = "result.png"
    key = "`"

    img_path = "lena_small.jpg"
    abjad = "abcdefghijklmnopqrstuvwxyz 1234567890`!?"
    print(lsb_encrypt("Hello", abjad, img_path, key))


if __name__ == "__main__":
    main()
