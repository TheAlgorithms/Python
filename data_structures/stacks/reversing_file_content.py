from .stack import Stack

def reverse_file(file):
    ''' Reversing the data stored in a file using stack'''
    S = Stack()
    original = open(file)
    for line in file:
        S.push(line.rstrip('\n'))
    original.close()
    
    # overwriting with reversed data
    new = open(file, 'w')
    while not S.is_empty():
        new.write(S.pop() + '\n')
    new.close()
    

reverse_file(path)