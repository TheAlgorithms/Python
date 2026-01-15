# Boolean Algebra

Boolean algebra is used to do arithmetic with bits of values True (1) or False (0).
There are three basic operations: 'and', 'or' and 'not'.
Special or derived operations are : 'NAND', 'NOR', 'XOR' and 'XNOR'

AND :
The AND operation in Boolean algebra gives a result of 1 (True) only when all the input variables are 1 (True).
If any input is 0 (False), the output will be 0 (False).

Symbol: · or ∧
Example: If A = “I study” and B = “I sleep early”,
then A AND B means “I study and I sleep early”.
------------------------------
    |INPUT A  | INPUT B | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    0   |
    |    1    |    0    |    0   |
    |    1    |    1    |    1   |
    ------------------------------

OR :
The OR operation gives a result of 1 (True) when at least one of the input variables is 1 (True).
It gives 0 (False) only when all inputs are 0 (False).

Symbol: + or ∨
Example : If A = “I study” and B = “I sleep early”,
then A OR B means “I study or I sleep early”.

 ------------------------------
    | INPUT A | INPUT B | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    1   |
    ------------------------------

NOT:
The NOT operation is a unary operation (works on one variable).
It inverts the value of the variable —
if the input is 1 (True), the output becomes 0 (False), and vice versa.

Symbol: Overline ( ̅ ), ¬, or !
Example : If A = “It’s raining”, then NOT A means “It’s not raining”.

 ------------------------------
    |    A    |    A̅    |
    ------------------------------
    |    0    |    1    |
    |    1    |    0    |
    ------------------------------

NAND:
The NAND operation is the inverse of the AND operation.
It gives an output of 0 (False) only when all inputs are 1 (True).
For all other combinations, the output is 1 (True).

Symbol: (A · B)̅ or ¬(A ∧ B)
Example:
If A = “I study” and B = “I sleep early”,
then A NAND B means “It’s not true that I study and sleep early both.”


------------------------------
    | INPUT A | INPUT B | Output |
    ------------------------------
    |    0    |    0    |    1   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    0   |
    ------------------------------

NOR:
The NOR operation is the inverse of the OR operation.
It gives an output of 1 (True) only when all inputs are 0 (False).
If any input is 1 (True), the output becomes 0.

Symbol: (A + B)̅ or ¬(A ∨ B)
Example : If A = “I study” and B = “I sleep early”,
then A NOR B means “Neither I study nor I sleep early.”

------------------------------
    | INPUT A | INPUT B | Output |
    ------------------------------
    |    0    |    0    |    1   |
    |    0    |    1    |    0   |
    |    1    |    0    |    0   |
    |    1    |    1    |    0   |
    ------------------------------

XOR:
The XOR (Exclusive OR) operation gives an output of 1 (True) only when exactly one of the inputs is 1 (True).
If both inputs are the same (both 0 or both 1), the output is 0 (False).

Symbol: ⊕ or A XOR B
Example:
If A = “I study” and B = “I sleep early”,
then A XOR B means “I study or I sleep early, but not both.”

------------------------------
    | INPUT A | INPUT B | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    0   |
    ------------------------------

XNOR:
The XNOR (Exclusive NOR) operation is the inverse of the XOR operation.
It gives an output of 1 (True) when both inputs are the same — either both 0 or both 1.
If the inputs are different, the output is 0 (False).

Symbol: ⊙ or (A ⊕ B)̅ or A XNOR B
Example: If A = “I study” and B = “I sleep early”,
then A XNOR B means “Either I study and sleep early both, or neither I study nor sleep early.”
------------------------------
    | INPUT A | INPUT B | Output |
    ------------------------------
    |    0    |    0    |    1   |
    |    0    |    1    |    0   |
    |    1    |    0    |    0   |
    |    1    |    1    |    1   |
    ------------------------------

* <https://en.wikipedia.org/wiki/Boolean_algebra>
* <https://plato.stanford.edu/entries/boolalg-math/>
