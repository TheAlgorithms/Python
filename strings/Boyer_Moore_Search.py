"""
This algorithm tries to find the pattern in given text using Bad Character Heuristic method. 
The bad-character rule considers the character in Text at which there is a mis-match. The next occurrence of that character to the left in Pattern is found, and a shift which brings that occurrence in line with the mismatched occurrence in Text is proposed. If the mismatched character does not occur to the left in Pattern, a shift is proposed that moves the entirety of Pattern past the point of mismatch

Complexity : O(n/m)
    n=length of main string
    m=length of pattern string
"""

class BoyerMooreSearch:
    def __init__(self, text, pattern):
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)
    
    def match_In_Pattern(self, char):

        """ finds the index of char in pattern in reverse order

        Paremeters : 
            char (chr): character to be searched
        
        Returns :
            i (int): index of char from last in pattern
            -1 (int): if char is not found in pattern 
        """ 

        for i in range(self.patLen-1, -1, -1):
            if char == self.pattern[i]:
                return i
        return -1


    def misMatch_In_Text(self, currentPos):

        """ finds the index of mis-matched character in text when compared with pattern from last

        Paremeters : 
            currentPos (int): current index position of text
        
        Returns :
            i (int): index of mismatched char from last in text
            -1 (int): if there is no mis-match between pattern and text block
        """

        for i in range(self.patLen-1, -1, -1):
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1
        
    def bad_Character_Heuristic(self):

        """ searches pattern in text and returns index positions """
        positions = []
        for i in range(self.textLen - self.patLen + 1):
            misMatch_Index = self.misMatch_In_Text(i)
            if misMatch_Index == -1:
                positions.append(i)
            else:
                match_Index = self.match_In_Pattern(self.text[misMatch_Index])
                i = misMatch_Index - match_Index   #shifting index
        return positions

 
text = "ABAABA"
pattern = "AB" 
bms = BoyerMooreSearch(text, pattern)
positions = bms.bad_Character_Heuristic()
if len(positions) == 0:
    print("No match found")
else:
    print("Pattern found in following positions: ")
    print(positions)
    

