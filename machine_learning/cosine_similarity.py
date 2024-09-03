import spacy
import logging
import numpy as np

class Cosine_Similarity:
    """
    Cosine Similarity Algorithm

    Use Case:
    - The Cosine Similarity Algorithm measures the Cosine of the Angle between two Non-Zero Vectors in a Multi-Dimensional Space.
    - It is used to determine how similar two texts are based on their Vector representations.
    - The similarity score ranges from -1 (Completely Dissimilar) to 1 (Completely Similar), with 0 indicating no Similarity.

    Dependencies:
    - spacy: A Natural Language Processing library for Python, used here for Tokenization and Vectorization.
    - numpy: A Library for Numerical Operations in Python, used for Mathematical Computations.
    """
    
    def __init__(self) -> None:
        """
        Initializes the Cosine Similarity class by loading the SpaCy model.
        """
        self.nlp = spacy.load('en_core_web_md')
    
    def Tokenize(self, text: str) -> list:
        """
        Tokenizes the input text into a list of lowercased tokens.

        Parameters:
        - text (str): The input text to be tokenized.

        Returns:
        - list: A list of lowercased tokens.
        """
        try:
            doc = self.nlp(text)
            tokens = [token.text.lower() for token in doc if not token.is_punct]
            return tokens
        except Exception as e:
            logging.error("An error occurred during Tokenization: ", exc_info=e)
            raise e
        
    def Vectorize(self, tokens: list) -> list:
        """
        Converts tokens into their corresponding vector representations.

        Parameters:
        - tokens (list): A list of tokens to be vectorized.

        Returns:
        - list: A list of vectors corresponding to the tokens.
        """
        try:
            vectors = [self.nlp(token).vector for token in tokens if self.nlp(token).vector.any()]
            return vectors
        except Exception as e:
            logging.error("An error occurred during Vectorization: ", exc_info=e)
            raise e
        
    def Mean_Vector(self, vectors: list) -> np.ndarray:
        """
        Computes the mean vector of a list of vectors.

        Parameters:
        - vectors (list): A list of vectors to be averaged.

        Returns:
        - np.ndarray: The mean vector.
        """
        try:
            if not vectors:
                return np.zeros(self.nlp.vocab.vectors_length)
            return np.mean(vectors, axis=0)
        except Exception as e:
            logging.error("An error occurred while computing the Mean Vector: ", exc_info=e)
            raise e
        
    def Dot_Product(self, vector1: np.ndarray, vector2: np.ndarray) -> float:
        """
        Computes the dot product between two vectors.

        Parameters:
        - vector1 (np.ndarray): The first vector.
        - vector2 (np.ndarray): The second vector.

        Returns:
        - float: The dot product of the two vectors.
        """
        try:
            return np.dot(vector1, vector2)
        except Exception as e:
            logging.error("An error occurred during the dot Product Calculation: ", exc_info=e)
            raise e
        
    def Magnitude(self, vector: np.ndarray) -> float:
        """
        Computes the magnitude (norm) of a vector.

        Parameters:
        - vector (np.ndarray): The vector whose magnitude is to be calculated.

        Returns:
        - float: The magnitude of the vector.
        """
        try:
            return np.sqrt(np.sum(vector ** 2))
        except Exception as e:
            logging.error("An error occurred while computing the Magnitude: ", exc_info=e)
            raise e
        
    def Cosine_Similarity(self, vector1: np.ndarray, vector2: np.ndarray) -> float:
        """
        Computes the cosine similarity between two vectors.

        Parameters:
        - vector1 (np.ndarray): The first vector.
        - vector2 (np.ndarray): The second vector.

        Returns:
        - float: The cosine similarity between the two vectors.
        """
        try:
            dot = self.Dot_Product(vector1, vector2)
            magnitude1, magnitude2 = self.Magnitude(vector1), self.Magnitude(vector2)
            if magnitude1 == 0 or magnitude2 == 0:
                return 0.0
            return dot / (magnitude1 * magnitude2)
        except Exception as e:
            logging.error("An error occurred during Cosine Similarity Calculation: ", exc_info=e)
            raise e
        
    def Cosine_Similarity_Percentage(self, text1: str, text2: str) -> float:
        """
        Computes the cosine similarity percentage between two texts.

        Parameters:
        - text1 (str): The first text.
        - text2 (str): The second text.

        Returns:
        - float: The cosine similarity percentage between the two texts.
        """
        try:
            tokens1 = self.Tokenize(text1)
            tokens2 = self.Tokenize(text2)
            
            vectors1 = self.Vectorize(tokens1)
            vectors2 = self.Vectorize(tokens2)
            
            mean_vec1 = self.Mean_Vector(vectors1)
            mean_vec2 = self.Mean_Vector(vectors2)
 
            similarity = self.Cosine_Similarity(mean_vec1, mean_vec2)
            return similarity * 100
        except Exception as e:
            logging.error("An error occurred while computing the Cosine Similarity Percentage: ", exc_info=e)
            raise e
        
if __name__ == "__main__":
    """
    Main function to Test the Cosine Similarity between two Texts.
    """
    text1 = input("Please enter text 1: ")
    text2 = input("Please enter text 2: ")
    
    similarity_percentage = Cosine_Similarity().Cosine_Similarity_Percentage(text1, text2)
    print(f"Cosine Similarity: {similarity_percentage:.2f}%")