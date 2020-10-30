
"""
Will convert the entire string to lowecase letters

>>> lower("wow")
'wow'
>>> lower("HellZo")
'hellzo'
>>> lower("WHAT")
'what'
>>> lower("wh[]32")
'wh[]32'
>>> lower("whAT")
'what'
"""

# converting to ascii value int value and checking to see if char is a capital
# letter if it is a capital letter it is getting shift by 32 which makes it a lower
# case letter
 
def lower(word):
    return word.lower()

word = input()
print(lower(word))
    
