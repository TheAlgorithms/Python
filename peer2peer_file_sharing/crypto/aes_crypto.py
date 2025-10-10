import zlib
from cryptography.fernet import Fernet

SKIP_COMPRESSION_EXTENSIONS = {
    '.zip', '.gz', '.bz2', '.xz', '.rar', '.7z',
    '.jpg', '.jpeg', '.png', '.gif', '.webp',
    '.mp3', '.mp4', '.avi', '.mkv', '.mov',
    '.pdf'
}

def generate_aes_key():
    return Fernet.generate_key()

def encrypt_chunk_with_aes(chunk: bytes, aes_key: bytes, file_extension: str) -> bytes:
    fernet = Fernet(aes_key)
    if file_extension.lower() not in SKIP_COMPRESSION_EXTENSIONS:
        try:
            chunk = zlib.compress(chunk)
        except Exception as e:
            print(f"\n[!] Compression failed: {e}")
            
    return fernet.encrypt(chunk)

def decrypt_chunk_with_aes(chunk: bytes, aes_key: bytes, file_extension: str) -> bytes:
    fernet = Fernet(aes_key)
    try:
        decrypted_data = fernet.decrypt(chunk)
    except Exception as e:
        raise Exception(f"\n[!] AES decryption failed: {e}")

    if file_extension.lower() not in SKIP_COMPRESSION_EXTENSIONS:
        try:
            decrypted_data = zlib.decompress(decrypted_data)
        except zlib.error:
            print("\n[!] Warning: Failed to decompress — file may not be compressed")

    return decrypted_data