# 文件名：data_structures/binary_tree/splay_tree.py
from __future__ import annotations


class Node:
    """Splay树节点类"""

    def __init__(self, key: int):
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None


class SplayTree:
    """
    伸展树（Splay Tree）实现
    特性：每次访问节点后，将该节点旋转到根位置，优化局部性访问性能
    """

    def __init__(self):
        self.root: Node | None = None

    def _right_rotate(self, x: Node) -> Node:
        """右旋操作（zig）"""
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x: Node) -> Node:
        """左旋操作（zig）"""
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root: Node | None, key: int) -> Node | None:
        """
        核心伸展操作：将包含key的节点旋转到根
        包含zig、zig-zig、zig-zag三种模式
        """
        if root is None or root.key == key:
            return root

        # 目标节点在左子树
        if key < root.key:
            if root.left is None:
                return root
            # Zig-Zig模式：左-左
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._right_rotate(root)
            # Zig-Zag模式：左-右
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._left_rotate(root.left)
            return root.left if root.left is None else self._right_rotate(root)

        # 目标节点在右子树
        else:
            if root.right is None:
                return root
            # Zig-Zig模式：右-右
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._left_rotate(root)
            # Zig-Zag模式：右-左
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._right_rotate(root.right)
            return root.right if root.right is None else self._left_rotate(root)

    def search(self, key: int) -> bool:
        """搜索指定key，存在返回True，不存在返回False"""
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key

    def insert(self, key: int) -> None:
        """插入新节点"""
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self._splay(self.root, key)
        if self.root.key == key:
            return  # 已存在，无需插入

        new_node = Node(key)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def delete(self, key: int) -> None:
        """删除指定key的节点"""
        if self.root is None:
            return

        self.root = self._splay(self.root, key)
        if self.root.key != key:
            return  # 节点不存在

        # 左右子树合并
        if self.root.left is None:
            self.root = self.root.right
        else:
            temp = self.root.right
            self.root = self.root.left
            self.root = self._splay(self.root, key)
            self.root.right = temp

    def find_min(self) -> int | None:
        """查找树中最小值"""
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        self.root = self._splay(self.root, current.key)
        return current.key

    def find_max(self) -> int | None:
        """查找树中最大值"""
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        self.root = self._splay(self.root, current.key)
        return current.key

    def inorder_traversal(self, root: Node | None, result: list[int]) -> None:
        """中序遍历（有序输出）"""
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.key)
            self.inorder_traversal(root.right, result)

    def get_size(self, root: Node | None) -> int:
        """获取树的节点总数"""
        if root is None:
            return 0
        return 1 + self.get_size(root.left) + self.get_size(root.right)

    def get_height(self, root: Node | None) -> int:
        """获取树的高度"""
        if root is None:
            return -1
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def print_tree(
        self, root: Node | None, indent: str = "", last: bool = True
    ) -> None:
        """可视化打印树结构"""
        if root:
            print(indent + ("└── " if last else "├── ") + str(root.key))
            indent += "    " if last else "│   "
            self.print_tree(root.left, indent, False)
            self.print_tree(root.right, indent, True)


# 测试用例
if __name__ == "__main__":
    tree = SplayTree()
    # 插入测试
    for key in [10, 20, 30, 40, 50, 25]:
        tree.insert(key)
    print("中序遍历:", end=" ")
    traversal_result = []
    tree.inorder_traversal(tree.root, traversal_result)
    print(traversal_result)

    # 搜索测试（访问后节点会被伸展到根）
    print("\n搜索25:", tree.search(25))
    print("搜索后根节点:", tree.root.key)

    # 删除测试
    tree.delete(30)
    print("\n删除30后中序遍历:", end=" ")
    traversal_result = []
    tree.inorder_traversal(tree.root, traversal_result)
    print(traversal_result)

    # 辅助方法测试
    print("\n树大小:", tree.get_size(tree.root))
    print("树高度:", tree.get_height(tree.root))
    print("最小值:", tree.find_min())
    print("最大值:", tree.find_max())

    print("\n树结构:")
    tree.print_tree(tree.root)
