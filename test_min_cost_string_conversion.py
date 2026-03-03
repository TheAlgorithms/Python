import pytest
from strings.min_cost_string_conversion import compute_transform_tables, assemble_transformation

def test_empty_strings():
    costs, ops = compute_transform_tables("", "", 1,1,1,1)
    assert costs == [[0]]
    assert assemble_transformation(ops, 0, 0) == []

def test_copy_only():
    costs, ops = compute_transform_tables("abc", "abc", 1,2,3,3)
    assert costs[-1][-1] == 3  # cost = sum of copy costs
    assert assemble_transformation(ops, len(ops)-1, len(ops[0])-1) == ["Ca", "Cb", "Cc"]

def test_insert_only():
    costs, ops = compute_transform_tables("", "xyz", 1,1,1,1)
    seq = assemble_transformation(ops, 0, len(ops[0])-1)
    assert seq == ["Ix", "Iy", "Iz"]
