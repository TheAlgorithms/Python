"""
Minimalist file that allows pytest to find and run the Test unittest.  For details, see:
https://doc.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery
"""

from .prime_check import Test

Test()
