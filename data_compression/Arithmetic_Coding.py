from collections_extended import bag
from decimal import Decimal, getcontext

# Set high precision for decimal calculations
getcontext().prec = 50

def build_probability_table(data):
    """Returns a dictionary int the form (symbol: probability)"""
    freq = bag(data) # A bag is like a multiset
    return {char: Decimal(freq.count(char)) / Decimal(len(data)) for char in set(freq)}

def arithmetic_encode(data, prob_table):
    """Preforms arithmetic coding compression"""
    symbols = sorted(prob_table.keys())
    cumulative = {}
    cumulative_sum = Decimal('0.0')
    for sym in symbols:
        cumulative[sym] = cumulative_sum
        cumulative_sum += prob_table[sym]

    low, high = Decimal('0.0'), Decimal('1.0')
    for symbol in data:
        range_ = high - low
        high   = low  + range_ * (cumulative[symbol] + prob_table[symbol])
        low    = low  + range_ *  cumulative[symbol]

    return (low + high) / 2, len(data)

def arithmetic_decode(encoded_value, length, prob_table):
    """Decodes an arithmetic-coded value"""
    symbols = sorted(prob_table.keys())
    cumulative = {}
    cumulative_sum = Decimal('0.0')
    for sym in symbols:
        cumulative[sym] = cumulative_sum
        cumulative_sum += prob_table[sym]

    result = []
    low, high = Decimal('0.0'), Decimal('1.0')
    value = Decimal(str(encoded_value))

    for _ in range(length):
        range_ = high - low
        for sym in symbols:
            sym_low  =     low + range_ * cumulative[sym]
            sym_high = sym_low + range_ * prob_table[sym]
            if sym_low <= value < sym_high:
                result.append(sym)
                low, high = sym_low, sym_high
                break

    return ''.join(result)

if __name__ == "__main__":
    text = "this is text used for testing"
    print(f"Original: {text}")

    prob_table = build_probability_table(text)
    encoded_value, length = arithmetic_encode(text, prob_table)
    print(f"Encoded value: {encoded_value}")

    decoded_text = arithmetic_decode(encoded_value, length, prob_table)
    print(f"Decoded: {decoded_text}")
    
    # Show compression ratio
    import sys
    original_size = sys.getsizeof(text)
    encoded_size = sys.getsizeof(str(encoded_value))
    print(f"Compression ratio: {original_size / encoded_size:.2f}")
