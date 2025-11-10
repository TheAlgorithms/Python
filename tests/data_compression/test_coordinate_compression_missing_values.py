from data_compression.coordinate_compression import CoordinateCompressor
import math


def test_basic_compression():
    arr = [100, 10, 52, 83]
    cc = CoordinateCompressor(arr)
    assert cc.compress(10) == 0
    assert cc.compress(83) == 2 or cc.compress(83) == 3
    assert cc.decompress(0) == 10


def test_with_none_and_nan():
    arr = [100, None, 52, 83, float("nan")]
    cc = CoordinateCompressor(arr)
    assert cc.compress(None) == -1
    assert cc.compress(float("nan")) == -1
    assert cc.compress(52) != -1
    assert cc.decompress(5) == -1


def test_duplicate_values():
    arr = [10, 10, 10]
    cc = CoordinateCompressor(arr)
    assert cc.compress(10) == 0
    assert cc.decompress(0) == 10
