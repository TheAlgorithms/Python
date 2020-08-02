#This is basic code demonstrating the qiskit library.
#A Quantum circuit with one Hadamard gate (H gate)

#importing dependancies
import numpy as np
from qiskit import (QuantumCircuit, execute , Aer)
from qiskit.visualization import plot_histogram

#For the simulator
simulator = Aer.get_backend('qasm_simulator')

#Creating the circuit
circuit = QuantumCircuit(2,2) # Two qubits

#Adding H-gate on Qubit 0
circuit.h(0)

# Adding a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Mapping the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000) #run the simulation 1,000 times

#Get the result from the simulation
result = job.result()

#Returning counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are",counts['00'],' and ',counts['11'])

