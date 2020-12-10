def encrypt_rail_fence(text):
    part1 = ''
    part2 = ''
    if len(text) % 2 != 0:
        text += '@'
    for letter in range(0, len(text)):
        if letter % 2 == 0:
            part1 += text[letter]
        else:
            part2 += text[letter]
    text = part1 + part2
    # print('Encrypted text:', text)
    return text


def decrypt_rail_fence(cypher):
    part1 = ''
    for letter in range(0, int(len(cypher) / 2)):
        part1 += cypher[letter] + cypher[letter + int(len(cypher) / 2)]
    # print('Decrypted test:', part1.replace('@',''))
    return part1.replace('@', '')










