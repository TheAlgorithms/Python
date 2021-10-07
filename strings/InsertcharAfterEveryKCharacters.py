def insertCharacterAfterEveryKelements(inputString, k, characterToInsert):
    result = []
    for i in range(0, len(inputString), k):
        result.append(inputString[:i] + characterToInsert + inputString[i:])
    return str(result)


inputString = input('Enter the string')
k = int(input('Enter after which K element want to enter the string')) 
characterToInsert = input('Enter the character to insert in the string')

result = insertCharacterAfterEveryKelements(inputString, k, characterToInsert)
print('Resulted string is',result)