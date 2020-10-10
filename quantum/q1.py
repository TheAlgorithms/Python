import qiskit as q

"""
Build a simple bare-minimum quantum
circuit that starts with a single qubit
(by default in state 0), runs the experiment
1000 times, and finally prints the total 
count of the states finally observed.
"""

# Use Aer's qasm_simulator
simulator = q.Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = q.QuantumCircuit(1, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0], [0])

# Execute the circuit on the qasm simulator
job = q.execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for varopis staes are:", counts)
