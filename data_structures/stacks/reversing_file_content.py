from .stack import Stack

def reverse_file(file) -> None:
    ''' Reversing the data stored in a file using stack'''
    S = Stack()
    original = open(file)
    # Pushing the data to the stack
    for line in file:
        S.push(line.rstrip('\n'))
    original.close()
    
    # overwriting with reversed data
    new = open(file, 'w')
    while not S.is_empty():
        new.write(S.pop() + '\n')
    new.close()
    
if __name__ == '__main__':
    reverse_file(path_to_the_file)
