"""
Solve the 3-SAT algorithm with 2-approximation solution.

More information: https://en.wikipedia.org/wiki/Boolean_satisfiability_problem
"""
from typing import List, Dict


class Literal:
    """
    Represent a literal in the CNF formula.
    """

    def __init__(self, polarity: bool, name: str):
        self.polarity = polarity
        self.name = name


def _is_three_cnf_formula(cnf_formula: List[List[Literal]]) -> bool:
    """
    This function check if the given CNF formula is a valid 3-CNF formula.
    Each clause should consists of exactly 3 literals.
    :param cnf_formula: A CNF formula to check.
    :return: True if the given CNF formula is a 3-CNF formula.

    Examples:
    1) formula1 = (x1 ∨ x2 ∨ x3) ∧ (x1 ∨ x1 ∨ x1)
     This CNF formula is valid because each clause is consist of exactly 3 literals:

    >>> x1 = Literal(True, "x1")
    >>> x2 = Literal(True, "x2")
    >>> x3 = Literal(False, "x3")
    >>> formula1 = [[x1,x2,x3], [x1, x1, x1]]
    >>> _is_three_cnf_formula(formula1)
    True

    2) formula2 = (x1 ∨ x2 ∨ x3) ∧ (x1 ∨ x2)
    This CNF formula is invalid because the second clause is consist of 2 literals.
    >>> _is_three_cnf_formula([[x1, x2, x3], [x1, x2]])
    False
    """
    for clause in cnf_formula:
        if not len(clause) == 3:
            return False
    return True


def _count_clause_satisfiability(three_cnf_formula: List[List[Literal]], solution: Dict[str, bool]) -> int:
    """
    This function count how many clauses are satisfies from the given solution.
    :param three_cnf_formula: 3-CNF formula.
    :param solution: The solution to check.
    :return: How many clauses are satisfied from the given solution.

    Examples:
    1)
    formula1 = (x1 ∨ x2 ∨ x3) ∧ (x1 ∨ x1 ∨ x1)
    sol1 = {x1: True, x2: False, x3: False}
    => 2
    >>> x1 = Literal(True, "x1")
    >>> x2 = Literal(True, "x2")
    >>> not_x3 = Literal(False, "x3")
    >>> formula1 = [[x1, x2, not_x3], [x1, x1, x1]]
    >>> sol_formula1 = {"x1": True, "x2": False, "x3": False}
    >>> _count_clause_satisfiability(formula1, sol_formula1)
    2

    2)
    formula2 = (x1 ∨ x2 ∨ x3) ∧ (~x1 ∨ x3 ∨ ~x4)  ∧ (x2 ∨ ~x1 ∨ ~x4)
    sol2 = {x1: True, x2:True, x3: False, x4: True}
    => 2
    >>> not_x1 = Literal(False, "x1")
    >>> x3 = Literal(True, "x3")
    >>> not_x4 = Literal(False, "x4")
    >>> formula2 = [[x1, x2, x3], [not_x1, x3, not_x4], [x2, not_x1, not_x4]]
    >>> sol_formula2 = {"x1": True, "x2":True, "x3": False, "x4": True}
    >>> _count_clause_satisfiability(formula2, sol_formula2)
    2
    """
    num_of_satisfy_clauses = 0
    for clause in three_cnf_formula:
        for literal in clause:
            if literal.polarity == solution.get(literal.name):
                num_of_satisfy_clauses += 1
                break

    return num_of_satisfy_clauses


def three_satisfiability_2_approximation(three_cnf_formula: List[List[Literal]]) -> Dict[str, bool]:
    """
    This function receive 3-CNF formula and return a 2-approximation solution:
    Let OPT be the number of satisfies clauses at the optimal solution.
    Let X be the number of satisfies clauses at the this solution.
    So: OPT/X <= 2
    Which equivalent to: OPT/2<=X

    :param three_cnf_formula: 3-CNF formula to find a 2-approximation solution.
    :return: 2-approximation solution for the given formula.

    Examples:
    1) formula1 = (x1 ∨ x2 ∨ x3) ∧ (x4 ∨ ~x5 ∨ ~x1) ∧ (x1 ∨ ~x2 ∨ ~x5)
    The optimal solution for this formula is satisfied all (3) clauses, so our solution should
    satisfied at least 1.5 clauses:
    >>> x1 = Literal(True, "x1")
    >>> x2 = Literal(True, "x2")
    >>> x3 = Literal(True, "x3")
    >>> x4 = Literal(True, "x4")
    >>> x5 = Literal(True, "x5")
    >>> not_x1 = Literal(False, "x1")
    >>> not_x2 = Literal(False, "x2")
    >>> not_x5 = Literal(False, "x5")
    >>> formula1 = [[x1, x2, x3], [x4, not_x5, not_x1], [x1, not_x2, not_x5]]
    >>> sol_formula1 = three_satisfiability_2_approximation(formula1)
    >>> _count_clause_satisfiability(formula1, sol_formula1) >= 1.5
    True

    2) formula2 = (x1 ∨ x2 ∨ x3) ∧ (~x1 ∨ ~x2 ∨ ~x3)
    The optimal solution for this formula is satisfied 1 clauses, so our solution should
    satisfied at least 1 clauses:
    >>> x1 = Literal(True, "x1")
    >>> x2 = Literal(True, "x2")
    >>> x3 = Literal(True, "x3")
    >>> not_x1 = Literal(False, "x1")
    >>> not_x2 = Literal(False, "x2")
    >>> not_x3 = Literal(False, "x3")
    >>> formula2 = [[x1, x2, x3], [not_x1, not_x2, not_x3]]
    >>> sol_formula2 = three_satisfiability_2_approximation(formula2)
    >>> _count_clause_satisfiability(formula1, sol_formula1) >= 1
    True
    """
    assert _is_three_cnf_formula(three_cnf_formula), "Each formula must have exactly 3 literals."

    all_literals = []
    for clause in three_cnf_formula:
        all_literals.extend(clause)

    true_sol = {literal.name: True for literal in all_literals}
    false_sol = {literal.name: False for literal in all_literals}

    num_of_satisfy_true_sol = _count_clause_satisfiability(three_cnf_formula, true_sol)
    num_of_satisfy_false_sol = _count_clause_satisfiability(three_cnf_formula, false_sol)

    return true_sol if num_of_satisfy_true_sol >= num_of_satisfy_false_sol else false_sol


if __name__ == '__main__':
    import doctest

    doctest.testmod()
