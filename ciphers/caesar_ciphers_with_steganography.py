#!/usr/bin/env python
"""
Concealing Ciphered Text in Images
"""
import argparse
from PIL import Image


def encrypt(string: str, shift: int) -> str:
    """
    encrypt
    =======
    Encodes a given string with the caesar cipher and returns the encoded
    message
    Parameters:
    -----------
    *   string: the plain-text that needs to be encoded
    *   shift: the number of letters to shift the message by

    Returns:
    *   A string containing the encoded cipher-text
    Doctests
    ========
    >>> encrypt('The quick brown fox jumps over the lazy dog', 8)
    'bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo'
    >>> encrypt('A very large key', 8000)
    's nWjq dSjYW cWq'
    """
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

def decrypt(string, shift):
    """
    decrypt
    =======
    Decodes a given string of cipher-text and returns the decoded plain-text
    Parameters:
    -----------
    *   string: the cipher-text that needs to be decoded
    *   shift: the number of letters to shift the message backwards by to decode
    Returns:
    *   A string containing the decoded plain-text
    Doctests
    ========
    >>> decrypt('bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo', 8)
    'The quick brown fox jumps over the lazy dog'
    >>> decrypt('s nWjq dSjYW cWq', 8000)
    'A very large key'
    """
    decipher = ''
    for char in string:
        if char == ' ':
            decipher = decipher + char
        elif  char.isupper():
            decipher = decipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decipher = decipher + chr((ord(char) - shift - 97) % 26 + 97)
    return decipher



# Convert encoding data into 8-bit form using ASCII value of characters
def gen_data(data):
    """
    gen_data
    =======
    Generates a list containing 8 bit binary representation of the data
    Parameters:
    -----------
    *   data: the cipher-text that needs to converted to 8 bit binary strings
    Returns:
    *   A list containing the 8 bit binary strings
    Doctests
    ========
    >>> gen_data('Tqxxa Iadxp')
    ['01010100', '01110001', '01111000', '01111000', '01100001']
    >>> gen_data('Iadxp')
    ['01001001', '01100001', '01100100', '01111000', '01110000']
    """
    # list of binary codes of given data
    newdata = []

    #Getting 8 bits bianry representation of the letters present in the string.
    for i in data:
        newdata.append(format(ord(i), '08b'))
    return newdata


# Pixels are modified according to the 8-bit binary data and finally returned
def alter_pixel(pix, data):
    """
    alter_pixel
    =======
    Alters the pixel value of the image according to the data provided
    Parameters:
    -----------
    *   pix: contents of the image as a sequence object containing pixel values
    *   data: the ciphered string
    Returns:
    *   A tuple of triplet altered pixel values with the help of yield
    Doctests
    ========
    >>> alter_pixel(cloneimg.getdata(), "Tqxxa Iadxp")
    (100, 101, 100)
    (77, 78, 77)
    (54, 56, 54)
    (86, 85, 85)
    (65, 64, 66)
    (46, 45, 46)
    (106, 107, 105)
    (89, 87, 88)
    (72, 70, 72)
    (102, 103, 103)
    (75, 75, 76)
    (50, 48, 48)
    (70, 69, 67)
    (54, 52, 52)
    """
    datalist = gen_data(data)
    lendata = len(datalist)
    # The iter() function creates an object which can be iterated one element at a time.
    iterdata = iter(pix)
    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in iterdata.__next__()[:3] \
            + iterdata.__next__()[:3] + iterdata.__next__()[:3]]

        # Pixel value should be made odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1
        #Eighth pixel of every set tells whether to stop or read further.
        #0 means keep reading; 1 means the message is over.
        #i==lendata-1 means we read the last 8-bit binary value
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1

        pix = tuple(pix)
        #yield is a keyword in Python that is used to return from a function
        #without destroying the states of its local variable
        #and when the function is called, the execution starts from the last yield statement
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

#Encoding the data
def encode_data(cloneimg, data):
    """
    encode
    =======
    Encodes the string provided in the parameter data into the image and saves as new_img_name
    Parameters:
    -----------
    *   img: the original image in which the data needs to be encoded
    *   data: the the string to be encoded in the image
    *   new_img_name: the new image which contains the encoded data
    Returns:
    *   True, after completion of all the steps
    Doctests
    ========
    >>> encode(abc.png,"Hello World",xyz.png)
    True

    """
    # w is the width of the image
    width_image = cloneimg.size[0]
    (x_val, y_val) = (0, 0)

    # getdata() Returns the contents of this image as a sequence object containing pixel values.
    # The sequence object is flattened, so that values for
    # line one follow directly after the values of line zero, and so on.
    # The default is to return all bands.
    # To return a single band, pass in the index value
    # (e.g. 0 to get the “R” band from an “RGB” image)
    for pixel in alter_pixel(cloneimg.getdata(), data):

        # Putting modified pixels in the new image
        cloneimg.putpixel((x_val, y_val), pixel)
        if x_val == width_image - 1:
            x_val = 0
            y_val += 1
        else:
            x_val += 1

# Encode data into image
def encode(img,data,new_img_name):
    """
    encode
    =======
    Encodes the string provided in the parameter data into the image and saves as new_img_name
    Parameters:
    -----------
    *   img: the original image in which the data needs to be encoded
    *   data: the ciphered string to be encoded in the image
    *   new_img_name: the new image which contains the encoded data
    Returns:
    *   True, after completion of all the steps

    More on the Image based Steganography
    =========================
    Steganography is the method of hiding secret data in any image/audio/video.
    In a nutshell, the main motive of steganography is to hide the intended information
    within any image/audio/video that doesn’t appear to be secret just by looking at it.
    The idea behind image-based Steganography is very simple.
    Images are composed of digital data (pixels), which describes what’s inside the picture,
    usually the colors of all the pixels.
    Since we know every image is made up of pixels
    and every pixel contains 3-values (red, green, blue).
    Further reading
    ===============
    *   https://www.geeksforgeeks.org/image-based-steganography-using-python/

    Doctests
    ========
    >>> encode(abc.png,"Hello World",xyz.png)
    True
    """
    image = Image.open(img, 'r')
    if len(data) == 0:
        raise ValueError('Empty data received from the user.')

    cloneimg = image.copy()
    encode_data(cloneimg, data)

    cloneimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

    return True

# Decode the data in the image
def decode(img):
    """
    decode
    =======
    Decodes the hidden text from the image and returns the string
    Parameters:
    -----------
    *   img: the image containing the hidden string
    Returns:
    *   A string decoded from the image
    Doctests
    ========
    >>> decode(abc.png)
    Tqxxa Iadxp
    """
    image = Image.open(img, 'r')

    data = ''
    # The iter() function creates an object which can be iterated one element at a time.
    iterdata = iter(image.getdata())
    while True:
        pixels = [value for value in iterdata.__next__()[:3] \
            + iterdata.__next__()[:3] + iterdata.__next__()[:3]]

        # string of binary data
        binarystr = ''
        #Each string of 8-bit binary data would represent a letter/character
        for i in pixels[:8]:
            if i%2 == 0:
                binarystr += '0'
            else:
                binarystr += '1'

        data += chr(int(binarystr, 2))
        if pixels[-1] % 2 != 0:
            return data

def main():
    """
    main
    =======
    Driver function

    Test Case 1: Encoding
    > python caesar_ciphers_with_steganography.py --encode OriginalImage.png
    --key 13 --message "Hello World" --newimg encodeImg.png
    Output:
    ********************* Caesar cipher with Steganography *********************
    [*] Encoding data in the image initiated.
    [*] Image name: OriginalImage.png

    [+] Data ciphered successfully --------- [50%  Completed]
    [+] Encoding successful ---------------- [100% Completed]

    [+] The new image is saved as: encodeImg.png

    Test Case 2: Decoding
    >  python caesar_ciphers_with_steganography.py --decode encodeImg.png --key 13
    Output:
    ********************* Caesar cipher with Steganography *********************
    [*] Decoding data from the image initiated
    [*] Image name: encodeImg.png

    [+] Decoding successful ----------------- [50%  Completed]
    [+] Data deciphered successful ---------- [100% Completed]

    [+] The data decoded and deciphered from the image is:  Hello World
    [+] Task Completed

    Test Case 3: No arguments provided
    > python caesar_ciphers_with_steganography.py
    Output:
    ********************* Caesar cipher with Steganography *********************
    [-] No arguments were provided.
    [*] Type 'python filename.py -h' or 'python filename.py --help' for help.

    Test Case 4: For help
    > python caesar_ciphers_with_steganography.py --help
    Output:
    ********************* Caesar cipher with Steganography *********************
    usage: caesar_ciphers_with_steganography.py [-h] [-k KEY] [-m MESSAGE]
                                            [-e ENCODE] [-n NEWIMG]
                                            [-d DECODE] [-s SYNTAX]

    optional arguments:
        -h, --help            show this help message and exit
        -k KEY, --key KEY     insert your shift key for cipher
        -m MESSAGE, --message MESSAGE
                        insert your message here
        -e ENCODE, --encode ENCODE
                        name of the image file where we want to hide the
                        message
        -n NEWIMG, --newimg NEWIMG
                        name of the new image file where data will be hidden
        -d DECODE, --decode DECODE
                        name of the image file which has the hidden message
        -s SYNTAX, --syntax SYNTAX
                        Type 'python filename.py -s YES' or 'python
                        filename.py --syntax YES'
    ========
    """
    print("\n********************* Caesar cipher with Steganography *********************")

    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-k", "--key", help = "insert your shift key for cipher",type=int)
    parser.add_argument("-m", "--message", help = "insert your message here")
    parser.add_argument("-e", "--encode", \
        help = "name of the image file where we want to hide the message")
    parser.add_argument("-n", "--newimg", \
        help = "name of the new image file where data will be hidden")
    parser.add_argument("-d", "--decode", \
        help = "name of the image file which has the hidden message")
    parser.add_argument("-s", "--syntax", \
        help = "Type 'python filename.py -s YES' or 'python filename.py --syntax YES'")
    # Read arguments from command line
    args = parser.parse_args()
    syntaxhelp = False
    if args.syntax:
        print("[*] To encode use the following syntax:")
        print("python filename.py -e [image name with extension]"\
            " -n [new image name with extension] -k [shift key, an integer value]"\
                " -m [Your string to be encoded within inverted commas]\n")
        print("[*] To decode use the following syntax:")
        print("python filename.py -d [image name with extension where the data is hidden]"\
            " -k [shift key, an integer value]\n")
        syntaxhelp = True
    if not syntaxhelp:
        if args.encode is None and args.decode is None:
            print("\n\n[-] No arguments were provided.")
            print("[*] Type 'python filename.py -h' or 'python filename.py --help' for help.\n\n")

        if args.encode:
            print("[*] Encoding data in the image initiated.\n[*] Image name: % s\n" % args.encode)
            if args.key is None or args.message is None or args.newimg is None:
                print("Process terminated due to lack of arguments!")
            else:
                msg = encrypt(args.message,args.key)
                print("[+] Data ciphered successfully --------- [50%  Completed]")
                if encode(args.encode,msg,args.newimg):
                    print("[+] Encoding successful ---------------- [100% Completed]\n")
                    print("[+] The new image is saved as: % s\n" % args.newimg)
        if args.decode:
            print("[*] Decoding data from the image initiated")
            print("[*] Image name: % s\n" % args.decode)
            if args.key:
                ciphermsg = decode(args.decode)
                print("[+] Decoding successful ----------------- [50%  Completed]")
                msg = decrypt(ciphermsg, args.key)
                print("[+] Data deciphered successful ---------- [100% Completed]\n")
                print("[+] The data decoded and deciphered from the image is: ",msg)
                print("[+] Task Completed")
if __name__ == "__main__":
    main()
