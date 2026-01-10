from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import math

# Number of qubits
n = 2

# Create Quantum Circuit
qc = QuantumCircuit(n, n)

# Step 1: Initialize in superposition
qc.h(range(n))

# -------- ORACLE (marks |11>) --------
qc.cz(0, 1)

# -------- DIFFUSER --------
qc.h(range(n))
qc.x(range(n))
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x(range(n))
qc.h(range(n))

# Measure
qc.measure(range(n), range(n))

# Run on simulator
backend = Aer.get_backend("qasm_simulator")
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()

print("Measurement Result:", counts)
