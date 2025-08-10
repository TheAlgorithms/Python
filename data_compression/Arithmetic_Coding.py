"""
Arithmetic coding compression algorithm implementation.

Arithmetic coding is a form of entropy encoding used in lossless data compression.
It encodes the entire message into a single number, representing a fraction between 0 and 1.

Algorithm reference:
https://en.wikipedia.org/wiki/Arithmetic_coding

Data compression techniques:
https://en.wikipedia.org/wiki/Data_compression

Requirements: None (uses only Python standard library)
"""

from collections import Counter
from decimal import Decimal, getcontext
from typing import Dict, Tuple, List, Union

# Set high precision for decimal calculations
getcontext().prec = 50


def calculate_symbol_probabilities(input_data: Union[str, List]) -> Dict[str, Decimal]:
    """
    Calculate probability distribution for symbols in the input data.

    Args:
        input_data: Input string or list to analyze for symbol frequencies

    Returns:
        Dictionary mapping each symbol to its probability as a Decimal

    Raises:
        ValueError: If input_data is empty
        TypeError: If input_data is not string or list

    Examples:
        >>> probs = calculate_symbol_probabilities("aab")
        >>> round(float(probs['a']), 10)
        0.6666666667
        >>> round(float(probs['b']), 10)
        0.3333333333
        >>> len(probs)
        2

        >>> calculate_symbol_probabilities("")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Input data cannot be empty

        >>> calculate_symbol_probabilities(123)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: Input data must be string or list
    """
    if not input_data:
        raise ValueError("Input data cannot be empty")
    if not isinstance(input_data, (str, list)):
        raise TypeError("Input data must be string or list")

    symbol_frequencies = Counter(input_data)
    total_symbols = len(input_data)
    
    probability_table = {}
    for symbol, frequency in symbol_frequencies.items():
        probability_table[symbol] = Decimal(frequency) / Decimal(total_symbols)
    
    return probability_table


def create_cumulative_distribution(probability_table: Dict[str, Decimal]) -> Dict[str, Decimal]:
    """
    Create cumulative distribution from probability table.

    Args:
        probability_table: Dictionary mapping symbols to their probabilities

    Returns:
        Dictionary mapping symbols to their cumulative probability positions

    Raises:
        ValueError: If probability_table is empty

    Examples:
        >>> probs = {'a': Decimal('0.6'), 'b': Decimal('0.4')}
        >>> cumulative = create_cumulative_distribution(probs)
        >>> float(cumulative['a'])
        0.0
        >>> float(cumulative['b'])
        0.6

        >>> create_cumulative_distribution({})  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Probability table cannot be empty
    """
    if not probability_table:
        raise ValueError("Probability table cannot be empty")

    sorted_symbols = sorted(probability_table.keys())
    cumulative_distribution = {}
    cumulative_sum = Decimal('0.0')
    
    for symbol in sorted_symbols:
        cumulative_distribution[symbol] = cumulative_sum
        cumulative_sum += probability_table[symbol]
    
    return cumulative_distribution


def encode_arithmetic_sequence(input_data: Union[str, List], 
                             probability_table: Dict[str, Decimal]) -> Tuple[Decimal, int]:
    """
    Encode input data using arithmetic coding algorithm.

    The algorithm works by maintaining an interval [low, high) that gets
    progressively narrowed based on the probability of each symbol.

    Args:
        input_data: Data to encode (string or list of symbols)
        probability_table: Symbol probabilities as returned by calculate_symbol_probabilities

    Returns:
        Tuple of (encoded_value, original_length) where encoded_value is the
        arithmetic representation and original_length is needed for decoding

    Raises:
        ValueError: If inputs are invalid
        KeyError: If input contains symbols not in probability table

    Examples:
        >>> probs = calculate_symbol_probabilities("aab")
        >>> encoded_val, length = encode_arithmetic_sequence("aab", probs)
        >>> length
        3
        >>> isinstance(encoded_val, Decimal)
        True

        >>> encode_arithmetic_sequence("xyz", {'a': Decimal('1.0')})  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        KeyError: Symbol 'x' not found in probability table
    """
    if not input_data:
        raise ValueError("Input data cannot be empty")
    if not probability_table:
        raise ValueError("Probability table cannot be empty")

    cumulative_distribution = create_cumulative_distribution(probability_table)
    
    # Initialize interval bounds
    low_bound = Decimal('0.0')
    high_bound = Decimal('1.0')
    
    # Process each symbol in the input
    for symbol in input_data:
        if symbol not in probability_table:
            raise KeyError(f"Symbol '{symbol}' not found in probability table")
            
        # Calculate current interval range
        current_range = high_bound - low_bound
        
        # Update interval bounds based on symbol's probability range
        symbol_cumulative_prob = cumulative_distribution[symbol]
        symbol_probability = probability_table[symbol]
        
        new_high = low_bound + current_range * (symbol_cumulative_prob + symbol_probability)
        new_low = low_bound + current_range * symbol_cumulative_prob
        
        low_bound = new_low
        high_bound = new_high
    
    # Return midpoint of final interval and original length
    encoded_value = (low_bound + high_bound) / 2
    return encoded_value, len(input_data)


def decode_arithmetic_sequence(encoded_value: Union[Decimal, float, str], 
                             original_length: int,
                             probability_table: Dict[str, Decimal]) -> str:
    """
    Decode an arithmetic-coded value back to original data.

    Args:
        encoded_value: The encoded arithmetic value
        original_length: Length of the original data sequence
        probability_table: Symbol probabilities used during encoding

    Returns:
        Decoded string matching the original input data

    Raises:
        ValueError: If inputs are invalid
        TypeError: If encoded_value cannot be converted to Decimal

    Examples:
        >>> probs = calculate_symbol_probabilities("aab")
        >>> encoded_val, length = encode_arithmetic_sequence("aab", probs)
        >>> decoded = decode_arithmetic_sequence(encoded_val, length, probs)
        >>> decoded
        'aab'

        >>> decode_arithmetic_sequence("invalid", 3, {})  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Probability table cannot be empty
    """
    if original_length <= 0:
        raise ValueError("Original length must be positive")
    if not probability_table:
        raise ValueError("Probability table cannot be empty")
    
    try:
        value = Decimal(str(encoded_value))
    except (TypeError, ValueError) as e:
        raise TypeError(f"Cannot convert encoded_value to Decimal: {e}")

    cumulative_distribution = create_cumulative_distribution(probability_table)
    sorted_symbols = sorted(probability_table.keys())
    
    decoded_sequence = []
    low_bound = Decimal('0.0')
    high_bound = Decimal('1.0')
    
    # Decode each symbol position
    for _ in range(original_length):
        current_range = high_bound - low_bound
        
        # Find which symbol's interval contains the current value
        for symbol in sorted_symbols:
            symbol_low = low_bound + current_range * cumulative_distribution[symbol]
            symbol_high = symbol_low + current_range * probability_table[symbol]
            
            if symbol_low <= value < symbol_high:
                decoded_sequence.append(symbol)
                # Update bounds to the symbol's interval
                low_bound = symbol_low
                high_bound = symbol_high
                break
    
    return ''.join(decoded_sequence)


def compress_with_arithmetic_coding(input_text: str) -> Tuple[Decimal, int, Dict[str, Decimal]]:
    """
    Complete arithmetic coding compression pipeline.

    Args:
        input_text: Text string to compress

    Returns:
        Tuple of (compressed_value, original_length, probability_table)
        All three components are needed for decompression

    Raises:
        ValueError: If input_text is empty

    Examples:
        >>> compressed_val, length, probs = compress_with_arithmetic_coding("hello")
        >>> length
        5
        >>> len(probs)  # Number of unique characters
        4
        >>> isinstance(compressed_val, Decimal)
        True

        >>> compress_with_arithmetic_coding("")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Input text cannot be empty
    """
    if not input_text:
        raise ValueError("Input text cannot be empty")
    
    probability_table = calculate_symbol_probabilities(input_text)
    compressed_value, original_length = encode_arithmetic_sequence(input_text, probability_table)
    
    return compressed_value, original_length, probability_table


def decompress_arithmetic_coding(compressed_value: Decimal, 
                               original_length: int,
                               probability_table: Dict[str, Decimal]) -> str:
    """
    Complete arithmetic coding decompression pipeline.

    Args:
        compressed_value: The arithmetic-coded value
        original_length: Length of original uncompressed data
        probability_table: Symbol probabilities from compression

    Returns:
        Decompressed text string

    Examples:
        >>> compressed_val, length, probs = compress_with_arithmetic_coding("test")
        >>> decompressed = decompress_arithmetic_coding(compressed_val, length, probs)
        >>> decompressed
        'test'
    """
    return decode_arithmetic_sequence(compressed_value, original_length, probability_table)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
