from cmath import exp, pi, sqrt
from random import random
import itertools

class System:
    """
        This class represents the wave function describing a
        basic quantum computer consisting of n qubits.
    """
    def __init__(self, num_qubits):
        """
        set up a quantum system with the given number of qubits
        initialized to the "zero" qubit.
        """
        self.num_qubits = num_qubits
        # In this classical simulation,we use 2^n Qubit complex numbers
        # this array of size 2^n will replicate the 2^n states Qubits can have
        self.amplitudes = [0] * (1 << num_qubits)  # use bitshift to realize 2^n
        self.amplitudes[0] = 1  # so that sum of prob.s is 1, starting in 000 state
        self.states = self.generate_states(num_qubits)

    def generate_states(self, num_qubits):
        """
        returns a dictionary of all possible states for n qubits
        in the format { 'state': 'amplitude' } e.g. { 010 : 0j}
        """
        if num_qubits <= 0:
            raise ValueError("simulation requires at least 1 qubit")
        # generate table of states using itertools
        tuples = [''.join(_) for _ in itertools.product(['0', '1'], repeat=num_qubits)]
        data = {}
        map(lambda x: data.update({x:0}), tuples)
        # so that sum of squared amplitudes is 1, assume starting in 000 state
        data['000'] = 1
        return data

    def collapse(self):
        """
        collapse the system (i.e. measure it) and return the state
        based on a random choice from the weighted distribution
        """
        total = 0
        r = random()
        for state in self.states.keys():
            total += abs(self.states[state])**2
            if r <= total: # randomly selected weighted number
                # reset amplitudes after system collapse
                self.states = { x:0 for x in self.states }
                self.states['000'] = 1
                return state
