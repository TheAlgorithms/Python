from __future__ import print_function
import time, os, sys
import transposition_cipher as transCipher

def main():
    inputFile = 'Prehistoric Men.txt'
    outputFile = 'Output.txt'
    key = int(raw_input('Enter key: '))
    mode = raw_input('Encrypt/Decrypt [e/d]: ')

    if not os.path.exists(inputFile):
        print('File %s does not exist. Quitting...' % inputFile)
        sys.exit()
    if os.path.exists(outputFile):
        print('Overwrite %s? [y/n]' % outputFile)
        response = raw_input('> ')
        if not response.lower().startswith('y'):
            sys.exit()
            
    startTime = time.time()
    if mode.lower().startswith('e'):
        content = open(inputFile).read()
        translated = transCipher.encryptMessage(key, content)
    elif mode.lower().startswith('d'):
        content = open(outputFile).read()
        translated =transCipher .decryptMessage(key, content)

    outputObj = open(outputFile, 'w')
    outputObj.write(translated)
    outputObj.close()
    
    totalTime = round(time.time() - startTime, 2)
    print(('Done (', totalTime, 'seconds )'))
    
if __name__ == '__main__':
    main()
