#!/usr/bin/env python3

"""
Davis-Putnam-Logemann-Loveland (DPLL) algorithm is a complete, backtracking-based
search algorithm for deciding the satisfiability of propositional logic formulae in
conjunctive normal form, i.e, for solving the Conjunctive Normal Form SATisfiability
(CNF-SAT) problem.

For more information about the algorithm: https://en.wikipedia.org/wiki/DPLL_algorithm
"""

from __future__ import annotations

import random
from collections.abc import Iterable


class Clause:
    """
    A clause represented in Conjunctive Normal Form.
    A clause is a set of literals, either complemented or otherwise.
    For example:
        {A1, A2, A3'} is the clause (A1 v A2 v A3')
        {A5', A2', A1} is the clause (A5' v A2' v A1)

    Create model
    >>> clause = Clause(["A1", "A2'", "A3"])
    >>> clause.evaluate({"A1": True})
    True
    """

    def __init__(self, literals: list[str]) -> None:
        """
        Represent the literals and an assignment in a clause."
        """
        # Assign all literals to None initially
        self.literals: dict[str, bool | None] = {literal: None for literal in literals}

    def __str__(self) -> str:
        """
        To print a clause as in Conjunctive Normal Form.
        >>> str(Clause(["A1", "A2'", "A3"]))
        "{A1 , A2' , A3}"
        """
        return "{" + " , ".join(self.literals) + "}"

    def __len__(self) -> int:
        """
        To print a clause as in Conjunctive Normal Form.
        >>> len(Clause([]))
        0
        >>> len(Clause(["A1", "A2'", "A3"]))
        3
        """
        return len(self.literals)

    def assign(self, model: dict[str, bool | None]) -> None:
        """
        Assign values to literals of the clause as given by model.
        """
        for literal in self.literals:
            symbol = literal[:2]
            if symbol in model:
                value = model[symbol]
            else:
                continue
            # Complement assignment if literal is in complemented form
            if value is not None and literal.endswith("'"):
                value = not value
            self.literals[literal] = value

    def evaluate(self, model: dict[str, bool | None]) -> bool | None:
        """
        Evaluates the clause with the assignments in model.
        This has the following steps:
        1. Return True if both a literal and its complement exist in the clause.
        2. Return True if a single literal has the assignment True.
        3. Return None(unable to complete evaluation) if a literal has no assignment.
        4. Compute disjunction of all values assigned in clause.
        """
        for literal in self.literals:
            symbol = literal.rstrip("'") if literal.endswith("'") else literal + "'"
            if symbol in self.literals:
                return True

        self.assign(model)
        for value in self.literals.values():
            if value in (True, None):
                return value
        return any(self.literals.values())


class Formula:
    """
    A formula represented in Conjunctive Normal Form.
    A formula is a set of clauses.
    For example,
        {{A1, A2, A3'}, {A5', A2', A1}} is ((A1 v A2 v A3') and (A5' v A2' v A1))
    """

    def __init__(self, clauses: Iterable[Clause]) -> None:
        """
        Represent the number of clauses and the clauses themselves.
        """
        self.clauses = list(clauses)

    def __str__(self) -> str:
        """
        To print a formula as in Conjunctive Normal Form.
        str(Formula([Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])]))
        "{{A1 , A2' , A3} , {A5' , A2' , A1}}"
        """
        return "{" + " , ".join(str(clause) for clause in self.clauses) + "}"


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
    clauses: set[Clause] = set()
    no_of_clauses = random.randint(1, 10)
    while len(clauses) < no_of_clauses:
        clauses.add(generate_clause())
    return Formula(clauses)


def generate_parameters(formula: Formula) -> tuple[list[Clause], list[str]]:
    """
    Return the clauses and symbols from a formula.
    A symbol is the uncomplemented form of a literal.
    For example,
        Symbol of A3 is A3.
        Symbol of A5' is A5.

    >>> formula = Formula([Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])])
    >>> clauses, symbols = generate_parameters(formula)
    >>> clauses_list = [str(i) for i in clauses]
    >>> clauses_list
    ["{A1 , A2' , A3}", "{A5' , A2' , A1}"]
    >>> symbols
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
    clauses: list[Clause], symbols: list[str], model: dict[str, bool | None]
) -> tuple[list[str], dict[str, bool | None]]:
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

    >>> formula = Formula([Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])])
    >>> clauses, symbols = generate_parameters(formula)

    >>> pure_symbols, values = find_pure_symbols(clauses, symbols, {})
    >>> pure_symbols
    ['A1', 'A2', 'A3', 'A5']
    >>> values
    {'A1': True, 'A2': False, 'A3': True, 'A5': False}
    """
    pure_symbols = []
    assignment: dict[str, bool | None] = {}
    literals = []

    for clause in clauses:
        if clause.evaluate(model):
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
    clauses: list[Clause],
    model: dict[str, bool | None],  # noqa: ARG001
) -> tuple[list[str], dict[str, bool | None]]:
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
    >>> clauses, symbols = generate_parameters(Formula([clause1, clause2, clause3]))

    >>> unit_clauses, values = find_unit_clauses(clauses, {})
    >>> unit_clauses
    ['A4', 'A3']
    >>> values
    {'A4': True, 'A3': True}
    """
    unit_symbols = []
    for clause in clauses:
        if len(clause) == 1:
            unit_symbols.append(next(iter(clause.literals.keys())))
        else:
            f_count, n_count = 0, 0
            for literal, value in clause.literals.items():
                if value is False:
                    f_count += 1
                elif value is None:
                    sym = literal
                    n_count += 1
            if f_count == len(clause) - 1 and n_count == 1:
                unit_symbols.append(sym)
    assignment: dict[str, bool | None] = {}
    for i in unit_symbols:
        symbol = i[:2]
        assignment[symbol] = len(i) == 2
    unit_symbols = [i[:2] for i in unit_symbols]

    return unit_symbols, assignment


def dpll_algorithm(
    clauses: list[Clause], symbols: list[str], model: dict[str, bool | None]
) -> tuple[bool | None, dict[str, bool | None] | None]:
    """
    Returns the model if the formula is satisfiable, else None
    This has the following steps:
    1. If every clause in clauses is True, return True.
    2. If some clause in clauses is False, return False.
    3. Find pure symbols.
    4. Find unit symbols.

    >>> formula = Formula([Clause(["A4", "A3", "A5'", "A1", "A3'"]), Clause(["A4"])])
    >>> clauses, symbols = generate_parameters(formula)

    >>> soln, model = dpll_algorithm(clauses, symbols, {})
    >>> soln
    True
    >>> model
    {'A4': True}
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

    try:
        pure_symbols, assignment = find_pure_symbols(clauses, symbols, model)
    except RecursionError:
        print("raises a RecursionError and is")
        return None, {}
    p = None
    if len(pure_symbols) > 0:
        p, value = pure_symbols[0], assignment[pure_symbols[0]]

    if p:
        tmp_model = model
        tmp_model[p] = value
        tmp_symbols = list(symbols)
        if p in tmp_symbols:
            tmp_symbols.remove(p)
        return dpll_algorithm(clauses, tmp_symbols, tmp_model)

    unit_symbols, assignment = find_unit_clauses(clauses, model)
    p = None
    if len(unit_symbols) > 0:
        p, value = unit_symbols[0], assignment[unit_symbols[0]]
    if p:
        tmp_model = model
        tmp_model[p] = value
        tmp_symbols = list(symbols)
        if p in tmp_symbols:
            tmp_symbols.remove(p)
        return dpll_algorithm(clauses, tmp_symbols, tmp_model)
    p = symbols[0]
    rest = symbols[1:]
    tmp1, tmp2 = model, model
    tmp1[p], tmp2[p] = True, False

    return dpll_algorithm(clauses, rest, tmp1) or dpll_algorithm(clauses, rest, tmp2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    formula = generate_formula()
    print(f"The formula {formula} is", end=" ")

    clauses, symbols = generate_parameters(formula)
    solution, model = dpll_algorithm(clauses, symbols, {})

    if solution:
        print(f"satisfiable with the assignment {model}.")
    else:
        print("not satisfiable.")
