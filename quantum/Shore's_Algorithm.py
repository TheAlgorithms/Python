from qiskit import Aer, QuantumCircuit, transpile, assemble
from qiskit.providers import BaseBackend
from qiskit.providers.ibmq import least_busy
from qiskit.algorithms import Shor

# Integer to be factorized
N = 15

# Create a QuantumCircuit to run Shor's algorithm
circuit = QuantumCircuit(N.bit_length() + 3, N.bit_length())

# Apply the Quantum Fourier Transform
for q in range(N.bit_length()):
    circuit.h(q)

# Apply the modular exponentiation
for q in range(N.bit_length()):
    circuit.x(N.bit_length() + q)
for a in range(N):
    a_binary = format(a, '0' + str(N.bit_length()) + 'b')
    for q in range(N.bit_length()):
        if a_binary[q] == '1':
            circuit.cx(q, N.bit_length() + q)

# Apply the inverse Quantum Fourier Transform
for q in range(N.bit_length()):
    for p in range(q):
        circuit.cp(-np.pi / (2 ** (q - p)), p, q)
    circuit.h(q)

# Measure the first N bits
circuit.measure(list(range(N.bit_length())), list(range(N.bit_length())))

# Choose a backend (simulator or real quantum device)
backend = Aer.get_backend('qasm_simulator')

# Run the circuit on the chosen backend
compiled_circuit = transpile(circuit, backend)
job = assemble(compiled_circuit)
result = backend.run(job).result()

# Use Shor's algorithm to find the factors
factors = Shor(N).factor(result, BaseBackend(backend))

print(f"The factors of {N} are {factors.factors}.")
