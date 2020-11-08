"""
Davis–Putnam–Logemann–Loveland (DPLL) algorithm is a complete,
backtracking-based search algorithm for deciding the satisfiability of
propositional logic formulae in conjunctive normal form,
i.e, for solving the CNF-SAT problem.

For more information about the algorithm:
https://en.wikipedia.org/wiki/DPLL_algorithm
"""

import random
from typing import Dict, List


class Clause:
    """
    A clause represented in CNF.
    A clause is a set of literals, either complemented or otherwise.
    For example:
        {A1, A2, A3'} is the clause (A1 v A2 v A3')
        {A5', A2', A1} is the clause (A5' v A2' v A1)

    Create a set of literals and a clause with them
    >>> literals = ["A1", "A2'", "A3"]
    >>> clause = Clause(literals)
    >>> print(clause)
    { A1 , A2' , A3 }

    Create model
    >>> model = {"A1": True}
    >>> clause.evaluate(model)
    True
    """

    def __init__(self, literals: List[int]) -> None:
        """
        Represent the literals and an assignment in a clause."
        """
        # Assign all literals to None initially
        self.literals = {literal: None for literal in literals}
        self.no_of_literals = len(self.literals)

    def __str__(self) -> str:
        """
        To print a clause as in CNF.
        Variable clause holds the string representation.
        """
        clause = "{ "
        for i in range(0, self.no_of_literals):
            clause += str(list(self.literals.keys())[i]) + " "
            if i != self.no_of_literals - 1:
                clause += ", "
        clause += "}"

        return clause

    def assign(self, model: Dict[str, bool]) -> None:
        """
        Assign values to literals of the clause as given by model.
        """
        i = 0
        while i < self.no_of_literals:
            symbol = list(self.literals.keys())[i][:2]
            if symbol in model.keys():
                val = model[symbol]
            else:
                i += 1
                continue
            if val is not None:
                # Complement assignment if literal is in complemented form
                if list(self.literals.keys())[i][-1] == "'":
                    val = not val
            self.literals[list(self.literals.keys())[i]] = val
            i += 1

    def evaluate(self, model: Dict[str, bool]) -> bool:
        """
        Evaluates the clause with the assignments in model.
        This has the following steps:
        1. Return True if both a literal and its complement exist in the clause.
        2. Return True if a single literal has the assignment True.
        3. Return None(unable to complete evaluation) if a literal has no assignment.
        4. Compute disjunction of all values assigned in clause.
        """
        for literal in self.literals:
            if len(literal) == 2:
                symbol = literal + "'"
                if symbol in self.literals:
                    return True
            else:
                symbol = literal[:2]
                if symbol in self.literals:
                    return True

        self.assign(model)
        result = False
        for j in self.literals.values():
            if j in (True, None):
                return j
        for j in self.literals.values():
            result = result or j
        return result


class Formula:
    """
    A formula represented in CNF.
    A formula is a set of clauses.
    For example,
        {{A1, A2, A3'}, {A5', A2', A1}} is ((A1 v A2 v A3') and (A5' v A2' v A1))

    Create two clauses and a formula with them
    >>> clause1 = Clause(["A1", "A2'", "A3"])
    >>> clause2 = Clause(["A5'", "A2'", "A1"])

    >>> formula = Formula([clause1, clause2])
    >>> print(formula)
    {{ A1 , A2' , A3 } , { A5' , A2' , A1 }}
    """

    def __init__(self, clauses: List[Clause]) -> None:
        """
        Represent the number of clauses and the clauses themselves.
        """
        self.clauses = [c for c in clauses]
        self.no_of_clauses = len(self.clauses)

    def __str__(self) -> str:
        """
        To print a formula as in CNF.
        Variable formula holds the string representation.
        """
        formula = "{"
        clause_repr = " , "
        clauses_as_strings = [str(clause) for clause in self.clauses]

        clause_repr = clause_repr.join(clauses_as_strings)

        formula += clause_repr
        formula += "}"

        return formula


def generate_clause() -> Clause:
    """
    Randomly generate a clause.
    All literals have the name Ax, where x is an integer from 1 to 5.
    """
    literals = []
    no_of_literals = random.randint(1, 5)
    base_var = "A"
    i = 0
    while i < no_of_literals:
        var_no = random.randint(1, 5)
        var_name = base_var + str(var_no)
        var_complement = random.randint(0, 1)
        if var_complement == 1:
            var_name += "'"
        if var_name in literals:
            i -= 1
        else:
            literals.append(var_name)
        i += 1
    return Clause(literals)


def generate_formula() -> Formula:
    """
    Randomly generate a formula.
    """
    clauses = []
    no_of_clauses = random.randint(1, 10)
    i = 0
    while i < no_of_clauses:
        clause = generate_clause()
        if clause in clauses:
            i -= 1
        else:
            clauses.append(clause)
        i += 1
    return Formula(set(clauses))


def generate_parameters(formula: Formula) -> (List[Clause], List[str]):
    """
    Return the clauses and symbols from a formula.
    A symbol is the uncomplemented form of a literal.
    For example,
        Symbol of A3 is A3.
        Symbol of A5' is A5.

    >>> clause1 = Clause(["A1", "A2'", "A3"])
    >>> clause2 = Clause(["A5'", "A2'", "A1"])

    >>> formula = Formula([clause1, clause2])
    >>> clauses, symbols = generate_parameters(formula)
    >>> clauses_list = [str(i) for i in clauses]
    >>> print(clauses_list)
    ["{ A1 , A2' , A3 }", "{ A5' , A2' , A1 }"]
    >>> print(symbols)
    ['A1', 'A2', 'A3', 'A5']
    """
    clauses = formula.clauses
    symbols_set = []
    for clause in formula.clauses:
        for literal in clause.literals:
            symbol = literal[:2]
            if symbol not in symbols_set:
                symbols_set.append(symbol)
    return clauses, symbols_set


def find_pure_symbols(
    clauses: List[Clause], symbols: List[str], model: Dict[str, bool]
) -> (List[str], Dict[str, bool]):
    """
    Return pure symbols and their values to satisfy clause.
    Pure symbols are symbols in a formula that exist only
    in one form, either complemented or otherwise.
    For example,
        { { A4 , A3 , A5' , A1 , A3' } , { A4 } , { A3 } } has
        pure symbols A4, A5' and A1.
    This has the following steps:
    1. Ignore clauses that have already evaluated to be True.
    2. Find symbols that occur only in one form in the rest of the clauses.
    3. Assign value True or False depending on whether the symbols occurs
    in normal or complemented form respectively.

    >>> clause1 = Clause(["A1", "A2'", "A3"])
    >>> clause2 = Clause(["A5'", "A2'", "A1"])

    >>> formula = Formula([clause1, clause2])
    >>> clauses, symbols = generate_parameters(formula)

    >>> model = {}
    >>> pure_symbols, values = find_pure_symbols(clauses, symbols, model)
    >>> print(pure_symbols, values)
    ['A1', 'A2', 'A3', 'A5'] {'A1': True, 'A2': False, 'A3': True, 'A5': False}
    """
    pure_symbols = []
    assignment = dict()
    literals = []

    for clause in clauses:
        if clause.evaluate(model) is True:
            continue
        for literal in clause.literals:
            literals.append(literal)

    for s in symbols:
        sym = s + "'"
        if (s in literals and sym not in literals) or (
            s not in literals and sym in literals
        ):
            pure_symbols.append(s)
    for p in pure_symbols:
        assignment[p] = None
    for s in pure_symbols:
        sym = s + "'"
        if s in literals:
            assignment[s] = True
        elif sym in literals:
            assignment[s] = False
    return pure_symbols, assignment


def find_unit_clauses(
    clauses: List[Clause], model: Dict[str, bool]
) -> (List[str], Dict[str, bool]):
    """
    Returns the unit symbols and their values to satisfy clause.
    Unit symbols are symbols in a formula that are:
    - Either the only symbol in a clause
    - Or all other literals in that clause have been assigned False
    This has the following steps:
    1. Find symbols that are the only occurrences in a clause.
    2. Find symbols in a clause where all other literals are assigned False.
    3. Assign True or False depending on whether the symbols occurs in
    normal or complemented form respectively.

    >>> clause1 = Clause(["A4", "A3", "A5'", "A1", "A3'"])
    >>> clause2 = Clause(["A4"])
    >>> clause3 = Clause(["A3"])

    >>> formula = Formula([clause1, clause2, clause3])
    >>> clauses, symbols = generate_parameters(formula)

    >>> model = {}
    >>> unit_clauses, values = find_unit_clauses(clauses, model)

    >>> print(unit_clauses, values)
    ['A4', 'A3'] {'A4': True, 'A3': True}
    """
    unit_symbols = []
    for clause in clauses:
        if clause.no_of_literals == 1:
            unit_symbols.append(list(clause.literals.keys())[0])
        else:
            Fcount, Ncount = 0, 0
            for literal, value in clause.literals.items():
                if value is False:
                    Fcount += 1
                elif value is None:
                    sym = literal
                    Ncount += 1
            if Fcount == clause.no_of_literals - 1 and Ncount == 1:
                unit_symbols.append(sym)
    assignment = dict()
    for i in unit_symbols:
        symbol = i[:2]
        assignment[symbol] = len(i) == 2
    unit_symbols = [i[:2] for i in unit_symbols]

    return unit_symbols, assignment


def dpll_algorithm(
    clauses: List[Clause], symbols: List[str], model: Dict[str, bool]
) -> (bool, Dict[str, bool]):
    """
    Returns the model if the formula is satisfiable, else None
    This has the following steps:
    1. If every clause in clauses is True, return True.
    2. If some clause in clauses is False, return False.
    3. Find pure symbols.
    4. Find unit symbols.

    >>> c1 = Clause(["A4", "A3", "A5'", "A1", "A3'"])
    >>> c2 = Clause(["A4"])
    >>> c3 = Clause(["A3"])

    >>> f = Formula([c1, c2, c3])
    >>> c, s = generate_parameters(f)

    >>> model = {}
    >>> soln, model = dpll_algorithm(c, s, model)

    >>> print(soln, model)
    True {'A4': True, 'A3': True}
    """
    check_clause_all_true = True
    for clause in clauses:
        clause_check = clause.evaluate(model)
        if clause_check is False:
            return False, None
        elif clause_check is None:
            check_clause_all_true = False
            continue

    if check_clause_all_true:
        return True, model

    pure_symbols, assignment = find_pure_symbols(clauses, symbols, model)
    P = None
    if len(pure_symbols) > 0:
        P, value = pure_symbols[0], assignment[pure_symbols[0]]

    if P:
        tmp_model = model
        tmp_model[P] = value
        tmp_symbols = [i for i in symbols]
        if P in tmp_symbols:
            tmp_symbols.remove(P)
        return dpll_algorithm(clauses, tmp_symbols, tmp_model)

    unit_symbols, assignment = find_unit_clauses(clauses, model)
    P = None
    if len(unit_symbols) > 0:
        P, value = unit_symbols[0], assignment[unit_symbols[0]]
    if P:
        tmp_model = model
        tmp_model[P] = value
        tmp_symbols = [i for i in symbols]
        if P in tmp_symbols:
            tmp_symbols.remove(P)
        return dpll_algorithm(clauses, tmp_symbols, tmp_model)
    P = symbols[0]
    rest = symbols[1:]
    tmp1, tmp2 = model, model
    tmp1[P], tmp2[P] = True, False

    return dpll_algorithm(clauses, rest, tmp1) or dpll_algorithm(clauses, rest, tmp2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    formula = generate_formula()
    print(f"The formula {formula} is", end=" ")

    clauses, symbols = generate_parameters(formula)

    solution, model = dpll_algorithm(clauses, symbols, {})

    if solution:
        print(" satisfiable with the assignment: ")
        print(model)
    else:
        print(" not satisfiable")
