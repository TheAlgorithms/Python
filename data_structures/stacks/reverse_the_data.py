from .stack import Stack

def reverse_text(text: str) -> str:
    ''' Reversing the data stored in a file using stack'''
    reversed_text: list[str] = []
    S = Stack()
    for char in text:
        S.push(char)
    # overwriting with reversed data
    while not S.is_empty():
        reversed_text.append(S.pop())

    return ''.join(reversed_text)
    
if __name__ == '__main__':
    
    examples = ['Hello world', 'TENET', 'Jupyter', 'Python']
    for test in examples:
        print(f'Original:{test} -> Reversed: {reverse_text(test)}')