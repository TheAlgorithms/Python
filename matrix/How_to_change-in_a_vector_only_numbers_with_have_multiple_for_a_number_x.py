
# How to change in a vector only numbers with have multiple for a number x

#HOW
'''
You need create a function that check if an element X in a vector(list) is divisible for another number Y
'''

def change_multiple(change_to,multiple,vector):
    for i in range(len(vector)): # scroll through the list
        if vector[i]%multiple == 0: #check if the mod of element vector[position] with  multiple  is 0 or not
            vector[i] = change_to # if 0 is multiple, change the number
        
'''

 *One exemple for test*
'''
vector = [4,5,6,7,9,10]
multiple = 2
change_to = 999
print(vector) # >> [4,5,6,7,9,10]
change_multiple(change_to,multiple,vector)
print(vector) # >> [999,5,999,7,9,999]
