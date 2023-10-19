"""
The FP-Growth (Frequent Pattern Growth) algorithm is a widely used
data mining technique for discovering frequent itemsets in
large transaction databases.
It overcomes some of the limitations of traditional methods like
Apriori by efficiently constructing the FP-Tree

WIKI: https://athena.ecs.csus.edu/~mei/associationcw/FpGrowth.html
Examples: https://www.javatpoint.com/fp-growth-algorithm-in-data-mining
"""

from typing import Optional


class TreeNode:
    """
    Initialize a TreeNode.

    Args:
        name_value (str): The name of the node.
        num_occur (int): The number of occurrences of the node.
        parent_node (TreeNode): The parent node.

    Example:
    >>> parent = TreeNode("Parent", 1, None)
    >>> child = TreeNode("Child", 2, parent)
    >>> child.name
    'Child'
    >>> child.count
    2
    """

    def __init__(
        self, name_value: str, num_occur: int, parent_node: Optional["TreeNode"] = None
    ) -> None:
        self.name = name_value
        self.count = num_occur
        self.node_link = None  # Initialize node_link to None
        self.parent = parent_node
        self.children: dict[str, TreeNode] = {}

    def inc(self, num_occur: int) -> None:
        self.count += num_occur

    def disp(self, ind: int = 1) -> None:
        print("  " * ind, self.name, " ", self.count)
        for child in self.children.values():
            child.disp(ind + 1)


def create_tree(data_set: list, min_sup: int = 1) -> tuple[TreeNode, dict]:
    """
    Create FP tree

    Args:
        data_set (list): A list of transactions, where each transaction
        is a list of items.
        min_sup (int, optional): The minimum support threshold.
        Items with support less than this will be pruned. Default is 1.

    Returns:
        TreeNode: The root of the FP-Tree.
        dict: The header table.

    Example:
    >>> data_set = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_sup = 2
    >>> fp_tree, header_table = create_tree(data_set, min_sup)

    >>> sorted(list(header_table.keys()))
    ['A', 'B', 'C', 'E']

    >>> fp_tree.name
    'Null Set'
    >>> sorted(fp_tree.children.keys())
    ['A', 'B']
    >>> fp_tree.children['A'].name
    'A'
    >>> sorted(fp_tree.children['A'].children.keys())
    ['B', 'C']

    """
    header_table: dict = {}
    for trans in data_set:
        for item in trans:
            header_table[item] = header_table.get(item, [0, None])
            header_table[item][0] += 1

    for k in list(header_table.keys()):
        if header_table[k][0] < min_sup:
            del header_table[k]

    freq_item_set = set(header_table.keys())

    if len(freq_item_set) == 0:
        return TreeNode("Null Set", 1, None), {}

    for k in header_table:
        header_table[k] = [header_table[k], None]

    fp_tree = TreeNode("Null Set", 1, None)  # Parent is None for the root node
    for tran_set in data_set:
        local_d = {}
        for item in tran_set:
            if item in freq_item_set:
                local_d[item] = header_table[item][0]
        if len(local_d) > 0:
            sorted_items = sorted(
                local_d.items(), key=lambda item_info: item_info[1], reverse=True
            )
            ordered_items = [item[0] for item in sorted_items]
            update_tree(ordered_items, fp_tree, header_table, 1)

    return fp_tree, header_table


def update_tree(items: list, in_tree: TreeNode, header_table: dict, count: int) -> None:
    """
    Update the FP-Tree with a transaction.

    Args:
        items (list): List of items in the transaction.
        in_tree (TreeNode): The current node in the FP-Tree.
        header_table (dict): The header table with item information.
        count (int): The count of the transaction.

    Example:
    >>> data_set = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_sup = 2
    >>> fp_tree, header_table = create_tree(data_set, min_sup)

    >>> transaction = ['A', 'B', 'E']
    >>> update_tree(transaction, fp_tree, header_table, 1)

    >>> sorted(fp_tree.children['A'].children['B'].children['E'].children.keys())
    []
    >>> fp_tree.children['A'].children['B'].children['E'].count
    2
    >>> header_table['E'][1].name
    'E'
    """
    if items[0] in in_tree.children:
        in_tree.children[items[0]].inc(count)
    else:
        in_tree.children[items[0]] = TreeNode(items[0], count, in_tree)
        if header_table[items[0]][1] is None:
            header_table[items[0]][1] = in_tree.children[items[0]]
        else:
            update_header(header_table[items[0]][1], in_tree.children[items[0]])
    if len(items) > 1:
        update_tree(items[1:], in_tree.children[items[0]], header_table, count)


def update_header(node_to_test: TreeNode, target_node: TreeNode) -> None:
    """
    Update the header table with a node link.

    Args:
        node_to_test (TreeNode): The node to be updated in the header table.
        target_node (TreeNode): The node to link to.

    Example:
    >>> data_set = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_sup = 2
    >>> fp_tree, header_table = create_tree(data_set, min_sup)

    >>> node1 = TreeNode("A", 3, None)
    >>> node2 = TreeNode("B", 4, None)
    >>> update_header(node1, node2)

    >>> node1.node_link.name
    'B'
    >>> node2.node_link is None
    True
    """
    if node_to_test is None:
        node_to_test = TreeNode(None, 0, None)
    while node_to_test is not None and node_to_test.node_link is not None:
        node_to_test = node_to_test.node_link
    node_to_test.node_link = target_node


def ascend_tree(leaf_node: TreeNode, prefix_path: list) -> None:
    """
    Ascend the FP-Tree from a leaf node to its root,
    adding item names to the prefix path.

    Args:
        leaf_node (TreeNode): The leaf node to start ascending from.
        prefix_path (list): A list to store the item as they are ascended.

    Example:
    >>> data_set = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_sup = 2
    >>> fp_tree, header_table = create_tree(data_set, min_sup)

    >>> path = []
    >>> ascend_tree(fp_tree.children['A'], path)
    >>> path # ascending from a leaf node 'A'
    ['A']
    """
    if leaf_node.parent is not None:
        prefix_path.append(leaf_node.name)
        ascend_tree(leaf_node.parent, prefix_path)


def find_prefix_path(base_pat: frozenset, tree_node: TreeNode | None) -> dict:
    """
    Find the conditional pattern base for a given base pattern.

    Args:
        base_pat (frozenset): The base pattern for which to find
        the conditional pattern base.
        tree_node (TreeNode): The node in the FP-Tree.

    Example:
    >>> data_set = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_sup = 2
    >>> fp_tree, header_table = create_tree(data_set, min_sup)
    >>> base_pattern = frozenset(['A'])
    >>> cond_pat = find_prefix_path(base_pattern, fp_tree.children['A'])
    >>> sorted(cond_pat.keys())
    []
    """
    cond_pats: dict = {}
    while tree_node is not None:
        prefix_path: list = []
        ascend_tree(tree_node, prefix_path)
        if len(prefix_path) > 1:
            cond_pats[frozenset(prefix_path[1:])] = tree_node.count
        tree_node = tree_node.node_link
    return cond_pats


def mine_tree(
    in_tree: TreeNode,
    header_table: dict,
    min_sup: int,
    pre_fix: set,
    freq_item_list: list,
) -> None:
    """
    Mine the FP-Tree recursively to discover frequent itemsets.

    Args:
        in_tree (TreeNode): The FP-Tree to mine.
        header_table (dict): The header table with item information.
        min_sup (int): The minimum support threshold.
        pre_fix (set): A set of items as a prefix for the itemsets being mined.
        freq_item_list (list): A list to store the frequent itemsets.

    Example:
    >>> data_set = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_sup = 2
    >>> fp_tree, header_table = create_tree(data_set, min_sup)

    >>> frequent_itemsets = []
    >>> mine_tree(fp_tree, header_table, min_sup, set([]), frequent_itemsets)
    >>> expe_itm = [{'C'}, {'C', 'A'}, {'E'}, {'A', 'E'}, {'E', 'B'}, {'A'}, {'B'}]
    >>> all(expected in frequent_itemsets for expected in expe_itm)
    True
    """
    sorted_items = sorted(header_table.items(), key=lambda item_info: item_info[1][0])
    big_l = [item[0] for item in sorted_items]
    for base_pat in big_l:
        new_freq_set = pre_fix.copy()
        new_freq_set.add(base_pat)
        freq_item_list.append(new_freq_set)
        cond_patt_bases = find_prefix_path(base_pat, header_table[base_pat][1])
        my_cond_tree, my_head = create_tree(list(cond_patt_bases.keys()), min_sup)
        if my_head is not None:
            mine_tree(my_cond_tree, my_head, min_sup, new_freq_set, freq_item_list)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    data_set: list = [
        frozenset(["bread", "milk", "cheese"]),
        frozenset(["bread", "milk"]),
        frozenset(["bread", "diapers"]),
        frozenset(["bread", "milk", "diapers"]),
        frozenset(["milk", "diapers"]),
        frozenset(["milk", "cheese"]),
        frozenset(["diapers", "cheese"]),
        frozenset(["bread", "milk", "cheese", "diapers"]),
    ]
    fp_tree, header_table = create_tree(data_set, min_sup=3)
    freq_items: list = []
    mine_tree(fp_tree, header_table, 3, set(), freq_items)
    print(freq_items)
