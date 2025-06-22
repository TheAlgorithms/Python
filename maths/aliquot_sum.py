def aliquot_sum(
    input_num: int, return_factors: bool = False
) -> int | tuple[int, list[int]]:
    """
    Calculates the aliquot sum of a positive integer. The aliquot sum is defined as
    the sum of all proper divisors of a number (all divisors except the number itself).
    
    This implementation uses an optimized O(sqrt(n)) algorithm for efficiency.
    
    Args:
        input_num: Positive integer to calculate aliquot sum for
        return_factors: If True, returns tuple (aliquot_sum, sorted_factor_list)
    
    Returns:
        Aliquot sum if return_factors=False
        Tuple (aliquot_sum, sorted_factor_list) if return_factors=True
    
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is not positive
        
    Examples:
        >>> aliquot_sum(15)
        9
        >>> aliquot_sum(15, True)
        (9, [1, 3, 5])
        >>> aliquot_sum(1)
        0
    """
    # Validate input type - must be integer
    if not isinstance(input_num, int):
        raise TypeError("Input must be an integer")
    
    # Validate input value - must be positive
    if input_num <= 0:
        raise ValueError("Input must be positive integer")
    
    # Special case: 1 has no proper divisors
    if input_num == 1:
        # Return empty factor list if requested
        return (0, []) if return_factors else 0
    
    # Initialize factors list with 1 (always a divisor)
    factors = [1]  
    total = 1  # Start sum with 1
    
    # Calculate square root as optimization boundary
    sqrt_num = int(input_num**0.5)
    
    # Iterate potential divisors from 2 to square root
    for divisor in range(2, sqrt_num + 1):
        # Check if divisor is a factor
        if input_num % divisor == 0:
            # Add divisor to factors list
            factors.append(divisor)
            total += divisor
            
            # Calculate complement (pair factor)
            complement = input_num // divisor
            
            # Avoid duplicate for perfect squares
            if complement != divisor:  
                factors.append(complement)
                total += complement
    
    # Sort factors for consistent output
    factors.sort()
    
    # Return based on return_factors flag
    return (total, factors) if return_factors else total


def classify_number(n: int) -> str:
    """
    Classifies a number based on its aliquot sum:
    - Perfect: aliquot sum = number
    - Abundant: aliquot sum > number
    - Deficient: aliquot sum < number
    
    Args:
        n: Positive integer to classify
        
    Returns:
        Classification string ("Perfect", "Abundant", or "Deficient")
        
    Raises:
        ValueError: If input is not positive
        
    Examples:
        >>> classify_number(6)
        'Perfect'
        >>> classify_number(12)
        'Abundant'
        >>> classify_number(19)
        'Deficient'
    """
    # Validate input
    if n <= 0:
        raise ValueError("Input must be positive integer")
    
    # Special case: 1 is always deficient
    if n == 1:
        return "Deficient"
    
    # Calculate aliquot sum (must be int only)
    s = aliquot_sum(n)  # type: ignore[assignment]
    
    # Determine classification
    if s == n:
        return "Perfect"
    return "Abundant" if s > n else "Deficient"


if __name__ == "__main__":
    import doctest
    
    # Run embedded doctests for verification
    doctest.testmod()
    
    # Additional demonstration examples
    print("Aliquot sum of 28:", aliquot_sum(28))  # Perfect number
    
    # Handle tuple return type safely
    result = aliquot_sum(28, True)
    if isinstance(result, tuple):
        print("Factors of 28:", result[1])
    
    print("Classification of 28:", classify_number(28))
    
    # Large number performance test (catch specific errors)
    try:
        print("\nCalculating aliquot sum for 10^9...")
        print("Result:", aliquot_sum(10**9))  # 1497558336
    except (TypeError, ValueError) as e:
        print(f"Input error: {e}")
    except MemoryError:
        print("Memory error: Number too large")
    except OverflowError:
        print("Overflow error: Calculation too large")
