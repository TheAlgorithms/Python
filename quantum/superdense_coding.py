"""
Build the superdense coding protocol. This quantum
circuit can send two classical bits using one quantum
bit. This circuit is designed using the Qiskit
framework. This experiment run in IBM Q simulator 
with 1000 shots.
.
References:
https://qiskit.org/textbook/ch-algorithms/superdense-coding.html
https://en.wikipedia.org/wiki/Superdense_coding
"""

import qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

def superdense_coding(
    c_information: str = '11'
    ) -> qiskit.result.counts.Counts:
    """
    # >>> superdense_coding(c_information)
    # The input refer to the classical message
    # that you wants to send. {'00','01','10','11'}
    # result for default values: {11: 1000}                         
               ┌───┐          ┌───┐     
    qr_0: ─────┤ X ├──────────┤ X ├─────
          ┌───┐└─┬─┘┌───┐┌───┐└─┬─┘┌───┐
    qr_1: ┤ H ├──■──┤ X ├┤ Z ├──■──┤ H ├
          └───┘     └───┘└───┘     └───┘
    cr: 2/══════════════════════════════                       
    Args:
        c_information: classical information to send.
    Returns:
        qiskit.result.counts.Counts: counts of send state.
    """
    # build registers
    qr = QuantumRegister(2, 'qr')
    cr = ClassicalRegister(2, 'cr')

    quantum_circuit = QuantumCircuit(qr,cr)

    # entanglement the qubits
    quantum_circuit.h(1)
    quantum_circuit.cx(1,0)

    # send the information

    if c_information == '11':
        quantum_circuit.x(1)
        quantum_circuit.z(1)
    elif c_information == '10':
        quantum_circuit.z(1)
    elif c_information == '01':
        quantum_circuit.x(1)
    else:
        quantum_circuit.i(1)

    #unentangled the circuit
    quantum_circuit.cx(1,0)
    quantum_circuit.h(1)

    # measure the circuit
    quantum_circuit.measure(qr,cr)

    backend = Aer.get_backend('qasm_simulator')
    job = execute(quantum_circuit, backend, shots=1000)

    return job.result().get_counts(quantum_circuit)

if __name__ == "__main__":
    print(f"Count for classical state send: {superdense_coding()}")
