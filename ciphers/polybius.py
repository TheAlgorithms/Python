#!/usr/bin/env python3
#!/usr/bin/env python3

'''
A Polybius Square is a table that allows someone to translate letters into numbers.

https://www.braingle.com/brainteasers/codes/polybius.php
'''

import numpy as np

class PolybiusCipher():
    
    def __init__(self) -> None:
        Square = [['a','b','c','d','e'],
                  ['f','g','h','i','k'],
                  ['l','m','n','o','p'],
                  ['q','r','s','t','u'],
                  ['v','w','x','y','z']]
        self.Square = np.array(Square)
    
    def LetterToNumbers(self, Letter: str) -> tuple:
        Index1, Index2 = np.where(self.Square == Letter)
        Indexes = np.concatenate([Index1, Index2])
        return Indexes

    def NumbersToLetter(self, Index1: int, Index2: int) -> str:
        Letter = self.Square[Index1, Index2]
        return Letter
        
    def Encode(self, Message: str) -> str:
        Message = Message.lower()
        
        EncodedMessage = ''
        for LetterIndex in range(len(Message)):
            if Message[LetterIndex] != ' ':
                Numbers = self.LetterToNumbers(Message[LetterIndex])
                EncodedMessage = EncodedMessage + str(Numbers[0] + 1) + str(Numbers[1] + 1)
            elif Message[LetterIndex] == ' ':
                EncodedMessage = EncodedMessage + ' '
        
        return EncodedMessage
    
    def Decode(self, Message: str) -> str:
        Message = Message.replace(' ', '  ')
        DecodedMessage = ''
        for NumbersIndex in range(int(len(Message)/2)):
            if Message[NumbersIndex * 2] != ' ':
                Index1 = Message[NumbersIndex * 2]
                Index2 = Message[NumbersIndex * 2 + 1]
                
                Letter = self.NumbersToLetter(int(Index1) - 1, int(Index2) - 1)
                DecodedMessage = DecodedMessage + Letter
            elif Message[NumbersIndex * 2] == ' ':
                DecodedMessage = DecodedMessage + ' '
            
        return DecodedMessage

    def TestCipher(self) -> None:
        CipherTest = PolybiusCipher()

        (CipherTest.Encode('testmessage') == '4415434432154343112215')
        assert (CipherTest.Encode('test message') == '44154344 32154343112215')
        assert (CipherTest.Encode('Test Message') == '44154344 32154343112215')
        assert (CipherTest.Encode('') == '')

        assert (CipherTest.Decode('44154344 32154343112215') == 'test message')
        assert (CipherTest.Decode('4415434432154343112215') == 'testmessage')
        assert (CipherTest.Decode('') == '')
        