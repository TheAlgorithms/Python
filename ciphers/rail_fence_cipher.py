input_string = input()
key = int(input())

string_list = [["" for _ in range(len(input_string))]for _ in range(key)]

def rail_fence_encryption(string, key):
    r, c = 0, 0 
    val = 0
    for i in range(len(input_string)):
        if r == key-1:
            val = 0
        elif r == 0:
            val = 1
        string_list[r][c] = input_string[i]
        c += 1

        if val == 1:
            r += 1
        else:
            r -= 1
    encrypted_string = ""
    for item in string_list:
        string = ''.join(item)
        encrypted_string += string
    return encrypted_string

encrypt_string = rail_fence_encryption(input_string, key)
print(encrypt_string)

