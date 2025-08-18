"""
TT-ENTAILS Algorithm (Propositional Logic)
Reference: [Russell & Norvig, Artificial Intelligence: A Modern Approach, Ch. 7](https://aima.cs.berkeley.edu/)
Wikipedia: [Entailment](https://en.wikipedia.org/wiki/Entailment)

This algorithm checks if a knowledge base (KB) entails a query sentence (a)
using truth tables. Returns True if KB entails a, False otherwise.
"""

import itertools
import re


def safe_eval(expr: str, model: dict[str, bool]) -> bool:
    """Safely evaluate propositional logic expression with given model."""
    # Replace symbols (like P, Q) with their boolean values
    for sym, val in model.items():
        expr = re.sub(rf'\b{sym}\b', str(val), expr)
    # Allow only True/False, and/or/not operators
    allowed = {"True", "False", "and", "or", "not", "(", ")", " "}
    if not all(token in allowed or token.isidentifier() or token in "()" for token in re.split(r'(\W+)', expr)):
        raise ValueError("Unsafe expression detected")
    return eval(expr, {"__builtins__": {}}, {})


def tt_entails(kb: list[str], query: str, symbols: list[str]) -> bool:
    """
    Check if the knowledge base entails the query using truth tables.

    Args:
        kb (List[str]): List of propositional sentences in KB as strings
        query (str): Query sentence to test entailment
        symbols (List[str]): List of all propositional symbols used

    Returns:
        bool: True if KB entails query, False otherwise

    Example:
        tt_entails(["P or Q"], "Q", ["P","Q"])

    """
    for values in itertools.product([True, False], repeat=len(symbols)):
        model: dict[str, bool] = dict(zip(symbols, values))
        # Check if KB is true under this model
        # # If query is false in this model, KB does not entail query
        if all(safe_eval(sentence, model) for sentence in kb) and not safe_eval(query, model):
            return False
    return True


# Example usage
if __name__ == "__main__":
    # Example 1: KB entails query → should return True
    symbols = ["P", "Q"]
    kb = ["P or Q", "not P or Q"]  # KB says P or Q is True, and not P or Q is True
    query = "Q"  # Query: Is Q True?
    print("Does KB entail query? : ", tt_entails(kb, query, symbols))

    # Example 2: KB does NOT entail query → should return False
    symbols2 = ["P", "Q"]
    kb2 = ["P"]  # KB says only P is True
    query2 = "Q"  # Query asks if Q is True
    print("Does KB2 entail query2? : ", tt_entails(kb2, query2, symbols2))
