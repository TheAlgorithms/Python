from graphs.two_satisfiability import TwoSatisfiability


def test_satisfiable_basic_case() -> None:
    """Case 1: Basic satisfiable case."""
    two_sat = TwoSatisfiability(5)

    two_sat.add_clause(1, False, 2, False)  # (x1 v x2)
    two_sat.add_clause(3, True, 2, False)  # (¬x3 v x2)
    two_sat.add_clause(4, False, 5, True)  # (x4 v ¬x5)

    two_sat.solve()

    assert two_sat.is_solution_exists(), "Expected solution to exist"
    expected: list[bool] = [False, True, True, True, True, True]
    assert two_sat.get_solutions() == expected


def test_unsatisfiable_contradiction() -> None:
    """Case 2: Unsatisfiable due to direct contradiction."""
    two_sat = TwoSatisfiability(1)

    two_sat.add_clause(1, False, 1, False)  # (x1 v x1)
    two_sat.add_clause(1, True, 1, True)  # (¬x1 v ¬x1)

    two_sat.solve()

    assert not two_sat.is_solution_exists(), "Expected no solution (contradiction)"


def test_single_variable_trivial_satisfiable() -> None:
    """Case 3: Single variable, trivially satisfiable."""
    two_sat = TwoSatisfiability(1)

    two_sat.add_clause(1, False, 1, False)  # (x1 v x1)

    two_sat.solve()

    assert two_sat.is_solution_exists(), "Expected solution to exist"
    expected: list[bool] = [False, True]
    assert two_sat.get_solutions() == expected


def test_chained_dependencies_satisfiable() -> None:
    """Case 4: Larger satisfiable system with dependencies."""
    two_sat = TwoSatisfiability(5)

    two_sat.add_clause(1, False, 2, False)
    two_sat.add_clause(2, True, 3, False)
    two_sat.add_clause(3, True, 4, False)
    two_sat.add_clause(4, True, 5, False)

    two_sat.solve()

    assert two_sat.is_solution_exists(), "Expected solution to exist"
    solution = two_sat.get_solutions()
    for i in range(1, 6):
        assert solution[i], f"Expected x{i} to be True"


def test_unsatisfiable_cycle() -> None:
    """Case 5: Contradiction due to dependency cycle."""
    two_sat = TwoSatisfiability(2)

    two_sat.add_clause(1, False, 2, False)
    two_sat.add_clause(1, True, 2, True)
    two_sat.add_clause(1, False, 2, True)
    two_sat.add_clause(1, True, 2, False)

    two_sat.solve()

    assert not two_sat.is_solution_exists(), (
        "Expected no solution due to contradictory cycle"
    )


def test_cses_case() -> None:
    """Case 6: CSES testcase."""
    two_sat = TwoSatisfiability(2)

    two_sat.add_clause(1, True, 2, False)
    two_sat.add_clause(2, True, 1, False)
    two_sat.add_clause(1, True, 1, True)
    two_sat.add_clause(2, False, 2, False)

    two_sat.solve()

    assert not two_sat.is_solution_exists(), "Expected no solution."
