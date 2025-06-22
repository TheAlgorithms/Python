from __future__ import annotations

import random
from typing import Any

class MyQueue:
    __slots__ = ("data", "head", "tail")
    
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.head = self.tail = 0

    def is_empty(self) -> bool:
        return self.head == self.tail

    def push(self, data: Any) -> None:
        self.data.append(data)
        self.tail += 1

    def pop(self) -> Any:
        ret = self.data[self.head]
        self.head += 1
        return ret

class MyNode:
    __slots__ = ("data", "height", "left", "right")  # 按字母顺序排序
    
    def __init__(self, data: Any) -> None:
        self.data = data
        self.height = 1
        self.left: MyNode | None = None
        self.right: MyNode | None = None

def get_height(node: MyNode | None) -> int: 
    return node.height if node else 0

def my_max(a: int, b: int) -> int: 
    return a if a > b else b

def right_rotation(node: MyNode) -> MyNode:
    left_child = node.left
    if left_child is None:
        return node
    
    node.left = left_child.right
    left_child.right = node
    node.height = my_max(get_height(node.right), get_height(node.left)) + 1
    left_child.height = my_max(get_height(left_child.right), get_height(left_child.left)) + 1
    return left_child

def left_rotation(node: MyNode) -> MyNode:
    right_child = node.right
    if right_child is None:
        return node
    
    node.right = right_child.left
    right_child.left = node
    node.height = my_max(get_height(node.right), get_height(node.left)) + 1
    right_child.height = my_max(get_height(right_child.right), get_height(right_child.left)) + 1
    return right_child

def lr_rotation(node: MyNode) -> MyNode:
    if node.left:
        node.left = left_rotation(node.left)
    return right_rotation(node)

def rl_rotation(node: MyNode) -> MyNode:
    if node.right:
        node.right = right_rotation(node.right)
    return left_rotation(node)

def insert_node(node: MyNode | None, data: Any) -> MyNode | None:
    if node is None:
        return MyNode(data)
    
    if data < node.data:
        node.left = insert_node(node.left, data)
        if get_height(node.left) - get_height(node.right) == 2:
            if node.left and data < node.left.data:
                node = right_rotation(node)
            else:
                node = lr_rotation(node)
    else:
        node.right = insert_node(node.right, data)
        if get_height(node.right) - get_height(node.left) == 2:
            if node.right and data < node.right.data:
                node = rl_rotation(node)
            else:
                node = left_rotation(node)
    
    node.height = my_max(get_height(node.right), get_height(node.left)) + 1
    return node

def get_left_most(root: MyNode) -> Any:
    while root.left:
        root = root.left
    return root.data

def del_node(root: MyNode | None, data: Any) -> MyNode | None:
    if root is None:
        return None
        if data == root.data:
        if root.left and root.right:
            root.data = get_left_most(root.right)
            root.right = del_node(root.right, root.data)
        else:
            return root.left or root.right
    elif data < root.data:
        root.left = del_node(root.left, data)
    else:
        root.right = del_node(root.right, data)
    
    if root.left is None and root.right is None:
        root.height = 1
        return root
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    if right_height - left_height == 2:
        right_right = get_height(root.right.right) if root.right else 0
        right_left = get_height(root.right.left) if root.right else 0
        # 使用三元表达式
        root = left_rotation(root) if right_right > right_left else rl_rotation(root)
    elif left_height - right_height == 2:
        left_left = get_height(root.left.left) if root.left else 0
        left_right = get_height(root.left.right) if root.left else 0
        # 使用三元表达式
        root = right_rotation(root) if left_left > left_right else lr_rotation(root)
    
    root.height = my_max(get_height(root.right), get_height(root.left)) + 1
    return root

class AVLTree:
    __slots__ = ("root",)
    
    def __init__(self) -> None: 
        self.root: MyNode | None = None
        
    def get_height(self) -> int: 
        return get_height(self.root)
    
    def insert(self, data: Any) -> None:
        self.root = insert_node(self.root, data)
    
    def delete(self, data: Any) -> None:
        self.root = del_node(self.root, data)
    
    def __str__(self) -> str:
        if self.root is None:
            return ""
            
        levels = []
        # 明确指定类型为 MyNode | None
        queue: list[MyNode | None] = [self.root]
        
        while queue:
            current = []
            next_level: list[MyNode | None] = []
            
            for node in queue:
                if node:
                    current.append(str(node.data))
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    current.append("*")
                    next_level.extend([None, None])
            
            if any(node is not None for node in next_level):
                levels.append(" ".join(current))
                queue = next_level
            else:
                if current:  # 添加最后一行
                    levels.append(" ".join(current))
                break
        
        return "\n".join(levels) + "\n" + "*"*36

def test_avl_tree() -> None:
    t = AVLTree()
    lst = list(range(10))
    random.shuffle(lst)
    
    for i in lst:
        t.insert(i)
    
    random.shuffle(lst)
    for i in lst:
        t.delete(i)

if __name__ == "__main__":
    test_avl_tree()
