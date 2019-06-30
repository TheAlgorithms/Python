def multiplicative_inverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def convert_list_to_string(l):
    l = map(str, l)
    string = ""

    return string.join(l)
p,q=11,13
#p, q = map(int, input("Enter p and q: ").split())

n = p*q
phi_n = (p-1)*(q-1)

e = 0
for i in range(3, p+1):
    if phi_n % i is not 0:
        e = i
        break

d = multiplicative_inverse(e, phi_n)

#print("n: {} \nphi(n): {} \ne: {} \nd: {}".format(n, phi_n, e, d))

#put your plaintext here
plain_text="iamthebest"
# plain_text = input("Enter the plain text: ")

pt_list = []
ct_list = []

# ENCRYPTION
print("----------------------ENCRYPTION---------------------")
for i, t in enumerate(plain_text):
        a = ord(t)
        a %= 97
        pt_list.append(a)
        ct_list.append((a**e) % n)

pt_string = convert_list_to_string(pt_list)
ct_string = convert_list_to_string(ct_list)
print("Plain Text in numbers: ", pt_string)
print("Cipher Text in numbers: ", ct_string)

# DECRYPTION
print("----------------------DECRYPTION---------------------")
pt_list_decrypt = []
pt_decrypted = ""
for t in ct_list:
        pt = (t**d) % n
        pt_list_decrypt.append(pt)
        pt_decrypted += chr(pt + 97)

pt_list_decrypt_string = convert_list_to_string(pt_list_decrypt)
print("Decrypted Plain Text in numbers: ", pt_list_decrypt_string)
print("Decrypted Plain Text: ", pt_decrypted)
