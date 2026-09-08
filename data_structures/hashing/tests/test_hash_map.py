from operator import delitem, getitem, setitem

import pytest

from data_structures.hashing.hash_map import HashMap


def _get(k):
    return getitem, k


def _set(k, v):
    return setitem, k, v


def _del(k):
    return delitem, k


def _run_operation(obj, fun, *args):
    try:
        return fun(obj, *args), None
    except Exception as e:
        return None, e


_add_items = (
    _set("key_a", "val_a"),
    _set("key_b", "val_b"),
)

_overwrite_items = [
    _set("key_a", "val_a"),
    _set("key_a", "val_b"),
]

_delete_items = [
    _set("key_a", "val_a"),
    _set("key_b", "val_b"),
    _del("key_a"),
    _del("key_b"),
    _set("key_a", "val_a"),
    _del("key_a"),
]

_access_absent_items = [
    _get("key_a"),
    _del("key_a"),
    _set("key_a", "val_a"),
    _del("key_a"),
    _del("key_a"),
    _get("key_a"),
]

_add_with_resize_up = [
    *[_set(x, x) for x in range(5)],  # guaranteed upsize
]

_add_with_resize_down = [
    *[_set(x, x) for x in range(5)],  # guaranteed upsize
    *[_del(x) for x in range(5)],
    _set("key_a", "val_b"),
]


@pytest.mark.parametrize(
    "operations",
    [
        pytest.param(_add_items, id="add items"),
        pytest.param(_overwrite_items, id="overwrite items"),
        pytest.param(_delete_items, id="delete items"),
        pytest.param(_access_absent_items, id="access absent items"),
        pytest.param(_add_with_resize_up, id="add with resize up"),
        pytest.param(_add_with_resize_down, id="add with resize down"),
    ],
)
def test_hash_map_is_the_same_as_dict(operations):
    my = HashMap(initial_block_size=4)
    py = {}
    for _, (fun, *args) in enumerate(operations):
        my_res, my_exc = _run_operation(my, fun, *args)
        py_res, py_exc = _run_operation(py, fun, *args)
        assert my_res == py_res
        assert str(my_exc) == str(py_exc)
        assert set(py) == set(my)
        assert len(py) == len(my)
        assert set(my.items()) == set(py.items())


def test_no_new_methods_was_added_to_api():
    def is_public(name: str) -> bool:
        return not name.startswith("_")

    dict_public_names = {name for name in dir({}) if is_public(name)}
    hash_public_names = {name for name in dir(HashMap()) if is_public(name)}

    assert dict_public_names > hash_public_names
