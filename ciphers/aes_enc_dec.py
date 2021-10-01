import sys, base64, json, math
try:
   from Crypto.Cipher import AES
except ImportError:
   print ("Error!! Module AES is required. Run either or following commands")
   print("pip install pycrypto")
   print("---------OR--------")
   print("pip3 install pycrypto")
   sys.exit()

KEY=""
PADDING_CHARACTER="S"
VECTOR_FOR_AES="SUDESH1611GITHUB"

def GetKey():
    global KEY
    tempKey = input("Enter password(min length: 8, max length: 32)")
    while(len(tempKey.strip())<8 or len(tempKey.strip())>32 or ' ' in tempKey):
        if(' ' in tempKey):
            print("White spaces are not allowed!")
        else:
            print("Password must be at least 8 characters long and at max 32 characters long. Try Again!")
    while(len(tempKey)%8!=0):
        tempKey+=PADDING_CHARACTER
    KEY=tempKey

def AES_Encryption(cleartext):
    if(len(KEY)<8 or len(KEY)%8!=0):
        print("Password is corrupted. Exiting!")
        sys.exit()
        return
    AES_Encryptor = AES.new(KEY,AES.MODE_CBC,VECTOR_FOR_AES)
    cleartext_length = len(cleartext)
    nearest_multiple_of_16 = 16 * math.ceil(cleartext_length/16)
    padded_cleartext = cleartext.rjust(nearest_multiple_of_16)
    raw_ciphertext = AES_Encryptor.encrypt(padded_cleartext)
    return base64.b64encode(raw_ciphertext).decode('utf-8')

def AES_Decryption(ciphertext):
    if(len(KEY)<8 or len(KEY)%8!=0):
        print("Password is corrupted. Exiting!")
        sys.exit()
        return
    AES_Decryptor = AES.new(KEY,AES.MODE_CBC,VECTOR_FOR_AES)
    raw_ciphertext = base64.b64decode(ciphertext)
    decrypted_message_with_padding = AES_Decryptor.decrypt(raw_ciphertext)
    return decrypted_message_with_padding.decode('utf-8').strip()

if __name__ == "__main__":
    type="S"
    while(type not in "ed"):
        type = input("Encrypt or Decrypt the text(e/d): ")
        type = type.strip().lower()
        if(len(type)!=1):
            type="S"
    GetKey()
    if(type=="e"):
        print("NOTE: If you forget this password, you will not be able to decrypt text correctly. So, DO NOT FORGET PASSWORD!!")
        message = input("Enter message in single line: ")
        ciphertext = AES_Encryption(message)
        print("Encrypted Message: %s" % ciphertext)
    else:
        encText = input("Enter encrypted message: ")
        message = AES_Decryption(encText)
        print("Original Message: %s" % message)