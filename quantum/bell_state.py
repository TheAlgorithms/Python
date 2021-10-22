### Qiskit code to create and measure a Bell state. ####
import numpy as np
from qiskit import QuantumCircuit, execute, Aer
# Create a Quantum Circuit with two qbits and 2 classical bits
circuit = QuantumCircuit(2,2)
# Add a H gate on qubit 0
circuit.h(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0,1)
# Map the quantum measurement to the classical bits
circuit.measure([0,1],[0,1])
# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)
# Grab results from the job
result = job.result()
# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
