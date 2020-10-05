# -*- coding: utf-8 -*-
#Author-Slayking1965
#email-kingslayer8509@gmail.com

def SOUNDEX(TERM: str):


    # Step 0: Covert the TERM to UpperCase
    TERM = TERM.upper()
    TERM_LETTERS = [char for char in TERM if char.isalpha()]

    #List the Remove occurrences of A, E, I, O, U, Y, H, W.
    Remove_List = ('A', 'E', 'I', 'O', 'U', 'Y', 'H', 'W')
    # Save the first letter
    first_letter = TERM_LETTERS[0]
    #Take the Other letters instead of First_Letter
    Characters = TERM_LETTERS[1:]
    #Remove items from Character using Remove_List
    Characters = [To_Characters for To_Characters in Characters if To_Characters not in Remove_List]

    #if len(Characters) == 0:
    #    return first_letter + "000"

    #Replace all the Characters with Numeric Values (instead of the first letter) with digits according to Soundex Algorythem Ruels
    Replace_List = {('B', 'F', 'P', 'V'): 1,
                  ('C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'): 2,
                  ('D', 'T'): 3,
                  ('L'): 4,
                  ('M', 'N'): 5,
                  ('R'): 6}
    Characters = [value if char else char
               for char in Characters
               for group,value in Replace_List.items()
               if char in group]

    # Step 3: Replace all adjacent same number with one number
    Characters = [char for Letter_Count, char in enumerate(Characters)
             if (Letter_Count == len(Characters) - 1 or
                (Letter_Count+1 < len(Characters) and
                 char != Characters[Letter_Count+1]))]

    #If the saved Characters’s Number is the same the resulting First Letter,keep the First Letter AND remove the Number
    if len(TERM_LETTERS)!=1:
        if first_letter == TERM_LETTERS[1]:
            Characters[0] = TERM[0]
        else:
            Characters.insert(0, first_letter)

    #If the Number of Characters are less than 4 insert 3 zeros to Characters
    # Remove all except first letter and 3 digits after it.
    #first_letter = Characters[0]
    #Characters = Characters[1:]

    #Characters = [char for char in Characters if isinstance(char, int)][0:3]
    while len(Characters) < 4:
        Characters.append(0)
    if len(Characters) > 4:
        Characters=Characters[0:4]

    INDEX = "".join([str(C) for C in Characters])
    return INDEX
