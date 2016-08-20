from RSA import load_credentials
from RSA import RSA_encrypt, RSA_decrypt, RSA_sign, RSA_check
from tools import rand_range, rand
from requests import get
from os import system

def main():
    base_url = "http://asymcryptwebservice.appspot.com/rsa/"
    key_size = 256
    key_filename = "client_key_%d.rsa" % (key_size)

    try:
        client_credentials = load_credentials(key_filename)
    except IOError:
        from RSA import generate_RSA_credentials, save_credentials
        client_credentials = generate_RSA_credentials(key_size)
        save_credentials(key_filename, client_credentials)
        pass

    client_shared_key = client_credentials["shared_key"]
    client_secret_key = client_credentials["secret_key"]
    client_n = client_shared_key["n"]
    client_e = client_shared_key["e"]

    payload = {"keySize": key_size}
    response = get(base_url+"serverKey", payload, timeout=10)
    cookies = response.cookies

    server_credentials = response.json()
    server_n = int(server_credentials["modulus"], 16)
    server_e = int(server_credentials["publicExponent"], 16)
    server_shared_key = {"n": server_n, "e": server_e}

    client_message = rand_range(1, client_n-1)
    client_cipher = RSA_encrypt(client_message, server_shared_key)

    print "Client credentials: n = %X e = %X" % (client_n, client_e)
    print "Server credentials: n = %X e = %X" % (server_n, server_e)
    print "Message (plain): %X" % (client_message)
    print "Ciphertext (client encrypt): %X" % (client_cipher)


    payload = {"message": "%X" % (client_message),
               "modulus": "%X" % (server_n),
               "publicExponent": "%X" % (server_e)}
    response = get(base_url+"encrypt", payload, cookies=cookies, timeout=10).json()
    server_cipher = response["cipherText"]

    payload = {"cipherText": "%X" % (client_cipher)}
    response = get(base_url+"decrypt", payload, cookies=cookies, timeout=10).json()
    server_decipher = response["message"]

    print "client_cipher == server_cipher:", "%X" % client_cipher == server_cipher
    print "server_decipher == client_message:", server_decipher == "%X" % client_message


    payload = {"message": "%X" % (client_message)}
    response = get(base_url+"sign", payload, cookies=cookies, timeout=10).json()
    server_signature = response["signature"]

    client_verified = RSA_check(client_message, int(server_signature, 16), server_shared_key)

    print "Server signature:", server_signature
    print "Client verified:", client_verified


    client_signature = RSA_sign(client_message, client_credentials)
    payload = {"message": "%X" % (client_message),
               "signature": "%X" % (client_signature),
               "modulus": "%X" % (client_n),
               "publicExponent": "%X" % (client_e)}
    response = get(base_url+"verify", payload, cookies=cookies, timeout=10).json()
    server_verified = response["verified"]

    print "Client signature: %X" % (client_signature)
    print "Server verified:", server_verified


    payload = {"modulus": "%X" % (client_n),
               "publicExponent": "%X" % (client_e)}
    response = get(base_url+"sendKey", payload, cookies=cookies, timeout=10).json()
    server_new_key, server_signature = response["key"], response["signature"]
    server_new_key, server_signature = int(server_new_key, 16), int(server_signature, 16)

    server_new_key = RSA_decrypt(server_new_key, client_credentials)
    server_signature = RSA_decrypt(server_signature, client_credentials)
    client_verified = RSA_check(server_new_key, server_signature, server_shared_key)

    print "Server new key:", server_new_key
    print "Client verified:", client_verified


    client_new_key_sent = rand(bit_length=64)
    client_signature = RSA_sign(client_new_key_sent, client_credentials)
    client_new_key_crypted = RSA_encrypt(client_new_key_sent, server_shared_key)
    client_signature_crypted = RSA_encrypt(client_signature, server_shared_key)

    payload = {"key": "%X" % (client_new_key_crypted),
               "signature": "%X" % (client_signature_crypted),
               "modulus": "%X" % (client_n),
               "publicExponent": "%X" % (client_e)}
    response = get(base_url+"receiveKey", payload, cookies=cookies, timeout=10).json()
    server_new_key_received, server_verified = response["key"], response["verified"]

    print "Server received new key:", server_new_key_received
    print "Server verified:", server_verified
    print "client_new_key_sent == server_new_key_received:", client_new_key_sent == int(server_new_key_received, 16)

if __name__ == '__main__':
    while 1:
        try:
            main()
            break
        except:
            system("cls")
            print "Error occured, trying one more time"
