"""
Context-Adaptive Binary Arithmetic Coding (CABAC) implementation.

CABAC is an entropy encoding method used in video compression standards like H.264/AVC
and H.265/HEVC. It combines arithmetic coding with adaptive context modeling to achieve
high compression efficiency.

Algorithm references:
https://en.wikipedia.org/wiki/Context-adaptive_binary_arithmetic_coding
https://en.wikipedia.org/wiki/Arithmetic_coding

Video compression standards:
https://en.wikipedia.org/wiki/Advanced_Video_Coding

Requirements: None (uses only Python standard library)
"""

from typing import List, Iterator, Tuple
import sys


class ContextAdaptiveBinaryArithmeticCoder:
    """
    Context-Adaptive Binary Arithmetic Coder (CABAC) implementation.
    
    This class implements both encoding and decoding functionality for CABAC,
    which uses adaptive probability models based on context to achieve efficient
    binary arithmetic coding.
    """
    
    def __init__(self, num_contexts: int = 256):
        """
        Initialize CABAC coder with default state.
        
        Args:
            num_contexts: Number of context models to maintain
            
        Raises:
            ValueError: If num_contexts is not positive
            
        Examples:
            >>> coder = ContextAdaptiveBinaryArithmeticCoder()
            >>> coder.num_contexts
            256
            >>> len(coder.context_probabilities)
            256
            
            >>> ContextAdaptiveBinaryArithmeticCoder(0)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ValueError: Number of contexts must be positive
        """
        if num_contexts <= 0:
            raise ValueError("Number of contexts must be positive")
            
        self.num_contexts = num_contexts
        self.reset_coder_state()
        
    def reset_coder_state(self) -> None:
        """
        Reset the coder to initial state.
        
        Examples:
            >>> coder = ContextAdaptiveBinaryArithmeticCoder()
            >>> coder.low_bound = 100
            >>> coder.reset_coder_state()
            >>> coder.low_bound
            0
        """
        self.low_bound = 0
        self.high_bound = (1 << 32) - 1
        self.context_probabilities = [0.5] * self.num_contexts
        self.code_value = 0
        
    def update_context_probability(self, context_index: int, observed_bit: int, 
                                 learning_rate: float = 0.05) -> None:
        """
        Update context probability based on observed bit value.
        
        Uses exponential moving average to adapt probability toward observed data.
        
        Args:
            context_index: Index of context to update
            observed_bit: The bit value that was observed (0 or 1)
            learning_rate: Adaptation speed (0 < learning_rate < 1)
            
        Raises:
            ValueError: If parameters are out of valid ranges
            IndexError: If context_index is invalid
            
        Examples:
            >>> coder = ContextAdaptiveBinaryArithmeticCoder(2)
            >>> coder.context_probabilities[0]
            0.5
            >>> coder.update_context_probability(0, 1)
            >>> coder.context_probabilities[0] > 0.5
            True
            
            >>> coder.update_context_probability(-1, 1)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            IndexError: Context index out of range
            
            >>> coder.update_context_probability(0, 2)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ValueError: Observed bit must be 0 or 1
        """
        if not 0 <= context_index < self.num_contexts:
            raise IndexError("Context index out of range")
        if observed_bit not in (0, 1):
            raise ValueError("Observed bit must be 0 or 1")
        if not 0 < learning_rate < 1:
            raise ValueError("Learning rate must be between 0 and 1")
            
        current_prob = self.context_probabilities[context_index]
        self.context_probabilities[context_index] = (
            (1 - learning_rate) * current_prob + learning_rate * observed_bit
        )
        
    def encode_binary_symbol(self, bit_value: int, context_index: int, 
                           output_buffer: List[int]) -> None:
        """
        Encode a single binary symbol using the specified context.
        
        Args:
            bit_value: Binary value to encode (0 or 1)
            context_index: Context index for probability model
            output_buffer: List to append output bytes to
            
        Raises:
            ValueError: If bit_value is not 0 or 1
            IndexError: If context_index is invalid
            
        Examples:
            >>> coder = ContextAdaptiveBinaryArithmeticCoder(2)
            >>> output = []
            >>> coder.encode_binary_symbol(1, 0, output)
            >>> isinstance(output, list)
            True
            
            >>> coder.encode_binary_symbol(2, 0, output)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ValueError: Bit value must be 0 or 1
        """
        if bit_value not in (0, 1):
            raise ValueError("Bit value must be 0 or 1")
        if not 0 <= context_index < self.num_contexts:
            raise IndexError("Context index out of range")
            
        probability_zero = self.context_probabilities[context_index]
        current_range = self.high_bound - self.low_bound + 1
        split_point = self.low_bound + int(current_range * probability_zero)
        
        if bit_value == 0:
            self.high_bound = split_point
        else:
            self.low_bound = split_point + 1
            
        # Renormalization: output bytes when range becomes too small
        while (self.high_bound ^ self.low_bound) < (1 << 24):
            output_buffer.append((self.high_bound >> 24) & 0xFF)
            self.low_bound = (self.low_bound << 8) & 0xFFFFFFFF
            self.high_bound = ((self.high_bound << 8) & 0xFFFFFFFF) | 0xFF
            
        self.update_context_probability(context_index, bit_value)
        
    def finalize_encoding(self, output_buffer: List[int]) -> None:
        """
        Finalize encoding by flushing remaining bits.
        
        Args:
            output_buffer: List to append final output bytes to
            
        Examples:
            >>> coder = ContextAdaptiveBinaryArithmeticCoder()
            >>> output = []
            >>> coder.finalize_encoding(output)
            >>> len(output)
            4
        """
        # Output remaining bits in low_bound
        for _ in range(4):
            output_buffer.append((self.low_bound >> 24) & 0xFF)
            self.low_bound = (self.low_bound << 8) & 0xFFFFFFFF
            
    def initialize_decoding(self, encoded_bytes: Iterator[int]) -> Iterator[int]:
        """
        Initialize decoder state from encoded byte stream.
        
        Args:
            encoded_bytes: Iterator over encoded bytes
            
        Returns:
            Iterator over remaining encoded bytes
            
        Raises:
            StopIteration: If encoded_bytes has fewer than 4 bytes
            
        Examples:
            >>> coder = ContextAdaptiveBinaryArithmeticCoder()
            >>> data = iter([1, 2, 3, 4, 5, 6])
            >>> remaining = coder.initialize_decoding(data)
            >>> list(remaining)
            [5, 6]
        """
        self.reset_coder_state()
        
        # Initialize code value from first 4 bytes
        for _ in range(4):
            try:
                next_byte = next(encoded_bytes)
                self.code_value = (self.code_value << 8) | next_byte
            except StopIteration:
                raise StopIteration("Not enough bytes to initialize decoder")
                
        return encoded_bytes
        
    def decode_binary_symbol(self, context_index: int, 
                           input_stream: Iterator[int]) -> int:
        """
        Decode a single binary symbol using the specified context.
        
        Args:
            context_index: Context index for probability model
            input_stream: Iterator over input bytes
            
        Returns:
            Decoded binary value (0 or 1)
            
        Raises:
            IndexError: If context_index is invalid
            StopIteration: If input_stream is exhausted during renormalization
            
        Examples:
            >>> coder = ContextAdaptiveBinaryArithmeticCoder(2)
            >>> # This is a complex test requiring full encode/decode cycle
            >>> output = []
            >>> coder.encode_binary_symbol(1, 0, output)
            >>> coder.finalize_encoding(output)
            >>> coder.reset_coder_state()
            >>> input_iter = coder.initialize_decoding(iter(output))
            >>> decoded = coder.decode_binary_symbol(0, input_iter)
            >>> decoded in (0, 1)
            True
        """
        if not 0 <= context_index < self.num_contexts:
            raise IndexError("Context index out of range")
            
        probability_zero = self.context_probabilities[context_index]
        current_range = self.high_bound - self.low_bound + 1
        split_point = self.low_bound + int(current_range * probability_zero)
        
        if self.code_value <= split_point:
            self.high_bound = split_point
            decoded_bit = 0
        else:
            self.low_bound = split_point + 1
            decoded_bit = 1
            
        # Renormalization: read new bytes when range becomes too small
        while (self.high_bound ^ self.low_bound) < (1 << 24):
            try:
                next_byte = next(input_stream)
                self.code_value = ((self.code_value << 8) & 0xFFFFFFFF) | next_byte
            except StopIteration:
                # Handle end of stream gracefully
                self.code_value = (self.code_value << 8) & 0xFFFFFFFF
                
            self.low_bound = (self.low_bound << 8) & 0xFFFFFFFF
            self.high_bound = ((self.high_bound << 8) & 0xFFFFFFFF) | 0xFF
            
        self.update_context_probability(context_index, decoded_bit)
        return decoded_bit


def convert_string_to_bit_sequence(input_string: str) -> List[int]:
    """
    Convert string to sequence of bits using UTF-8 encoding.
    
    Args:
        input_string: String to convert
        
    Returns:
        List of bits (0s and 1s) representing the string
        
    Raises:
        UnicodeEncodeError: If string cannot be UTF-8 encoded
        
    Examples:
        >>> bits = convert_string_to_bit_sequence("A")
        >>> len(bits)
        8
        >>> all(bit in (0, 1) for bit in bits)
        True
        
        >>> convert_string_to_bit_sequence("") 
        []
    """
    if not input_string:
        return []
        
    bit_sequence = []
    utf8_bytes = input_string.encode('utf-8')
    
    for byte_value in utf8_bytes:
        # Convert each byte to 8 bits (MSB first)
        for bit_position in range(7, -1, -1):
            bit_sequence.append((byte_value >> bit_position) & 1)
            
    return bit_sequence


def convert_bit_sequence_to_string(bit_sequence: List[int]) -> str:
    """
    Convert sequence of bits back to string using UTF-8 decoding.
    
    Args:
        bit_sequence: List of bits (0s and 1s)
        
    Returns:
        Decoded UTF-8 string
        
    Raises:
        ValueError: If bit_sequence length is not multiple of 8
        UnicodeDecodeError: If resulting bytes are not valid UTF-8
        
    Examples:
        >>> bits = convert_string_to_bit_sequence("Hello")
        >>> reconstructed = convert_bit_sequence_to_string(bits)
        >>> reconstructed
        'Hello'
        
        >>> convert_bit_sequence_to_string([1, 0, 1])  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Bit sequence length must be multiple of 8
    """
    if len(bit_sequence) % 8 != 0:
        raise ValueError("Bit sequence length must be multiple of 8")
        
    if not bit_sequence:
        return ""
        
    byte_array = bytearray()
    
    # Convert every 8 bits to a byte
    for byte_start in range(0, len(bit_sequence), 8):
        byte_value = 0
        byte_bits = bit_sequence[byte_start:byte_start + 8]
        
        for bit in byte_bits:
            if bit not in (0, 1):
                raise ValueError(f"Invalid bit value: {bit}")
            byte_value = (byte_value << 1) | bit
            
        byte_array.append(byte_value)
        
    return byte_array.decode('utf-8')


def compress_string_with_cabac(input_text: str, num_contexts: int = 256) -> Tuple[List[int], int]:
    """
    Compress a string using CABAC algorithm.
    
    Args:
        input_text: Text string to compress
        num_contexts: Number of context models to use
        
    Returns:
        Tuple of (compressed_bytes, original_bit_length)
        
    Raises:
        ValueError: If num_contexts is not positive
        
    Examples:
        >>> compressed, orig_len = compress_string_with_cabac("test")
        >>> len(compressed) > 0
        True
        >>> orig_len > 0
        True
        >>> isinstance(compressed, list)
        True
        
        >>> compress_string_with_cabac("", 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Number of contexts must be positive
    """
    if num_contexts <= 0:
        raise ValueError("Number of contexts must be positive")
        
    if not input_text:
        return [], 0
        
    # Convert string to bit sequence
    bit_sequence = convert_string_to_bit_sequence(input_text)
    
    # Initialize encoder
    encoder = ContextAdaptiveBinaryArithmeticCoder(num_contexts)
    compressed_bytes = []
    
    # Encode each bit using positional context
    for bit_position, bit_value in enumerate(bit_sequence):
        context_index = bit_position % num_contexts
        encoder.encode_binary_symbol(bit_value, context_index, compressed_bytes)
        
    # Finalize encoding
    encoder.finalize_encoding(compressed_bytes)
    
    return compressed_bytes, len(bit_sequence)


def decompress_string_with_cabac(compressed_bytes: List[int], original_bit_length: int,
                                num_contexts: int = 256) -> str:
    """
    Decompress a CABAC-compressed byte sequence back to original string.
    
    Args:
        compressed_bytes: List of compressed bytes
        original_bit_length: Length of original bit sequence
        num_contexts: Number of context models used during compression
        
    Returns:
        Decompressed string
        
    Raises:
        ValueError: If parameters are invalid
        
    Examples:
        >>> compressed, orig_len = compress_string_with_cabac("hello")
        >>> decompressed = decompress_string_with_cabac(compressed, orig_len)
        >>> decompressed
        'hello'
        
        >>> decompress_string_with_cabac([], 8)
        Traceback (most recent call last):
        StopIteration: Not enough bytes to initialize decoder
    """
    if num_contexts <= 0:
        raise ValueError("Number of contexts must be positive")
    if original_bit_length < 0:
        raise ValueError("Original bit length must be non-negative")
        
    if original_bit_length == 0:
        return ""
        
    # Initialize decoder
    decoder = ContextAdaptiveBinaryArithmeticCoder(num_contexts)
    input_stream = decoder.initialize_decoding(iter(compressed_bytes))
    
    # Decode bits using same context pattern as encoding
    decoded_bits = []
    for bit_position in range(original_bit_length):
        context_index = bit_position % num_contexts
        decoded_bit = decoder.decode_binary_symbol(context_index, input_stream)
        decoded_bits.append(decoded_bit)
        
    # Convert bits back to string
    return convert_bit_sequence_to_string(decoded_bits)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
