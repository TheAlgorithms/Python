from genome import Genome
from geneh import GeneHistory
from species import Species

import random
import numpy as np
import matplotlib.pyplot as plt

class Population:
    def __init__(self, pop_len, n_inputs, n_outputs):
        self.pop_len = pop_len
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.population = []
        self.gh = GeneHistory(n_inputs, n_outputs)

        for _ in range(pop_len):
            self.population.append(Genome(self.gh))
            # temp 
            for _ in range(random.randint(10, 50)):
                self.population[-1].mutate()

        self.best_index = 0
        self.best = self.population[self.best_index]
        self.max_species = 5
        self.species = []
        pass

    def fitness_sharing(self):
        for i in range(self.pop_len):
            # For now, fitness_sharing dosen't work
            self.population[i].adjusted_fitness = self.population[i].fitness
            pass
        pass
    
    def speciate(self):
        # Clear all species
        self.species.clear()
        # add first member in a species
        self.species.append(Species(self.population[0]))
        for i in range(1, self.pop_len):
            accepted = False
            for s in range(len(self.species)):
                accepted = self.species[s].check(self.population[i])
                if accepted:
                    self.species[s].add(self.population[i])
                    break
            if not accepted:
                if len(self.species) >= self.max_species:
                    # get species with lowest no. of members
                    lowest = np.argmin([(len(s.members)) for s in self.species])
                    self.species[lowest].add(self.population[i])
                else:
                    self.species.append(Species(self.population[i]))
        if True:
            for s in self.species:
                print('Species : ', s.get_len())
        pass

    def plot_cluster(self):
        values = []
        # Append 0 for starting brain
        yvalues = np.zeros(self.pop_len)
        for i in range(self.pop_len):
            cd = self.population[0].calculate_compatibility(self.population[i])
            values.append(cd)
            yvalues[i] = i
        plt.plot(values, yvalues, 'ro')
        plt.show()
        pass
    
    # Heuristic for testing
    def next(self):
        self.best_index = self.best_index + 1 if self.best_index <= self.pop_len - 2 else 0
        self.best = self.population[self.best_index]
        print(self.best_index)
        pass

    def prev(self):
        self.best_index = self.best_index - 1 if self.best_index > 0 else self.pop_len - 1
        self.best = self.population[self.best_index]
        print(self.best_index)
        pass
