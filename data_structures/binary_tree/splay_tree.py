class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self) -> None:
        self.root = None

    def left_rotate(self, node) -> None:
        y = node.right
        node.right = y.left
        if y.left != None:
            y.left.parent = node

        y.parent = node.parent
        # x is root
        if node.parent == None:
            self.root = y
        # x is left child
        elif node == node.parent.left:
            node.parent.left = y
        # x is right child
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def right_rotate(self, node) -> None:
        y = node.left
        node.left = y.right
        if y.right != None:
            y.right.parent = node

        y.parent = node.parent
        # x is root
        if node.parent == None:
            self.root = y
        # x is right child
        elif node == node.parent.right:
            node.parent.right = y
        # x is left child
        else:
            node.parent.left = y

        y.right = node
        node.parent = y

    def splay(self, node) -> None:
        # node is not root
        while node.parent != None:
            # node is child of root, one rotation
            if node.parent == self.root:
                if node == node.parent.left:
                    self.right_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)

            else:
                p = node.parent
                g = p.parent  # grandparent

                if node.parent.left == node and p.parent.left == p:  # both are left children
                    self.right_rotate(g)
                    self.right_rotate(p)

                elif (
                    node.parent.right == node and p.parent.right == p
                ):  # both are right children
                    self.left_rotate(g)
                    self.left_rotate(p)

                elif node.parent.right == node and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)

                elif node.parent.left == node and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)

    def insert(self, node) -> None:
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if node.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        node.parent = y

        if y == None:  # newly added node is root
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self.splay(node)

    def bst_search(self, node, value) -> None:
        if value == node.data:
            self.splay(node)
            return node
        elif value < node.data:
            return self.bst_search(node.left, value)
        elif value > node.data:
            return self.bst_search(node.right, value)
        else:
            return None

    def pre_order(self, node) -> None:
        if node != None:
            print(node.data)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node) -> None:
        if node != None:
            self.in_order(node.left)
            print(node.data)
            self.in_order(node.right)

    def post_order(self, node) -> None:
        if node != None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data)


def main() -> None:
    tree = SplayTree()

    tree.insert(Node(90))
    """
    The tree looks like this:
                        90
    """

    tree.insert(Node(10))
    """
    The tree looks like this:
                        90
                       /
                      10
    """

    tree.insert(Node(34))
    """
    The tree looks like this:
                        34
                       /  \
                      10   90
    """

    tree.insert(Node(18))
    """
    The tree looks like this:
                        18
                       /  \
                      10   34
                            \
                            90
    """

    tree.insert(Node(25))
    """
    The tree looks like this:
                        25
                       /  \
                     18    34
                    /        \
                   10        90
    """

    tree.insert(Node(60))
    """
    The tree looks like this:
                        60
                       /  \
                     25    90
                    /  \
                   18   34
                  /
                10
    """

    tree.insert(Node(100))
    """
    Finally the tree looks like this:
                        100
                       /
                      90
                     /
                    60
                   /
                  25
                 /  \
                18   34
               /
              10
    """

    tree.bst_search(tree.root, 10)  # splay 10 to root
    """
    The tree looks like this:
                        10
                          \
                          100
                         /
                        60
                       /  \
                      18   90
                        \
                         25
                           \
                            34
    """

    print("The Pre-order traveral of the tree is:")
    tree.pre_order(tree.root)
    """
    The traversal of the tree is:   10, 100, 60, 18, 25, 34, 90
    """

    print("The In-order traveral of the tree is:")
    tree.in_order(tree.root)
    """
    The traversal of the tree is:   10, 100, 60, 18, 25, 34, 90
    """

    print("The Post-order traveral of the tree is:")
    tree.post_order(tree.root)
    """
    The traversal of the tree is:   34, 25, 18, 90, 60, 100, 10
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
