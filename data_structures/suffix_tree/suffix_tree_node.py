from typing import Dict, Optional


class SuffixTreeNode:
    def __init__(
        self,
        children: Optional[Dict[str, "SuffixTreeNode"]] = None,
        is_end_of_string: bool = False,
        start: Optional[int] = None,
        end: Optional[int] = None,
        suffix_link: Optional["SuffixTreeNode"] = None,
    ) -> None:
        """
        Initializes a suffix tree node.

        Parameters:
            children (Optional[Dict[str, SuffixTreeNode]]): The children of this node.
            is_end_of_string (bool): Indicates if this node represents
                                     the end of a string.
            start (Optional[int]): The start index of the suffix in the text.
            end (Optional[int]): The end index of the suffix in the text.
            suffix_link (Optional[SuffixTreeNode]): Link to another suffix tree node.
        """
        self.children = children or {}
        self.is_end_of_string = is_end_of_string
        self.start = start
        self.end = end
        self.suffix_link = suffix_link
