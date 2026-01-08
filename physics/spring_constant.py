"""
Comprehensive test suite for corrected Hooke's Law implementation
"""
import math


def spring_constant(force: float, displacement: float) -> float:
    if displacement == 0:
        raise ValueError("Displacement cannot be zero")
    return -force / displacement


def spring_force(spring_constant: float, displacement: float) -> float:
    if spring_constant < 0:
        raise ValueError("Spring constant must be positive")
    return -spring_constant * displacement


def spring_displacement(spring_constant: float, force: float) -> float:
    if spring_constant <= 0:
        raise ValueError("Spring constant must be positive")
    return -force / spring_constant


# ============================================================================
# COMPREHENSIVE TEST SUITE
# ============================================================================

def test_spring_constant():
    """Test spring_constant function comprehensively"""
    print("=" * 80)
    print("TESTING: spring_constant()")
    print("=" * 80)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Negative force, positive displacement (spring stretched right, pulls left)
    print("\n✓ Test 1: Spring stretched right (+x), restoring force left (-F)")
    result = spring_constant(-10, 0.5)
    expected = 20.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_constant(-10, 0.5) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 2: Positive force, negative displacement (spring compressed left, pushes right)
    print("\n✓ Test 2: Spring compressed left (-x), restoring force right (+F)")
    result = spring_constant(10, -0.5)
    expected = 20.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_constant(10, -0.5) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 3: Different spring constant
    print("\n✓ Test 3: Different spring constant")
    result = spring_constant(-5.5, 0.25)
    expected = 22.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_constant(-5.5, 0.25) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 4: Larger values
    print("\n✓ Test 4: Larger values")
    result = spring_constant(-100, 2.0)
    expected = 50.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_constant(-100, 2.0) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 5: Opposite direction
    print("\n✓ Test 5: Opposite direction")
    result = spring_constant(100, -2.0)
    expected = 50.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_constant(100, -2.0) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 6: Zero force
    print("\n✓ Test 6: Zero force (equilibrium)")
    result = spring_constant(0, 1.0)
    expected = 0.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_constant(0, 1.0) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 7: Zero displacement (should raise error)
    print("\n✓ Test 7: Zero displacement - should raise ValueError")
    try:
        result = spring_constant(10, 0)
        print(f"  ✗ FAIL:  Should have raised ValueError, got {result}")
        tests_failed += 1
    except ValueError as e:
        print(f"  Correctly raised ValueError: '{e}' ✓")
        tests_passed += 1
    
    # Test 8: Very small values
    print("\n✓ Test 8: Very small values")
    result = spring_constant(-0.001, 0.0001)
    expected = 10.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_constant(-0.001, 0.0001) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 9: Very large values
    print("\n✓ Test 9: Very large values")
    result = spring_constant(-1000000, 10000)
    expected = 100.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_constant(-1000000, 10000) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    print(f"\n{'─' * 80}")
    print(f"spring_constant() Results: {tests_passed} passed, {tests_failed} failed")
    return tests_passed, tests_failed


def test_spring_force():
    """Test spring_force function comprehensively"""
    print("\n" + "=" * 80)
    print("TESTING:  spring_force()")
    print("=" * 80)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Positive displacement (spring stretched right, force pulls left)
    print("\n✓ Test 1: Spring stretched right, force pulls left")
    result = spring_force(20, 0.5)
    expected = -10.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_force(20, 0.5) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 2: Negative displacement (spring compressed left, force pushes right)
    print("\n✓ Test 2: Spring compressed left, force pushes right")
    result = spring_force(20, -0.5)
    expected = 10.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_force(20, -0.5) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 3: Different spring constant
    print("\n✓ Test 3: Different spring constant")
    result = spring_force(22, 0.25)
    expected = -5.5
    if abs(result - expected) < 1e-10:
        print(f"  spring_force(22, 0.25) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL:  Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 4: Larger values
    print("\n✓ Test 4: Larger values")
    result = spring_force(50, 2.0)
    expected = -100.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_force(50, 2.0) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 5: Larger values, opposite direction
    print("\n✓ Test 5: Larger values, opposite direction")
    result = spring_force(50, -2.0)
    expected = 100.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_force(50, -2.0) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 6: Zero displacement (equilibrium)
    print("\n✓ Test 6: Zero displacement (equilibrium)")
    result = spring_force(10, 0)
    expected = -0.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_force(10, 0) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 7: Negative spring constant (should raise error)
    print("\n✓ Test 7: Negative spring constant - should raise ValueError")
    try:
        result = spring_force(-10, 0.5)
        print(f"  ✗ FAIL: Should have raised ValueError, got {result}")
        tests_failed += 1
    except ValueError as e:
        print(f"  Correctly raised ValueError:  '{e}' ✓")
        tests_passed += 1
    
    # Test 8: Very stiff spring
    print("\n✓ Test 8: Very stiff spring")
    result = spring_force(1000, 0.01)
    expected = -10.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_force(1000, 0.01) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 9: Very soft spring
    print("\n✓ Test 9: Very soft spring")
    result = spring_force(0.1, 100)
    expected = -10.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_force(0.1, 100) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    print(f"\n{'─' * 80}")
    print(f"spring_force() Results: {tests_passed} passed, {tests_failed} failed")
    return tests_passed, tests_failed


def test_spring_displacement():
    """Test spring_displacement function comprehensively"""
    print("\n" + "=" * 80)
    print("TESTING: spring_displacement()")
    print("=" * 80)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Negative restoring force (spring pulls left, displaced right)
    print("\n✓ Test 1: Restoring force left (-F), displacement right (+x)")
    result = spring_displacement(20, -10)
    expected = 0.5
    if abs(result - expected) < 1e-10:
        print(f"  spring_displacement(20, -10) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 2: Positive restoring force (spring pushes right, displaced left)
    print("\n✓ Test 2: Restoring force right (+F), displacement left (-x)")
    result = spring_displacement(20, 10)
    expected = -0.5
    if abs(result - expected) < 1e-10:
        print(f"  spring_displacement(20, 10) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 3: Different spring constant
    print("\n✓ Test 3: Different spring constant")
    result = spring_displacement(22, -5.5)
    expected = 0.25
    if abs(result - expected) < 1e-10:
        print(f"  spring_displacement(22, -5.5) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 4: Larger values
    print("\n✓ Test 4: Larger values")
    result = spring_displacement(50, -100)
    expected = 2.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_displacement(50, -100) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL:  Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 5: Larger values, opposite direction
    print("\n✓ Test 5: Larger values, opposite direction")
    result = spring_displacement(50, 100)
    expected = -2.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_displacement(50, 100) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 6: Zero force (equilibrium)
    print("\n✓ Test 6: Zero force (equilibrium)")
    result = spring_displacement(10, 0)
    expected = -0.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_displacement(10, 0) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 7: Zero spring constant (should raise error)
    print("\n✓ Test 7: Zero spring constant - should raise ValueError")
    try:
        result = spring_displacement(0, 10)
        print(f"  ✗ FAIL: Should have raised ValueError, got {result}")
        tests_failed += 1
    except ValueError as e: 
        print(f"  Correctly raised ValueError: '{e}' ✓")
        tests_passed += 1
    
    # Test 8: Negative spring constant (should raise error)
    print("\n✓ Test 8: Negative spring constant - should raise ValueError")
    try:
        result = spring_displacement(-10, 5)
        print(f"  ✗ FAIL: Should have raised ValueError, got {result}")
        tests_failed += 1
    except ValueError as e: 
        print(f"  Correctly raised ValueError: '{e}' ✓")
        tests_passed += 1
    
    # Test 9: Very stiff spring
    print("\n✓ Test 9: Very stiff spring (small displacement)")
    result = spring_displacement(10000, -100)
    expected = 0.01
    if abs(result - expected) < 1e-10:
        print(f"  spring_displacement(10000, -100) = {result} ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    # Test 10: Very soft spring
    print("\n✓ Test 10: Very soft spring (large displacement)")
    result = spring_displacement(0.01, -1)
    expected = 100.0
    if abs(result - expected) < 1e-10:
        print(f"  spring_displacement(0.01, -1) = {result} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Expected {expected}, got {result}")
        tests_failed += 1
    
    print(f"\n{'─' * 80}")
    print(f"spring_displacement() Results: {tests_passed} passed, {tests_failed} failed")
    return tests_passed, tests_failed


def test_consistency():
    """Test mathematical consistency between all three functions"""
    print("\n" + "=" * 80)
    print("TESTING:  MATHEMATICAL CONSISTENCY")
    print("=" * 80)
    
    tests_passed = 0
    tests_failed = 0
    
    # Consistency Test 1: Round-trip through all three functions
    print("\n✓ Consistency Test 1: Round-trip calculation")
    print("  Starting values: k=20 N/m, x=0.5 m")
    
    k_original = 20
    x_original = 0.5
    
    # Step 1: Calculate force from k and x
    F = spring_force(k_original, x_original)
    print(f"  Step 1: spring_force({k_original}, {x_original}) = {F} N")
    
    # Step 2: Calculate k from F and x
    k_recovered = spring_constant(F, x_original)
    print(f"  Step 2: spring_constant({F}, {x_original}) = {k_recovered} N/m")
    
    # Step 3: Calculate x from k and F
    x_recovered = spring_displacement(k_original, F)
    print(f"  Step 3: spring_displacement({k_original}, {F}) = {x_recovered} m")
    
    # Verify consistency
    if abs(k_recovered - k_original) < 1e-10 and abs(x_recovered - x_original) < 1e-10:
        print(f"  ✓ CONSISTENT: k={k_original}→{k_recovered}, x={x_original}→{x_recovered}")
        tests_passed += 1
    else:
        print(f"  ✗ INCONSISTENT!")
        tests_failed += 1
    
    # Consistency Test 2: Another round-trip with different values
    print("\n✓ Consistency Test 2: Round-trip with negative displacement")
    print("  Starting values: k=50 N/m, x=-1.0 m")
    
    k_original = 50
    x_original = -1.0
    
    F = spring_force(k_original, x_original)
    print(f"  Step 1: spring_force({k_original}, {x_original}) = {F} N")
    
    k_recovered = spring_constant(F, x_original)
    print(f"  Step 2: spring_constant({F}, {x_original}) = {k_recovered} N/m")
    
    x_recovered = spring_displacement(k_original, F)
    print(f"  Step 3: spring_displacement({k_original}, {F}) = {x_recovered} m")
    
    if abs(k_recovered - k_original) < 1e-10 and abs(x_recovered - x_original) < 1e-10:
        print(f"  ✓ CONSISTENT: k={k_original}→{k_recovered}, x={x_original}→{x_recovered}")
        tests_passed += 1
    else: 
        print(f"  ✗ INCONSISTENT!")
        tests_failed += 1
    
    # Consistency Test 3: Verify F = -kx relationship
    print("\n✓ Consistency Test 3: Verify F = -kx directly")
    k = 30
    x = 0.75
    F_calculated = spring_force(k, x)
    F_expected = -k * x
    
    if abs(F_calculated - F_expected) < 1e-10:
        print(f"  spring_force({k}, {x}) = {F_calculated}")
        print(f"  Direct calculation: -({k}) * {x} = {F_expected}")
        print(f"  ✓ MATCH!")
        tests_passed += 1
    else:
        print(f"  ✗ MISMATCH!")
        tests_failed += 1
    
    # Consistency Test 4: Verify k = -F/x relationship
    print("\n✓ Consistency Test 4: Verify k = -F/x directly")
    F = -15
    x = 0.5
    k_calculated = spring_constant(F, x)
    k_expected = -F / x
    
    if abs(k_calculated - k_expected) < 1e-10:
        print(f"  spring_constant({F}, {x}) = {k_calculated}")
        print(f"  Direct calculation: -({F}) / {x} = {k_expected}")
        print(f"  ✓ MATCH!")
        tests_passed += 1
    else:
        print(f"  ✗ MISMATCH!")
        tests_failed += 1
    
    # Consistency Test 5: Verify x = -F/k relationship
    print("\n✓ Consistency Test 5: Verify x = -F/k directly")
    k = 25
    F = -12.5
    x_calculated = spring_displacement(k, F)
    x_expected = -F / k
    
    if abs(x_calculated - x_expected) < 1e-10:
        print(f"  spring_displacement({k}, {F}) = {x_calculated}")
        print(f"  Direct calculation: -({F}) / {k} = {x_expected}")
        print(f"  ✓ MATCH!")
        tests_passed += 1
    else:
        print(f"  ✗ MISMATCH!")
        tests_failed += 1
    
    print(f"\n{'─' * 80}")
    print(f"Consistency Tests Results: {tests_passed} passed, {tests_failed} failed")
    return tests_passed, tests_failed


def test_physics_principles():
    """Test that the code follows correct physics principles"""
    print("\n" + "=" * 80)
    print("TESTING:  PHYSICS PRINCIPLES")
    print("=" * 80)
    
    tests_passed = 0
    tests_failed = 0
    
    # Physics Test 1: Restoring force opposes displacement
    print("\n✓ Physics Test 1: Restoring force opposes displacement")
    
    # Case 1a: Positive displacement should give negative force
    k = 20
    x_positive = 0.5
    F = spring_force(k, x_positive)
    if F < 0:
        print(f"  Displacement = +{x_positive} m → Force = {F} N ✓")
        print(f"  (Spring stretched right, pulls left)")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL:  Positive displacement should give negative force")
        tests_failed += 1
    
    # Case 1b:  Negative displacement should give positive force
    x_negative = -0.5
    F = spring_force(k, x_negative)
    if F > 0:
        print(f"  Displacement = {x_negative} m → Force = {F} N ✓")
        print(f"  (Spring compressed left, pushes right)")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Negative displacement should give positive force")
        tests_failed += 1
    
    # Physics Test 2: Spring constant is always positive
    print("\n✓ Physics Test 2: Spring constant is always positive")
    
    test_cases = [
        (-10, 0.5),   # Force left, displacement right
        (10, -0.5),   # Force right, displacement left
        (-100, 2.0),  # Larger values
        (50, -1.0),   # Different ratio
    ]
    
    all_positive = True
    for F, x in test_cases: 
        k = spring_constant(F, x)
        if k >= 0:
            print(f"  spring_constant({F}, {x}) = {k} N/m ✓")
        else:
            print(f"  ✗ FAIL: spring_constant({F}, {x}) = {k} (should be positive)")
            all_positive = False
    
    if all_positive:
        tests_passed += 1
    else:
        tests_failed += 1
    
    # Physics Test 3: Equilibrium position (x=0) has zero force
    print("\n✓ Physics Test 3: Zero displacement → Zero force")
    F = spring_force(20, 0)
    if abs(F) < 1e-10:
        print(f"  spring_force(20, 0) = {F} N ✓")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Expected 0, got {F}")
        tests_failed += 1
    
    # Physics Test 4: Linear relationship (double displacement = double force)
    print("\n✓ Physics Test 4: Linear relationship (Hooke's Law is linear)")
    k = 30
    x1 = 0.4
    x2 = 0.8  # Double the displacement
    
    F1 = spring_force(k, x1)
    F2 = spring_force(k, x2)
    
    if abs(F2 - 2 * F1) < 1e-10:
        print(f"  Displacement {x1} m → Force {F1} N")
        print(f"  Displacement {x2} m → Force {F2} N")
        print(f"  Ratio: {F2/F1:.2f} (expected 2.00) ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Not linear!  {F2} ≠ 2 × {F1}")
        tests_failed += 1
    
    # Physics Test 5: Stiffer spring requires more force for same displacement
    print("\n✓ Physics Test 5: Stiffer spring → More force for same displacement")
    k_soft = 10
    k_stiff = 100
    x = 0.3
    
    F_soft = abs(spring_force(k_soft, x))
    F_stiff = abs(spring_force(k_stiff, x))
    
    if F_stiff > F_soft:
        print(f"  Soft spring (k={k_soft}): |F| = {F_soft} N")
        print(f"  Stiff spring (k={k_stiff}): |F| = {F_stiff} N ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL: Stiff spring should have larger force")
        tests_failed += 1
    
    print(f"\n{'─' * 80}")
    print(f"Physics Tests Results: {tests_passed} passed, {tests_failed} failed")
    return tests_passed, tests_failed


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("\n" + "=" * 80)
    print("TESTING: EDGE CASES")
    print("=" * 80)
    
    tests_passed = 0
    tests_failed = 0
    
    # Edge Case 1: Very large values
    print("\n✓ Edge Case 1: Very large values")
    try:
        k = spring_constant(-1e10, 1e5)
        F = spring_force(1e8, 1e6)
        x = spring_displacement(1e12, -1e9)
        print(f"  Large k calculation: {k}")
        print(f"  Large F calculation: {F}")
        print(f"  Large x calculation: {x}")
        print(f"  ✓ Handles large values")
        tests_passed += 1
    except Exception as e: 
        print(f"  ✗ FAIL: {e}")
        tests_failed += 1
    
    # Edge Case 2: Very small values
    print("\n✓ Edge Case 2: Very small values")
    try:
        k = spring_constant(-1e-10, 1e-15)
        F = spring_force(1e-8, 1e-12)
        x = spring_displacement(1e-6, -1e-9)
        print(f"  Small k calculation: {k}")
        print(f"  Small F calculation:  {F}")
        print(f"  Small x calculation: {x}")
        print(f"  ✓ Handles small values")
        tests_passed += 1
    except Exception as e: 
        print(f"  ✗ FAIL: {e}")
        tests_failed += 1
    
    # Edge Case 3: Floating point precision
    print("\n✓ Edge Case 3: Floating point precision")
    k = spring_constant(-1/3, 0.1)
    expected = (1/3) / 0.1
    if abs(k - expected) < 1e-10:
        print(f"  spring_constant(-1/3, 0.1) = {k}")
        print(f"  Expected: {expected} ✓")
        tests_passed += 1
    else: 
        print(f"  ✗ FAIL:  Precision issue")
        tests_failed += 1
    
    # Edge Case 4: Symmetry test
    print("\n✓ Edge Case 4: Symmetry (opposite signs should give same k)")
    k1 = spring_constant(-10, 0.5)
    k2 = spring_constant(10, -0.5)
    if abs(k1 - k2) < 1e-10:
        print(f"  spring_constant(-10, 0.5) = {k1}")
        print(f"  spring_constant(10, -0.5) = {k2}")
        print(f"  ✓ Symmetric!")
        tests_passed += 1
    else:
        print(f"  ✗ FAIL: Not symmetric")
        tests_failed += 1
    
    # Edge Case 5: All error conditions
    print("\n✓ Edge Case 5: All error conditions caught")
    error_tests = [
        (lambda: spring_constant(10, 0), "Displacement cannot be zero"),
        (lambda: spring_force(-10, 0.5), "Spring constant must be positive"),
        (lambda: spring_displacement(0, 10), "Spring constant must be positive"),
        (lambda: spring_displacement(-5, 10), "Spring constant must be positive"),
    ]
    
    all_errors_caught = True
    for test_func, expected_msg in error_tests: 
        try:
            test_func()
            print(f"  ✗ FAIL: Should have raised ValueError")
            all_errors_caught = False
        except ValueError as e: 
            if expected_msg in str(e):
                print(f"  ✓ Correctly raised:  '{e}'")
            else:
                print(f"  ✗ Wrong error message: '{e}'")
                all_errors_caught = False
    
    if all_errors_caught:
        tests_passed += 1
    else:
        tests_failed += 1
    
    print(f"\n{'─' * 80}")
    print(f"Edge Cases Results: {tests_passed} passed, {tests_failed} failed")
    return tests_passed, tests_failed


def run_doctests():
    """Run the built-in doctests"""
    print("\n" + "=" * 80)
    print("TESTING: DOCTESTS")
    print("=" * 80)
    
    import doctest
    
    # Create a fake module with our functions and their docstrings
    test_module = type('module', (), {
        'spring_constant': spring_constant,
        'spring_force': spring_force,
        'spring_displacement': spring_displacement,
    })()
    
    # Copy docstrings from the original code
    spring_constant.__doc__ = """
    Calculate spring constant (k) using Hooke's Law:  k = -F/x
    
    >>> spring_constant(-10, 0.5)
    20.0
    >>> spring_constant(10, -0.5)
    20.0
    >>> spring_constant(-5.5, 0.25)
    22.0
    >>> spring_constant(-100, 2.0)
    50.0
    >>> spring_constant(100, -2.0)
    50.0
    >>> spring_constant(0, 1.0)
    0.0
    """
    
    spring_force.__doc__ = """
    Calculate restoring force exerted by a spring using Hooke's Law:  F = -kx
    
    >>> spring_force(20, 0.5)
    -10.0
    >>> spring_force(20, -0.5)
    10.0
    >>> spring_force(22, 0.25)
    -5.5
    >>> spring_force(50, 2.0)
    -100.0
    >>> spring_force(50, -2.0)
    100.0
    >>> spring_force(10, 0)
    -0.0
    """
    
    spring_displacement.__doc__ = """
    Calculate displacement of a spring using Hooke's Law: x = -F/k
    
    >>> spring_displacement(20, -10)
    0.5
    >>> spring_displacement(20, 10)
    -0.5
    >>> spring_displacement(22, -5.5)
    0.25
    >>> spring_displacement(50, -100)
    2.0
    >>> spring_displacement(50, 100)
    -2.0
    >>> spring_displacement(10, 0)
    -0.0
    """
    
    print("\nRunning doctests for spring_constant()...")
    result1 = doctest.testmod(m=test_module, verbose=False, extraglobs={'spring_constant': spring_constant})
    
    print(f"\nRunning doctests for spring_force()...")
    result2 = doctest.testmod(m=test_module, verbose=False, extraglobs={'spring_force': spring_force})
    
    print(f"\nRunning doctests for spring_displacement()...")
    result3 = doctest.testmod(m=test_module, verbose=False, extraglobs={'spring_displacement': spring_displacement})
    
    total_tests = result1.attempted + result2.attempted + result3.attempted
    total_failures = result1.failed + result2.failed + result3.failed
    total_passed = total_tests - total_failures
    
    print(f"\n{'─' * 80}")
    print(f"Doctests Results: {total_passed} passed, {total_failures} failed out of {total_tests} tests")
    
    return total_passed, total_failures


# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

if __name__ == "__main__": 
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "  COMPREHENSIVE TEST SUITE FOR CORRECTED HOOKE'S LAW IMPLEMENTATION". center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")
    
    total_passed = 0
    total_failed = 0
    
    try:
        # Run all test suites
        p, f = test_spring_constant()
        total_passed += p
        total_failed += f
        
        p, f = test_spring_force()
        total_passed += p
        total_failed += f
        
        p, f = test_spring_displacement()
        total_passed += p
        total_failed += f
        
        p, f = test_consistency()
        total_passed += p
        total_failed += f
        
        p, f = test_physics_principles()
        total_passed += p
        total_failed += f
        
        p, f = test_edge_cases()
        total_passed += p
        total_failed += f
        
        p, f = run_doctests()
        total_passed += p
        total_failed += f
        
        # Final summary
        print("\n")
        print("╔" + "=" * 78 + "╗")
        print("║" + " " * 78 + "║")
        print("║" + "FINAL TEST SUMMARY".center(78) + "║")
        print("║" + " " * 78 + "║")
        print("╚" + "=" * 78 + "╝")
        
        total_tests = total_passed + total_failed
        pass_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n  Total Tests Run: {total_tests}")
        print(f"  ✓ Passed: {total_passed}")
        print(f"  ✗ Failed: {total_failed}")
        print(f"  Pass Rate: {pass_rate:.1f}%")
        
        if total_failed == 0:
            print("\n  🎉 SUCCESS!  All tests passed!")
            print("  ✓ Code is mathematically correct")
            print("  ✓ Code follows physics principles")
            print("  ✓ Functions are consistent with each other")
            print("  ✓ Error handling works properly")
        else:
            print(f"\n  ⚠️  WARNING: {total_failed} test(s) failed!")
        
        print("\n" + "=" * 80 + "\n")
        
    except Exception as e:
        print(f"\n✗ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()