from operator import delitem, getitem, setitem
from typing import Any

import pytest

from data_structures.hashing.coalesced_hashing import CoalescedHashMap
from data_structures.hashing.fnv_hashtable import FNVHashMap
from data_structures.hashing.hopscotch import HopscotchHashMap
from data_structures.hashing.linear_probing import LinearProbing
from data_structures.hashing.power_of_two import PowerOfTwoHashMap

# Import all your new classes
from data_structures.hashing.robin_hood import RobinHoodHashMap


# --- WRAPPER FOR REPO-STYLE CLASSES ---
# Makes LinearProbing behave like a dict for testing
class RepoStyleWrapper:
    def __init__(self, size=10):
        self._backend = LinearProbing(size)

    def __setitem__(self, key: int, val: Any):
        # LinearProbing.insert_data(data) hashes 'data' to find index.
        # It doesn't support separate key/value pairs in the same way dict does.
        # It stores 'val' at hash(val).
        # So we only test it with integer keys where key == val for simplicity here.
        self._backend.insert_data(val)

    def __getitem__(self, key: int):
        # The repo implementation doesn't support O(1) retrieval by value easily
        # without looking at internal structure, or using search logic.
        # But wait! The repo's HashTable stores KEY=Hash, VALUE=Data.
        # It DOES NOT support random keys.
        # So we SKIP LinearProbing in this generic dict-compliance test
        # because its API is fundamentally different (Set vs Map).
        pass

    def __delitem__(self, key):
        pass

    def keys(self):
        return self._backend.keys().values()  # Return values as keys for comparison


# Helper functions
def _get(k):
    return getitem, k


def _set(k, v):
    return setitem, k, v


def _del(k):
    return delitem, k


def _run_operation(obj, fun, *args):
    try:
        return fun(obj, *args), None
    except Exception as e:  # noqa: BLE001
        return None, str(type(e).__name__)


# Test Scenarios
_add_items = (_set("key_a", "val_a"), _set("key_b", "val_b"))
_overwrite_items = [_set("key_a", "val_a"), _set("key_a", "val_b")]
_delete_items = [
    _set("key_a", "val_a"),
    _set("key_b", "val_b"),
    _del("key_a"),
    _del("key_b"),
]
_access_absent = [_get("key_a"), _del("key_a")]


# --- TEST 1: Modern MutableMapping Classes ---
@pytest.mark.parametrize(
    "hash_map_cls",
    [
        RobinHoodHashMap,
        HopscotchHashMap,
        CoalescedHashMap,
        FNVHashMap,
        PowerOfTwoHashMap,
    ],
)
@pytest.mark.parametrize(
    "operations",
    [
        pytest.param(_add_items, id="add"),
        pytest.param(_overwrite_items, id="overwrite"),
        pytest.param(_delete_items, id="delete"),
        pytest.param(_access_absent, id="absent_access"),
    ],
)
def test_compatibility_with_dict(hash_map_cls, operations):
    """
    Verify that new MutableMapping classes behave EXACTLY like a Python dict.
    """
    try:
        my_map = hash_map_cls()
    except TypeError:
        my_map = hash_map_cls(8)

    py_dict = {}

    for i, (fun, *args) in enumerate(operations):
        my_res, my_exc = _run_operation(my_map, fun, *args)
        py_res, py_exc = _run_operation(py_dict, fun, *args)

        assert my_res == py_res, f"{hash_map_cls.__name__}: Result mismatch at op {i}"
        assert my_exc == py_exc, (
            f"{hash_map_cls.__name__}: Exception mismatch at op {i}"
        )
        assert len(my_map) == len(py_dict)
        assert sorted(my_map.keys()) == sorted(py_dict.keys())


def test_linear_probing_specifics():
    """
    LinearProbing uses a different API (insert_data), so we test it separately.
    """
    lp = LinearProbing(5)

    # 1. Insertion
    lp.insert_data(10)  # hash(10)%5 = 0
    lp.insert_data(15)  # hash(15)%5 = 0 -> Collision -> Index 1

    # LinearProbing.keys() returns a dict of {index: value}
    # We must check membership in that dict, not the object itself.
    assert 0 in lp.keys()  # noqa: SIM118
    assert lp.keys()[0] == 10
    assert 1 in lp.keys()  # noqa: SIM118
    assert lp.keys()[1] == 15

    # 2. Resizing (Implicitly tested via inserts)
    lp = LinearProbing(2)
    lp.insert_data(1)
    lp.insert_data(2)
    lp.insert_data(3)  # Trigger resize

    assert len(lp.keys()) == 3
