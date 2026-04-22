# Bit manipulation

Bit manipulation is the act of manipulating bits to detect errors (hamming code), encrypts and decrypts messages (more on that in the 'ciphers' folder) or just do anything at the lowest level of your computer.

* <https://en.wikipedia.org/wiki/Bit_manipulation>
* <https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations>
* <https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations>
* <https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types>
* <https://wiki.python.org/moin/BitManipulation>
* <https://wiki.python.org/moin/BitwiseOperators>
* <https://www.tutorialspoint.com/python3/bitwise_operators_example.htm>

## Example

Below is a simple example using the `get_set_bits_count_using_brian_kernighans_algorithm`
function from [bit_manipulation/count_number_of_one_bits.py](bit_manipulation/count_number_of_one_bits.py).

```python
from bit_manipulation.count_number_of_one_bits import get_set_bits_count_using_brian_kernighans_algorithm

print(get_set_bits_count_using_brian_kernighans_algorithm(25))  # 3
print(get_set_bits_count_using_brian_kernighans_algorithm(58))  # 4
```

This repository also includes doctest examples in the implementation that can be run with:

```bash
python3 bit_manipulation/count_number_of_one_bits.py
```

