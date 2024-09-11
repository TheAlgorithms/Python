import logging

"""
Jaccard Similarity Algorithm - Natural Language Processing (NLP) Algorithm

Use Case:
    - Useful in text analysis and natural language processing (NLP) tasks.
    - Can be used for document similarity, plagiarism detection,
and information retrieval.

Dependencies:
    - Python Standard Library's logging module for error handling.
"""
class JaccardSimilarity:
    def __init__(self) -> None:
        """
        Initialize the JaccardSimilarity class.
        """

    def jaccard_similarity(self, str1: str, str2: str) -> float:
        """
        Calculate the Jaccard Similarity between two strings.

        Parameters:
        - str1 (str): The first string for comparison.
        - str2 (str): The second string for comparison.

        Returns:
        - float: The Jaccard similarity between the two strings as a percentage.

        Examples:
        >>> js = JaccardSimilarity()
        >>> js.jaccard_similarity("hello world", "hello there")
        33.33333333333333
        >>> js.jaccard_similarity("apple orange banana", "banana orange apple")
        100.0
        >>> js.jaccard_similarity("apple", "banana")
        0.0
        """
        if not str1 or not str2:
            raise ValueError("Input strings must not be empty.")

        try:
            set1 = set(str1.split())
            set2 = set(str2.split())

            intersection = set1.intersection(set2)
            union = set1.union(set2)

            similarity = len(intersection) / len(union)

            return similarity * 100
        except Exception as e:
            logging.error("An Error Occurred: ", exc_info=e)
            raise e

if __name__ == "__main__":
    """
    Main function to Test the Jaccard Similarity between two Texts.
    """
    import doctest

    doctest.testmod()  # Run the Doctests
