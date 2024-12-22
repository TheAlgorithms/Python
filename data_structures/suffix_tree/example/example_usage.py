#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11554
#  https://github.com/TheAlgorithms/Python/pull/11554
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

from data_structures.suffix_tree.suffix_tree import SuffixTree


def main() -> None:
    """
    Demonstrate the usage of the SuffixTree class.

    - Initializes a SuffixTree with a predefined text.
    - Defines a list of patterns to search for within the suffix tree.
    - Searches for each pattern in the suffix tree.

    Patterns tested:
        - "ana" (found) --> True
        - "ban" (found) --> True
        - "na" (found) --> True
        - "xyz" (not found) --> False
        - "mon" (found) --> True
    """
    text = "monkey banana"
    suffix_tree = SuffixTree(text)

    patterns = ["ana", "ban", "na", "xyz", "mon"]
    for pattern in patterns:
        found = suffix_tree.search(pattern)
        print(f"Pattern '{pattern}' found: {found}")


if __name__ == "__main__":
    main()
