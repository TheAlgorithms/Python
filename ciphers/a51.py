# implementing A5/1 cipher algorithm
from collections import Counter
import re

reg1_len:int = 19
reg2_len:int = 22
reg3_len:int = 23

LFSR1:list = [] # 19  -> 8
LFSR2:list = [] # 22 -> 10
LFSR3:list = [] # 23 -> 10

for _ in range(reg1_len):
    LFSR1.append(0)
for _ in range(reg2_len):
    LFSR2.append(0)
for _ in range(reg3_len):
    LFSR3.append(0)

tapped_bits_1:list = [13,16,17,18]
tapped_bits_2:list = [20,21]
tapped_bits_3:list = [7,20,21,22]

def set_register(type:int, i:int, a:str) -> None:
    """
        >>> set_register(1, 0, "0")
    """
    if (type == 1):
        # register 1
        intermediate_xor = LFSR1[tapped_bits_1[0]] ^ LFSR1[tapped_bits_1[1]] ^ LFSR1[tapped_bits_1[2]] ^ LFSR1[tapped_bits_1[3]]
        if i < 19:
            LFSR1[i] = intermediate_xor ^ int(a)

    if (type == 2):
        # register 2
        intermediate_xor = LFSR2[tapped_bits_1[0]] ^ LFSR2[tapped_bits_1[1]] 
        if i < 22:
            LFSR2[i] = intermediate_xor ^ int(a)
            
    if (type == 3):
        # register 3
        intermediate_xor =  LFSR3[tapped_bits_1[0]] ^ LFSR3[tapped_bits_1[1]] ^ LFSR3[tapped_bits_1[2]] ^ LFSR3[tapped_bits_1[3]]
        if i < 23:
            LFSR3[i] = intermediate_xor ^ int(a)

def majority(arr:list) -> int:
    """
    >>> majority([0,1,1])
    1
    """
    freq = Counter(arr)
    for (key,val) in freq.items():
        if(val > 1):
            return key

def set_register_majority(mv:int) -> None:
    """
    >>> set_register_majority(0)
    """
    if (mv == LFSR1[8]):
        intermediate_xor = LFSR1[tapped_bits_1[0]] ^ LFSR1[tapped_bits_1[1]] ^ LFSR1[tapped_bits_1[2]] ^ LFSR1[tapped_bits_1[3]]
        LFSR1.insert(0, intermediate_xor)
        LFSR1.pop()
    if (mv == LFSR2[10]):
        intermediate_xor = LFSR2[tapped_bits_1[0]] ^ LFSR2[tapped_bits_1[1]] 
        LFSR2.insert(0, intermediate_xor)
        LFSR2.pop()
    if (mv == LFSR3[10]):
        intermediate_xor = LFSR3[tapped_bits_1[0]] ^ LFSR3[tapped_bits_1[1]] ^ LFSR3[tapped_bits_1[2]] ^ LFSR3[tapped_bits_1[3]]
        LFSR3.insert(0, intermediate_xor)
        LFSR3.pop()

def main() -> None:
    """
    >>> incomming_str = "1101001000011010110001110001100100101001000000110111111010110111"
    >>> main()
    Enter a 64-bit key: 
    """
    #Example of 64-bit key: 1101001000011010110001110001100100101001000000110111111010110111
    incomming_str = str(input('Enter a 64-bit key: '))
    if ((not (len(incomming_str) == 64)) and (not (re.match("^([01])+", incomming_str)))): return 

    key = []
    cipher = []

    # 64
    for i in range(len(incomming_str)):
        set_register(1, i, incomming_str[i])
        set_register(2, i, incomming_str[i])
        set_register(3, i, incomming_str[i])


    for i in range(len(incomming_str)):
        # majority counting function
        majority_value = majority([LFSR1[8], LFSR2[10], LFSR3[10]])
        set_register_majority(majority_value)
        output:int = LFSR1[18]^LFSR2[21]^LFSR3[22]
        key.append(output)

    for i in key:
        cipher.append(key[i] ^ int(incomming_str[i]))

    print("LFSR1: ", LFSR1)
    print("LFSR2: ", LFSR2)
    print("LFSR3: ", LFSR3)
    print("KEY: ", key)
    print("Cipher: ", cipher)

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()