#Suggestion: Use jupyter notebook for quantum programs

from qiskit import *

qr = QuantumRegister(2)   # 2 qubits 
cr = ClassicalRegister(2) # 2 classical bits for measurement

circuit = QuantumCircuit(qr, cr) #Built a quantum circuit

%matplotlib inline #check out circuit
circuit.draw()

circuit.h(qr[0])  #Hadamard Gate on first qubit
circuit.draw(output='mpl')

circuit.cx(qr[0], qr[1]) #CNOT gate controlling qubit q0 qubit and controlled qubit is q1
circuit.draw(output='mpl')

circuit.measure(qr, cr) #Measuring the circuit using classical bits
circuit.draw(output='mpl')

simulator = Aer.get_backend('qasm_simulator')  #Setting up backend simulator
execute(circuit, backend=simulator)  #Simulating the results

result= execute(circuit, backend=simulator).result()  #Storing the results

from qiskit.tools.visualization import plot_histogram #Now we need to plot the results

plot_histogram(result.get_counts(circuit))