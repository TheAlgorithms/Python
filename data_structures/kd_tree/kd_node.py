from typing import Optional


class KDNode:
    """
    Represents a node in a KD-Tree.

    Attributes:
        point (list[float]): The point stored in this node.
        left (Optional[KDNode]): The left child node.
        right (Optional[KDNode]): The right child node.
    """

    def __init__(
        self,
        point: list[float],
        left: Optional["KDNode"] = None,
        right: Optional["KDNode"] = None,
    ) -> None:
        """
        Initializes a KDNode with the given point and child nodes.

        Args:
            point (list[float]): The point stored in this node.
            left (Optional[KDNode]): The left child node.
            right (Optional[KDNode]): The right child node.
        """
        self.point = point
        self.left = left
        self.right = right
