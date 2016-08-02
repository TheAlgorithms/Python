# The Caesar Cipher Algorithm

def main():
    message = input("Enter message: ")
    key = int(input("Key [1-26]: "))
    mode = input("Encrypt or Decrypt [e/d]: ")

    if mode.lower().startswith('e'):
        mode = "encrypt"
    elif mode.lower().startswith('d'):
        mode = "decrypt"

    translated = encdec(message, key, mode)
    if mode == "encrypt":
        print("Encryption:", translated)
    elif mode == "decrypt":
        print("Decryption:", translated)
        
def encdec(message, key, mode):
    """
    >>> encdec('Harshil Darji', 12, 'encrypt')
    'TMDETUX PMDVU'

    >>> encdec('TMDETUX PMDVU', 12, 'decrypt')
    'HARSHIL DARJI'
    """
    message = message.upper()
    translated = ""
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == "encrypt":
                num = num + key
            elif mode == "decrypt":
                num = num - key

            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    return translated

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()