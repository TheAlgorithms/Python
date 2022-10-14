# -*- coding: utf-8 -*-
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_bloch_multivector
from qiskit_textbook.widgets import plot_bloch_vector_spherical
from math import pi
sim = Aer.get_backend('aer_simulator')
"""Bloch_Sphere
In quantum mechanics, the Bloch sphere is a geometrical representation of the
pure state space of a two-level quantum mechanical system (qubit)"""
"""
**References**

https://en.wikipedia.org/wiki/Bloch_sphere

https://qiskit.org/textbook """
""""
Requirements

!pip install qiskit ipywidgets
!pip install pylatexenc
"""
coords = [pi / 2 , 0 , 1]   # [Theta, Phi, Radius]
plot_bloch_vector_spherical(coords)   # Bloch Vector with spherical coordinates

"""# **Example**"""

qc = QuantumCircuit(1)
qc.x(0)
qc.draw()
qc.save_statevector()
qobj = assemble(qc)
state = sim.run(qobj).result().get_statevector()
plot_bloch_multivector(state)

"""# **Implementation using U-gate**"""

# Let's have U-gate transform a |0> to |+> state
qc = QuantumCircuit(1)
qc.u(pi / 2 , 0 , pi , 0)
qc.draw()
# Let's see the result
qc.save_statevector()
qobj = assemble(qc)
state = sim.run(qobj).result().get_statevector()
plot_bloch_multivector(state)
