from typing import List, Optional

class KDNode:
    """
    Represents a node in a KD-Tree.

    Attributes:
        point (List[float]): The k-dimensional point stored in this node.
        left (Optional[KDNode]): The left subtree of this node.
        right (Optional[KDNode]): The right subtree of this node.
    """

    def __init__(self, point: List[float], left: Optional['KDNode'] = None, right: Optional['KDNode'] = None) -> None:
        """
        Initializes a KDNode with a point and optional left and right children.

        Args:
            point (List[float]): The k-dimensional point to be stored in this node.
            left (Optional[KDNode]): The left subtree of this node. Defaults to None.
            right (Optional[KDNode]): The right subtree of this node. Defaults to None.
        """
        self.point = point
        self.left = left
        self.right = right
