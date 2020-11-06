"""
Davis–Putnam–Logemann–Loveland (DPLL) algorithm is a complete, backtracking-based search algorithm 
for deciding the satisfiability of propositional logic formulae in conjunctive normal form, i.e. for solving the CNF-SAT problem.

For more information about the algorithm: https://en.wikipedia.org/wiki/DPLL_algorithm
"""

import random


class Clause():
    """
    A clause represented in CNF.
    A clause is a set of literals, either complemented or otherwise.
    For example:
        {A1, A2, A3'} is the clause (A1 v A2 v A3')
        {A5', A2', A1} is the clause (A5' v A2' v A1) 
    """

    def __init__(self, no_of_literals, literals):
        """
        Represent the number of literals, the literals themselves, and an assignment in a clause."
        """
        self.no_of_literals = no_of_literals
        self.literals = [l for l in literals]
        self.literal_values = dict()
        for l in self.literals:
            self.literal_values[l] = None    # Assign all literals to None initially
    
    def __str__(self):
        """
        To print a clause as in CNF. 
        Variable clause holds the string representation. 
        """
        clause = "{ "
        for i in range(0, self.no_of_literals):
            clause += (self.literals[i] + " ")
            if i != self.no_of_literals - 1:
                clause += ", "
        clause += "}"
        
        return clause
    
    def assign(self, model):
        """
        Assign values to literals of the clause as given by model.
        """
        i = 0
        while i < self.no_of_literals:
            symbol = self.literals[i][:2]
            if symbol in model.keys():
                val = model[symbol]
            else:
                 i += 1
                 continue
            if val != None:
                if self.literals[i][-1] == "'":
                    val = not val                  #Complement assignment if literal is in complemented form
            self.literal_values[self.literals[i]] = val
            i += 1
    
    def evaluate(self, model):
        """
        Evaluates the clause till the extent possible with the current assignments in model.
        This has the following steps:
        1. Return True if both a literal and its complement exist in the clause.
        2. Return True if a single literal has the assignment True.
        3. Return None(unable to complete evaluation) if a literal has no assignment.
        4. Compute disjunction of all values assigned in clause.
        """
        for l in self.literals:
            if len(l) == 2:
                symbol = l + "'"
                if symbol in self.literals:
                    return True
            else:
                symbol = l[:2]
                if symbol in self.literals:
                    return True 

        self.assign(model)
        result = False
        for j in self.literal_values.values():
            if j == True:
                return True
            elif j == None:
                return None
        for j in self.literal_values.values():
            result = result or j
        return result

class Formula():
    """
    A formula represented in CNF.
    A formula is a set of clauses.
    For example,
        {{A1, A2, A3'}, {A5', A2', A1}} is the formula ((A1 v A2 v A3') and (A5' v A2' v A1))
    """
    def __init__(self, no_of_clauses, clauses):
        """
        Represent the number of clauses and the clauses themselves.
        """
        self.no_of_clauses = no_of_clauses
        self.clauses = [c for c in clauses]
    
    def __str__(self):
        """
        To print a formula as in CNF. 
        Variable formula holds the string representation. 
        """
        formula = "{ "
        for i in range(0, self.no_of_clauses):
            formula += (str(self.clauses[i]) + " ")
            if i != self.no_of_clauses - 1:
                formula += ", "
        formula += "}"
        
        return formula

def generate_clause():
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
        var_name = base_var+str(var_no)
        var_complement = random.randint(0, 1)
        if var_complement == 1:
            var_name += "'"
        if var_name in literals:
            i -= 1
        else:
            literals.append(var_name)
        i+=1
    clause = Clause(no_of_literals, literals)
    return clause

def generate_formula():
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
    formula = Formula(no_of_clauses, clauses)
    return formula

def generate_parameters(formula):
    """
    Return the clauses and symbols from a formula.
    A symbol is the uncomplemented form of a literal.
    For example,
        Symbol of A3 is A3.
        Symbol of A5' is A5.

    """
    clauses = formula.clauses
    symbols_set = []
    for clause in formula.clauses:
        for literal in clause.literals:
            symbol = literal[:2]
            if symbol not in symbols_set:
             symbols_set.append(symbol)
    return clauses, symbols_set

def find_pure_symbols(clauses, symbols, model):
    """
    Return pure symbols and their assignments to satisfy the clause, if figurable.
    Pure symbols are symbols in a formula that exist only in one form, either complemented or otherwise.
    For example,
        { { A4 , A3 , A5' , A1 , A3' } , { A4 } , { A3 } } has the pure symbols A4, A5' and A1.
    This has the following steps:
    1. Ignore clauses that have already evaluated to be True. 
    2. Find symbols that occur only in one form in the rest of the clauses.
    3. Assign value True or False depending on whether the symbols occurs in normal or complemented form respectively.
    """
    pure_symbols = []
    assignment = dict()
    literals = []
    
    for clause in clauses:
        if clause.evaluate(model) == True:
            continue
        for l in clause.literals:
            literals.append(l)

    for s in symbols:
        sym = (s + "'")
        if (s in literals and sym not in literals) or (s not in literals and sym in literals):
            pure_symbols.append(s)
    for p in pure_symbols:
        assignment[p] = None
    for s in pure_symbols:
        sym = (s + "'")
        if s in literals:
            assignment[s] = True
        elif sym in literals:
            assignment[s] = False
    return pure_symbols, assignment

def find_unit_clauses(clauses, model):
    """
    Returns the unit symbols and their assignments to satisfy the clause, if figurable.
    Unit symbols are symbols in a formula that are:
        - Either the only symbol in a clause
        - Or all other literals in that clause have been assigned False
    This has the following steps:
    1. Find symbols that are the only occurences in a clause.
    2. Find symbols in a clause where all other literals are assigned to be False.
    3. Assign True or False depending on whether the symbols occurs in normal or complemented form respectively.
    """
    unit_symbols = []
    for clause in clauses:
        if clause.no_of_literals == 1:
            unit_symbols.append(clause.literals[0])
        else:
            Fcount, Ncount = 0, 0
            for l,v in clause.literal_values.items():
                if v == False:
                    Fcount += 1
                elif v == None:
                    sym = l
                    Ncount += 1
            if Fcount == clause.no_of_literals - 1 and Ncount == 1:
                unit.append(sym)
    assignment = dict()
    for i in unit_symbols:
        symbol = i[:2]
        if len(i) == 2:
            assignment[symbol] = True
        else:
            assignment[symbol] = False
    unit_symbols = [i[:2] for i in unit_symbols]

    return unit_symbols, assignment

def DPLL(clauses, symbols, model):
    """
    Returns the model if the formula is satisfiable, else None
    This has the following steps:
    1. If every clause in clauses is True, return True.
    2. If some clause in clauses is False, return False.
    3. Find pure symbols.
    4. Find unit symbols.
    """
    check_clause_all_true = True
    for clause in clauses:
        clause_check = clause.evaluate(model)
        if clause_check == False:
            return False, None
        elif clause_check == None:
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
        return DPLL(clauses, tmp_symbols, tmp_model)
    
    unit_symbols, assignment =  find_unit_clauses(clauses, model)
    P = None
    if len(unit_symbols) > 0:
        P, value = unit_symbols[0], assignment[unit_symbols[0]]
    if P:
        tmp_model = model
        tmp_model[P]=value
        tmp_symbols = [i for i in symbols]
        if P in tmp_symbols:
            tmp_symbols.remove(P)
        return DPLL(clauses, tmp_symbols, tmp_model)
    P = symbols[0]
    rest = symbols[1:]
    tmp1, tmp2 = model, model
    tmp1[P], tmp2[P] = True, False

    return DPLL(clauses, rest, tmp1) or DPLL(clauses, rest, tmp2)

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    formula = generate_formula()
    print(formula)

    clauses, symbols = generate_parameters(formula)

    solution, model = DPLL(clauses, symbols, {})

    if solution:
        print(model)
    else:
        print("Not satisfiable")