import slash
import fibonacci

default_fib = [0, 1, 1, 2, 3, 5, 8]


@slash.tag('fibonacci')
@slash.parametrize(('n', 'seq'), [(2, [0, 1]), (3, [0, 1, 1]), (9, [0, 1, 1, 2, 3, 5, 8, 13, 21])])
def test_different_sequence_lengths(n, seq):
    """Test output of varying fibonacci sequence lengths"""
    iterative = fibonacci.fib_iterative(n)
    formula = fibonacci.fib_formula(n)
    assert iterative == seq
    assert formula == seq


@slash.tag('fibonacci')
@slash.parametrize('n', [7.3, 7.8, 7.0])
def test_float_input_iterative(n):
    """Test when user enters a float value"""
    iterative = fibonacci.fib_iterative(n)
    formula = fibonacci.fib_formula(n)
    assert iterative == default_fib
    assert formula == default_fib

