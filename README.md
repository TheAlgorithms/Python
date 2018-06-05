# The Algorithms - Python <!-- [![Build Status](https://travis-ci.org/TheAlgorithms/Python.svg)](https://travis-ci.org/TheAlgorithms/Python) -->

### All algorithms implemented in Python (for education)

- [Sorting](sorts)

## Search Algorithms

### Linear
![alt text][linear-image]

From [Wikipedia][linear-wiki]: linear search or sequential search is a method for finding a target value within a list. It sequentially checks each element of the list for the target value until a match is found or until all the elements have been searched.
  Linear search runs in at worst linear time and makes at most n comparisons, where n is the length of the list.

__Properties__
* Worst case performance	O(n)
* Best case performance	O(1)
* Average case performance	O(n)
* Worst case space complexity	O(1) iterative

### Binary
![alt text][binary-image]

From [Wikipedia][binary-wiki]: Binary search, also known as half-interval search or logarithmic search, is a search algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful.

__Properties__
* Worst case performance	O(log n)
* Best case performance	O(1)
* Average case performance	O(log n)
* Worst case space complexity	O(1) 

----------------------------------------------------------------------------------------------------------------------

## Ciphers

### Caesar
![alt text][caesar]<br>
In cryptography, a **Caesar cipher**, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.<br>
It is **a type of substitution cipher** in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. <br>
The method is named after **Julius Caesar**, who used it in his private correspondence.<br>
The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communication security.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)

### Vigenère
The **Vigenère cipher** is a method of encrypting alphabetic text by using a series of **interwoven Caesar ciphers** based on the letters of a keyword. It is **a form of polyalphabetic substitution**.<br>
The Vigenère cipher has been reinvented many times. The method was originally described by Giovan Battista Bellaso in his 1553 book La cifra del. Sig. Giovan Battista Bellaso; however, the scheme was later misattributed to Blaise de Vigenère in the 19th century, and is now widely known as the "Vigenère cipher".<br>
Though the cipher is easy to understand and implement, for three centuries it resisted all attempts to break it; this earned it the description **le chiffre indéchiffrable**(French for 'the indecipherable cipher'). 
Many people have tried to implement encryption schemes that are essentially Vigenère ciphers. Friedrich Kasiski was the first to publish a general method of deciphering a Vigenère cipher in 1863.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

### Transposition
In cryptography, a **transposition cipher** is a method of encryption by which the positions held by units of plaintext (which are commonly characters or groups of characters) are shifted according to a regular system, so that the ciphertext constitutes a permutation of the plaintext. That is, the order of the units is changed (the plaintext is reordered).<br> 
Mathematically a bijective function is used on the characters' positions to encrypt and an inverse function to decrypt.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Transposition_cipher)


[linear-wiki]: https://en.wikipedia.org/wiki/Linear_search
[linear-image]: http://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif

[binary-wiki]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[binary-image]: https://upload.wikimedia.org/wikipedia/commons/f/f7/Binary_search_into_array.png


[caesar]: https://upload.wikimedia.org/wikipedia/commons/4/4a/Caesar_cipher_left_shift_of_3.svg
