from typing import List

class RC4:
    def __init__(self, key: bytes):
        self.key=key
        self.s=self._ksa(key)

    def _ksa(self, key: bytes) -> List[int]:
        """Key Scheduling Algorithm (KSA)"""
        key_length=len(key)
        s=list(range(256))  
        j=0
        for i in range(256):
            j=(j+s[i]+key[i%key_length])%256
            s[i],s[j]=s[j],s[i]  
        return s

    def _prga(self) -> int:
        """Pseudo-Random Generation Algorithm (PRGA)"""
        i=0
        j=0
        while True:
            i=(i+1)%256
            j=(j+self.s[i])%256
            self.s[i],self.s[j]=self.s[j],self.s[i]  
            yield self.s[(self.s[i]+self.s[j])%256]  

    def _reset_state(self):
        """Reset state for each encryption/decryption."""
        self.s=self._ksa(self.key)

    def encrypt(self,plaintext:bytes)->bytes:
        """Encrypt plaintext using RC4"""
        self._reset_state()  
        prga=self._prga()
        return bytes([p^next(prga) for p in plaintext])

    def decrypt(self,ciphertext:bytes)->bytes:
        """Decrypt ciphertext using RC4 (Same as encryption)"""
        return self.encrypt(ciphertext)  


if __name__ == "__main__":
    key=b"SecretKey"
    rc4=RC4(key)
    
    plaintext=b"Hello, RC4 Cipher!"
    print("Original:",plaintext)
    
    ciphertext=rc4.encrypt(plaintext)
    print("Encrypted:",ciphertext)
    
    decrypted_text=rc4.decrypt(ciphertext)
    print("Decrypted:",decrypted_text)

    assert plaintext==decrypted_text, "Decryption failed"
    print("Encryption and decryption successful.")
