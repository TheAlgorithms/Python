# Hashes
Hashing is the process of mapping any amount of data to a specified size using an algorithm. This is known as a hash value (or, if you're feeling fancy, a hash code, hash sums, or even a hash digest). Hashing is a one-way function, whereas encryption is a two-way function. While it is functionally conceivable to reverse-hash stuff, the required computing power makes it impractical. Hashing is a one-way street.
Unlike encryption, which is intended to protect data in transit, hashing is intended to authenticate that a file or piece of data has not been altered—that it is authentic. In other words, it functions as a checksum.

## Common hashing algorithms
### MD5
This is one of the first algorithms that has gained widespread acceptance. MD5 is hashing algorithm made by Ray Rivest that is known to suffer vulnerabilities. It was created in 1992 as the successor to MD4. Currently MD6 is in the works, but as of 2009 Rivest had removed it from NIST consideration for SHA-3.

### SHA
SHA stands for Security Hashing Algorithm and it’s probably best known as the hashing algorithm used in most SSL/TLS cipher suites. A cipher suite is a collection of ciphers and algorithms that are used for SSL/TLS connections. SHA handles the hashing aspects. SHA-1, as we mentioned earlier, is now deprecated. SHA-2 is now mandatory. SHA-2 is sometimes known has SHA-256, though variants with longer bit lengths are also available.

### SHA256
SHA 256 is a member of the SHA 2 algorithm family, under which SHA stands for Secure Hash Algorithm. It was a collaborative effort between both the NSA and NIST to implement a successor to the SHA 1 family, which was beginning to lose potency against brute force attacks. It was published in 2001.
The importance of the 256 in the name refers to the final hash digest value, i.e. the hash value will remain 256 bits regardless of the size of the plaintext/cleartext. Other algorithms in the SHA family are similar to SHA 256 in some ways.

### Luhn
The Luhn algorithm, also renowned as the modulus 10 or mod 10 algorithm, is a straightforward checksum formula used to validate a wide range of identification numbers, including credit card numbers, IMEI numbers, and Canadian Social Insurance Numbers. A community of mathematicians developed the LUHN formula in the late 1960s. Companies offering credit cards quickly followed suit. Since the algorithm is in the public interest, anyone can use it. The algorithm is used by most credit cards and many government identification numbers as a simple method of differentiating valid figures from mistyped or otherwise incorrect numbers. It was created to guard against unintentional errors, not malicious attacks.