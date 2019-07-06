import os

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # if entry == listOfFile[len(listOfFile)-1]:
        #     continue
        if entry=='.git':
            continue
        # Create full path
        fullPath = os.path.join(dirName, entry)
        entryName = entry.split('_')
        # print(entryName)
        ffname = ''
        try:
            for word in entryName:
                temp = word[0].upper() + word[1:]
                ffname = ffname + ' ' + temp
                # print(temp)
            final_fn = ffname.replace('.py', '')
            final_fn = final_fn.strip()
            print('* ['+final_fn+']('+fullPath+')')
                # pass    
        except:
            pass
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            print ('\n## '+entry)
            filesInCurrDir = getListOfFiles(fullPath)
            for file in filesInCurrDir:
                fileName = file.split('/')
                fileName = fileName[len(fileName)-1]

                # print (fileName)
            allFiles = allFiles + filesInCurrDir
        else:
            allFiles.append(fullPath)
                
    return allFiles


dirName = './';
 
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)
# print (listOfFiles)