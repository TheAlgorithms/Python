# Quantum Modules (Pure-Python Educational Restorations)

This document tracks the restored quantum modules that were previously disabled.

## Restored modules

- `quantum/not_gate.py`
- `quantum/single_qubit_measure.py`
- `quantum/bb84.py`
- `quantum/deutsch_jozsa.py`
- `quantum/quantum_entanglement.py`
- `quantum/quantum_teleportation.py`
- `quantum/quantum_random.py`
- `quantum/half_adder.py`
- `quantum/q_full_adder.py`
- `quantum/ripple_adder_classic.py`
- `quantum/superdense_coding.py`

## Notes

- Implementations are designed for deterministic, dependency-free CI execution.
- They model the protocol logic in a simplified way, prioritizing educational clarity.
- For runnable examples, use: `python examples/quantum_quickstart.py`.
- For tests, use: `python -m pytest tests/test_quantum.py`.

## Suggested references

- BB84: <https://en.wikipedia.org/wiki/BB84>
- Deutsch-Jozsa: <https://en.wikipedia.org/wiki/Deutsch%E2%80%93Jozsa_algorithm>
- Superdense coding: <https://en.wikipedia.org/wiki/Superdense_coding>
- Quantum teleportation: <https://en.wikipedia.org/wiki/Quantum_teleportation>
