from __future__ import annotations
from typing import Dict, Optional


class SuffixTreeNode:
    def __init__(
        self,
        children: Dict[str, "SuffixTreeNode"] = None,
        is_end_of_string: bool = False,
        start: int | None = None,
        end: int | None = None,
        suffix_link: SuffixTreeNode | None = None,
    ) -> None:
        """
        Initializes a suffix tree node.

        Parameters:
            children (Dict[str, SuffixTreeNode], optional): The children of this node. Defaults to an empty dictionary.
            is_end_of_string (bool, optional): Indicates if this node represents the end of a string. Defaults to False.
            start (int | None, optional): The start index of the suffix in the text. Defaults to None.
            end (int | None, optional): The end index of the suffix in the text. Defaults to None.
            suffix_link (SuffixTreeNode | None, optional): Link to another suffix tree node. Defaults to None.
        """
        self.children = children or {}
        self.is_end_of_string = is_end_of_string
        self.start = start
        self.end = end
        self.suffix_link = suffix_link
