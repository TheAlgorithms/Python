from __future__ import annotations

from quantum.bb84 import bb84
from quantum.deutsch_jozsa import deutsch_jozsa
from quantum.half_adder import half_adder
from quantum.not_gate import not_gate
from quantum.q_full_adder import q_full_adder
from quantum.quantum_entanglement import quantum_entanglement
from quantum.quantum_random import quantum_random
from quantum.quantum_teleportation import quantum_teleportation
from quantum.ripple_adder_classic import ripple_adder
from quantum.single_qubit_measure import single_qubit_measure
from quantum.superdense_coding import superdense_coding


def test_not_gate() -> None:
    assert not_gate(0) == 1
    assert not_gate(1) == 0


def test_single_qubit_measure_counts() -> None:
    assert single_qubit_measure(1, 1, shots=7) == {"0": 7}


def test_bb84_length_and_seed_reproducibility() -> None:
    assert len(bb84(32, seed=42)) == 32
    assert bb84(8, seed=1) == bb84(8, seed=1)


def test_deutsch_jozsa_constant_and_balanced() -> None:
    assert deutsch_jozsa(lambda _: 1, 4) == "constant"
    assert deutsch_jozsa(lambda bits: int(bits.count("1") % 2 == 0), 3) == "balanced"


def test_entanglement_and_teleportation() -> None:
    entangled = quantum_entanglement(101)
    assert set(entangled) == {"00", "11"}
    assert sum(entangled.values()) == 101
    assert quantum_teleportation(1, shots=9) == {"1": 9}


def test_adders() -> None:
    assert half_adder(1, 1) == (0, 1)
    assert q_full_adder(1, 1, 1) == (1, 1)
    assert ripple_adder(13, 11) == 24


def test_quantum_random_and_superdense() -> None:
    bits = quantum_random(12, seed=0)
    assert len(bits) == 12
    assert set(bits) <= {"0", "1"}
    assert superdense_coding(1, 0, shots=3) == {"10": 3}
