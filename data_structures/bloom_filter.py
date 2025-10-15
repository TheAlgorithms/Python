"""
Bloom Filter implementation.

A Bloom filter is a space-efficient probabilistic data structure that is designed
to test whether an element is a member of a set. It can have false positives
but never false negatives.

Time Complexity:
    - Insert: O(k) where k is the number of hash functions
    - Lookup: O(k) where k is the number of hash functions
Space Complexity: O(m) where m is the size of the bit array

Reference: https://en.wikipedia.org/wiki/Bloom_filter
"""

import hashlib
import math
from typing import List, Union


class BloomFilter:
    """
    Bloom Filter implementation with configurable false positive rate.
    
    Attributes:
        bit_array: List of bits representing the filter
        hash_functions: Number of hash functions to use
        size: Size of the bit array
        count: Number of elements added to the filter
    """
    
    def __init__(self, expected_items: int, false_positive_rate: float = 0.01):
        """
        Initialize Bloom Filter.
        
        Args:
            expected_items: Expected number of items to be stored
            false_positive_rate: Desired false positive rate (0.0 to 1.0)
            
        Examples:
            >>> bf = BloomFilter(1000, 0.01)
            >>> bf.size > 0
            True
            >>> bf.hash_functions > 0
            True
        """
        self.expected_items = expected_items
        self.false_positive_rate = false_positive_rate
        
        # Calculate optimal size and number of hash functions
        self.size = self._calculate_size(expected_items, false_positive_rate)
        self.hash_functions = self._calculate_hash_functions(self.size, expected_items)
        
        # Initialize bit array
        self.bit_array = [False] * self.size
        self.count = 0
    
    def _calculate_size(self, n: int, p: float) -> int:
        """Calculate optimal size of bit array."""
        if p <= 0 or p >= 1:
            raise ValueError("False positive rate must be between 0 and 1")
        
        # m = -(n * ln(p)) / (ln(2)^2)
        size = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(math.ceil(size))
    
    def _calculate_hash_functions(self, m: int, n: int) -> int:
        """Calculate optimal number of hash functions."""
        # k = (m/n) * ln(2)
        k = (m / n) * math.log(2)
        return int(math.ceil(k))
    
    def _hash(self, item: Union[str, bytes], seed: int) -> int:
        """
        Generate hash value for an item with given seed.
        
        Args:
            item: Item to hash
            seed: Seed for hash function
            
        Returns:
            Hash value
        """
        if isinstance(item, str):
            item = item.encode('utf-8')
        
        # Use different hash algorithms for different seeds
        hash_algorithms = [
            hashlib.md5,
            hashlib.sha1,
            hashlib.sha256,
            hashlib.sha512,
            hashlib.blake2b,
            hashlib.blake2s
        ]
        
        algorithm = hash_algorithms[seed % len(hash_algorithms)]
        hash_obj = algorithm(item)
        hash_obj.update(str(seed).encode('utf-8'))
        
        return int(hash_obj.hexdigest(), 16) % self.size
    
    def add(self, item: Union[str, bytes]) -> None:
        """
        Add an item to the Bloom Filter.
        
        Args:
            item: Item to add to the filter
            
        Examples:
            >>> bf = BloomFilter(100, 0.01)
            >>> bf.add("hello")
            >>> bf.contains("hello")
            True
        """
        for i in range(self.hash_functions):
            index = self._hash(item, i)
            self.bit_array[index] = True
        
        self.count += 1
    
    def contains(self, item: Union[str, bytes]) -> bool:
        """
        Check if an item might be in the Bloom Filter.
        
        Args:
            item: Item to check
            
        Returns:
            True if item might be in the filter (no false negatives),
            False if item is definitely not in the filter
            
        Examples:
            >>> bf = BloomFilter(100, 0.01)
            >>> bf.add("hello")
            >>> bf.contains("hello")
            True
            >>> bf.contains("world")  # Might be False or True (false positive)
            False
        """
        for i in range(self.hash_functions):
            index = self._hash(item, i)
            if not self.bit_array[index]:
                return False
        
        return True
    
    def get_false_positive_rate(self) -> float:
        """
        Calculate current false positive rate.
        
        Returns:
            Current false positive rate
            
        Examples:
            >>> bf = BloomFilter(100, 0.01)
            >>> bf.add("test")
            >>> rate = bf.get_false_positive_rate()
            >>> 0 <= rate <= 1
            True
        """
        if self.count == 0:
            return 0.0
        
        # (1 - e^(-k*n/m))^k
        k = self.hash_functions
        n = self.count
        m = self.size
        
        return (1 - math.exp(-k * n / m)) ** k
    
    def get_load_factor(self) -> float:
        """
        Get current load factor of the filter.
        
        Returns:
            Load factor (number of items / expected items)
            
        Examples:
            >>> bf = BloomFilter(100, 0.01)
            >>> bf.add("test")
            >>> bf.get_load_factor() > 0
            True
        """
        return self.count / self.expected_items
    
    def clear(self) -> None:
        """Clear all items from the Bloom Filter."""
        self.bit_array = [False] * self.size
        self.count = 0
    
    def __len__(self) -> int:
        """Return the number of items added to the filter."""
        return self.count
    
    def __contains__(self, item: Union[str, bytes]) -> bool:
        """Support 'in' operator."""
        return self.contains(item)
    
    def __repr__(self) -> str:
        """String representation of the Bloom Filter."""
        return (f"BloomFilter(size={self.size}, hash_functions={self.hash_functions}, "
                f"items={self.count}, load_factor={self.get_load_factor():.3f})")


class CountingBloomFilter:
    """
    Counting Bloom Filter that supports deletion.
    
    Uses counters instead of bits to allow for element removal.
    """
    
    def __init__(self, expected_items: int, false_positive_rate: float = 0.01):
        """
        Initialize Counting Bloom Filter.
        
        Args:
            expected_items: Expected number of items to be stored
            false_positive_rate: Desired false positive rate (0.0 to 1.0)
        """
        self.expected_items = expected_items
        self.false_positive_rate = false_positive_rate
        
        # Calculate optimal size and number of hash functions
        self.size = self._calculate_size(expected_items, false_positive_rate)
        self.hash_functions = self._calculate_hash_functions(self.size, expected_items)
        
        # Initialize counter array
        self.counters = [0] * self.size
        self.count = 0
    
    def _calculate_size(self, n: int, p: float) -> int:
        """Calculate optimal size of counter array."""
        if p <= 0 or p >= 1:
            raise ValueError("False positive rate must be between 0 and 1")
        
        size = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(math.ceil(size))
    
    def _calculate_hash_functions(self, m: int, n: int) -> int:
        """Calculate optimal number of hash functions."""
        k = (m / n) * math.log(2)
        return int(math.ceil(k))
    
    def _hash(self, item: Union[str, bytes], seed: int) -> int:
        """Generate hash value for an item with given seed."""
        if isinstance(item, str):
            item = item.encode('utf-8')
        
        hash_algorithms = [
            hashlib.md5,
            hashlib.sha1,
            hashlib.sha256,
            hashlib.sha512,
            hashlib.blake2b,
            hashlib.blake2s
        ]
        
        algorithm = hash_algorithms[seed % len(hash_algorithms)]
        hash_obj = algorithm(item)
        hash_obj.update(str(seed).encode('utf-8'))
        
        return int(hash_obj.hexdigest(), 16) % self.size
    
    def add(self, item: Union[str, bytes]) -> None:
        """Add an item to the Counting Bloom Filter."""
        for i in range(self.hash_functions):
            index = self._hash(item, i)
            self.counters[index] += 1
        
        self.count += 1
    
    def remove(self, item: Union[str, bytes]) -> bool:
        """
        Remove an item from the Counting Bloom Filter.
        
        Args:
            item: Item to remove
            
        Returns:
            True if item was removed, False if item was not in the filter
        """
        if not self.contains(item):
            return False
        
        for i in range(self.hash_functions):
            index = self._hash(item, i)
            self.counters[index] -= 1
        
        self.count -= 1
        return True
    
    def contains(self, item: Union[str, bytes]) -> bool:
        """Check if an item might be in the Counting Bloom Filter."""
        for i in range(self.hash_functions):
            index = self._hash(item, i)
            if self.counters[index] == 0:
                return False
        
        return True


if __name__ == "__main__":
    # Example usage
    print("Bloom Filter Example")
    print("=" * 50)
    
    # Create Bloom Filter
    bf = BloomFilter(expected_items=1000, false_positive_rate=0.01)
    
    # Add some items
    items_to_add = ["apple", "banana", "cherry", "date", "elderberry"]
    for item in items_to_add:
        bf.add(item)
        print(f"Added: {item}")
    
    print(f"\nBloom Filter Info:")
    print(f"Size: {bf.size}")
    print(f"Hash Functions: {bf.hash_functions}")
    print(f"Items Added: {len(bf)}")
    print(f"Load Factor: {bf.get_load_factor():.3f}")
    print(f"False Positive Rate: {bf.get_false_positive_rate():.3f}")
    
    # Test contains
    test_items = ["apple", "banana", "grape", "kiwi", "mango"]
    print(f"\nTesting items:")
    for item in test_items:
        result = bf.contains(item)
        print(f"'{item}': {'Found' if result else 'Not found'}")
    
    # Counting Bloom Filter example
    print(f"\nCounting Bloom Filter Example")
    print("=" * 50)
    
    cbf = CountingBloomFilter(expected_items=100, false_positive_rate=0.05)
    
    # Add items
    for item in ["test1", "test2", "test3"]:
        cbf.add(item)
        print(f"Added: {item}")
    
    # Test removal
    print(f"\nRemoving 'test2': {cbf.remove('test2')}")
    print(f"Contains 'test2': {cbf.contains('test2')}")
    print(f"Contains 'test1': {cbf.contains('test1')}")
    
    print(f"\nCounting Bloom Filter Info:")
    print(f"Items: {len(cbf)}")
    print(f"Load Factor: {cbf.get_load_factor():.3f}")
