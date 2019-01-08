from __future__ import print_function
import time, os, sys
import transposition_cipher as transCipher

def main():
    inputFile = 'Prehistoric Men.txt'
    outputFile = 'Output.txt'
    key = int(input('Enter key: '))
    mode = input('Encrypt/Decrypt [e/d]: ')

    if not os.path.exists(inputFile):
        print('File %s does not exist. Quitting...' % inputFile)
        sys.exit()
    if os.path.exists(outputFile):
        print('Overwrite %s? [y/n]' % outputFile)
        response = input('> ')
        if not response.lower().startswith('y'):
            sys.exit()
            
    startTime = time.time()
    if mode.lower().startswith('e'):
        with open(inputFile) as f:
            content = f.read()
        translated = transCipher.encryptMessage(key, content)
    elif mode.lower().startswith('d'):
        with open(outputFile) as f:
            content = f.read()
        translated =transCipher .decryptMessage(key, content)

    with open(outputFile, 'w') as outputObj:
        outputObj.write(translated)
    
    totalTime = round(time.time() - startTime, 2)
    print(('Done (', totalTime, 'seconds )'))
    
if __name__ == '__main__':
    main()
