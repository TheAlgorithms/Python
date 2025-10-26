# Binary Tree Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Normal inorder traversal
def inorder(root, out):
    """Perform inorder traversal and append values to 'out' list."""
    if root is None:
        return
    inorder(root.left, out)
    out.append(root.data)
    inorder(root.right, out)


# === Build tree using PREORDER + INORDER ===
def build_tree_from_pre(
    preorder, pre_start, pre_end, inorder_seq, in_start, in_end, in_map
):
    """Recursive helper to build tree from preorder and inorder traversal."""
    if pre_start > pre_end or in_start > in_end:
        return None

    # Root is the first element in current preorder segment
    root_val = preorder[pre_start]
    root = Node(root_val)

    # Find the root index in inorder traversal
    in_root_index = in_map[root_val]
    nums_left = in_root_index - in_start

    # Recursively build left and right subtrees
    root.left = build_tree_from_pre(
        preorder,
        pre_start + 1,
        pre_start + nums_left,
        inorder_seq,
        in_start,
        in_root_index - 1,
        in_map,
    )

    root.right = build_tree_from_pre(
        preorder,
        pre_start + nums_left + 1,
        pre_end,
        inorder_seq,
        in_root_index + 1,
        in_end,
        in_map,
    )

    return root


def build_tree_pre(inorder_seq, preorder_seq):
    """Wrapper function for building tree from preorder + inorder."""
    in_map = {val: i for i, val in enumerate(inorder_seq)}
    return build_tree_from_pre(
        preorder_seq,
        0,
        len(preorder_seq) - 1,
        inorder_seq,
        0,
        len(inorder_seq) - 1,
        in_map,
    )


# === Build tree using POSTORDER + INORDER ===
def build_tree_from_post(
    postorder, post_start, post_end, inorder_seq, in_start, in_end, in_map
):
    """Recursive helper to build tree from postorder and inorder traversal."""
    if post_start > post_end or in_start > in_end:
        return None

    # Root is the last element in current postorder segment
    root_val = postorder[post_end]
    root = Node(root_val)

    # Find the root index in inorder traversal
    in_root_index = in_map[root_val]
    nums_left = in_root_index - in_start

    # Recursively build left and right subtrees
    root.left = build_tree_from_post(
        postorder,
        post_start,
        post_start + nums_left - 1,
        inorder_seq,
        in_start,
        in_root_index - 1,
        in_map,
    )

    root.right = build_tree_from_post(
        postorder,
        post_start + nums_left,
        post_end - 1,
        inorder_seq,
        in_root_index + 1,
        in_end,
        in_map,
    )

    return root


def build_tree_post(inorder_seq, postorder_seq):
    """Wrapper function for building tree from postorder + inorder."""
    in_map = {val: i for i, val in enumerate(inorder_seq)}
    return build_tree_from_post(
        postorder_seq,
        0,
        len(postorder_seq) - 1,
        inorder_seq,
        0,
        len(inorder_seq) - 1,
        in_map,
    )


# === Example ===
if __name__ == "__main__":
    inorder_seq = [1, 2, 3, 4, 5]
    preorder_seq = [3, 2, 1, 4, 5]
    postorder_seq = [1, 2, 5, 4, 3]

    print("=== Build BST from Preorder & Inorder ===")
    tree_pre = build_tree_pre(inorder_seq, preorder_seq)
    out = []
    inorder(tree_pre, out)
    print("Inorder:", *out)

    print("=== Build BST from Postorder & Inorder ===")
    tree_post = build_tree_post(inorder_seq, postorder_seq)
    out = []
    inorder(tree_post, out)
    print("Inorder:", *out)
