import hashlib
my_hash1 = hashlib.md5() #Choose md5 and update with a bytes
update_bytes = b'Python123'
my_hash1.update(update_bytes)
print("Result after digesting: " + str(my_hash1.hexdigest()))
print("Digest Size: " + str(my_hash1.digest_size))

my_hash2 = hashlib.sha256() #Choose SHA256 and update with same bytes
my_hash2.update(update_bytes)
print("Result after digesting: " + str(my_hash2.hexdigest()))
print("Digest Size: " + str(my_hash2.digest_size))
