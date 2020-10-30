from passlib.context import CryptContext 
#importing cryptcontext from passlib

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

#A round is a part of the algorithm that runs many times in order to reduce "crackability".

def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

password_val=input("Enter the password :")

hashed=encrypt_password(password)
print(check_encrypted_password(password_val,hashed))
