# Hashes

Hashing is the process of mapping any amount of data to a fixed-size value using a mathematical algorithm. The result is called a **hash value**, **hash code**, **hash sum**, or **hash digest**.  

Hashing is a **one-way function**, whereas encryption is a **two-way function**. While it is theoretically possible to recover the original data from a hash, the computational effort required makes it impractical. In other words, hashing is a one-way street.  

Unlike encryption, which is designed to protect data in transit, hashing is used to verify data integrity — to ensure that a file or piece of data has not been altered. In this sense, it functions as a **checksum**.

---

## Common Hashing Algorithms

### MD5
MD5 is a hashing algorithm developed by **Ronald Rivest** in 1992 as the successor to MD4. It was once widely used but is now considered cryptographically broken due to discovered vulnerabilities. Although **MD6** was later proposed, Rivest withdrew it from NIST's SHA-3 competition in 2009.

---

### SHA
**SHA** stands for **Secure Hash Algorithm**. It is best known as the hashing algorithm family used in many SSL/TLS cipher suites. A **cipher suite** is a collection of algorithms used to secure SSL/TLS connections, and SHA handles the hashing part.  
**SHA-1** is now deprecated, while **SHA-2** (and its variants like SHA-256, SHA-384, and SHA-512) is currently recommended and widely used.

---

### SHA-256
**SHA-256** is a member of the **SHA-2** algorithm family, where “256” refers to the number of bits in the resulting hash digest. It was developed by the **NSA** and published by **NIST** in 2001 as a successor to SHA-1, which had shown vulnerabilities to **collision attacks**.  
Regardless of the input size, SHA-256 always produces a 256-bit hash value, making it highly consistent and secure for modern cryptographic applications.

---

### Luhn
The **Luhn algorithm**, also known as the **Modulus 10** or **mod 10** algorithm, is a simple checksum formula used to validate identification numbers such as credit card numbers, IMEI numbers, and national identification numbers.  
It was developed by **Hans Peter Luhn**, an IBM scientist, in **1954**. The algorithm is publicly available and widely used to detect accidental errors, such as mistyped digits, rather than to provide cryptographic security.

---

