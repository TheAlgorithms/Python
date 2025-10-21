from typing import Any, Optional, List


class BSTNode:
    def __init__(self, key: Any):
        self.key = key
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: Any) -> None:
        def _insert(node: Optional[BSTNode], key: Any) -> BSTNode:
            if not node:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def search(self, key: Any) -> bool:
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self) -> List[Any]:
        res: List[Any] = []

        def _in(node: Optional[BSTNode]) -> None:
            if not node:
                return
            _in(node.left)
            res.append(node.key)
            _in(node.right)

        _in(self.root)
        return res
