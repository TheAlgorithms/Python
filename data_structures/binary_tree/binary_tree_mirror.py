def mirror_subtree(tree: dict, root: int):
    if root not in tree:
        return
    left, right = tree[root]
    tree[root] = [right, left]
    if left:
        mirror_subtree(tree, left)
    if right:
        mirror_subtree(tree, right)


def mirror_binary_tree(tree: dict, root: int = 1) -> dict:
    """
    Returns the mirror of the given binary tree starting from the root.

    >>> mirror_binary_tree({1: [2, 3], 2: [4, 5], 3: [6, 7], 7: [8, 9]}, 1)
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 7: [9, 8]}
    >>> mirror_binary_tree({1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [10, 11]}, 1)
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 4: [11, 10]}
    >>> mirror_binary_tree({1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [10, 11]}, 5)
    Traceback (most recent call last):
        ...
    ValueError: Root 5 is not present in the binary tree
    >>> mirror_binary_tree({}, 5)
    Traceback (most recent call last):
        ...
    ValueError: Binary tree cannot be empty
    """
    if not tree:
        raise ValueError("Binary tree cannot be empty")
    if root not in tree:
        raise ValueError(f"Root {root} is not present in the binary tree")

    mirrored_tree = dict(tree)
    mirror_subtree(mirrored_tree, root)
    return mirrored_tree


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    binary_tree = {1: [2, 3], 2: [4, 5], 3: [6, 7], 7: [8, 9]}
    print(f"Original binary tree: {binary_tree}")
    mirrored_tree = mirror_binary_tree(binary_tree, 1)
    print(f"Mirrored binary tree: {mirrored_tree}")
