text = input( 'write a sample text: \n')
op = int(input( ' do you want to catch a bin from a text(1) or catch a text from a bin(2)?\n'))
def text2bits(text, encoding='utf-8', errors='surrogatepass'):
    b = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return b.zfill(8 * ((len(b) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
if op == 1:
    print("===============\n ascii to bin\n ==============\n") 
    print(text2bits(text))
elif op == 2:
    bits= str(input('write a bit sequence that you want to convert\n'))
    print(text_from_bits(bits))
