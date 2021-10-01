#wikipedia - https://en.wikipedia.org/wiki/Bacon%27s_cipher
lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}

def encrypt(message: str) -> str:
    cipher = ''
    for letter in message:

        if(letter != ' '):

            cipher += lookup[letter]
        else:

            cipher += ' '

    return cipher


def decrypt(message: str)-> str:
    ```
    baabbaabaabaababaabb abbaaaabaabaababaabaaaaaaaabbaaabaa
    ENJOY
    ```
    decipher = ''
    i = 0

    while True :

        if(i < len(message)-4):

            substr = message[i:i + 5]

            if(substr[0] != ' '):
                '''
                This statement gets us the key(plaintext) using the values(ciphertext)
                Just the reverse of what we were doing in encrypt function
                '''
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
                i += 5

            else:
                decipher += ' '
                i += 1
        else:
            break

    return decipher

def main() -> str:
    message = "Test Message"
    result = encrypt(message.upper())
    print (result)

    message = "AABAAABBABABAABABBBABBAAA"
    result = decrypt(message.lower())
    print (result)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
