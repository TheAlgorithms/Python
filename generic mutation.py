# Python3 program to create target string, starting from 
# random string using Genetic Algorithm 

import random 

# Number of individuals in each generation 
POPULATION_SIZE = 10

# Valid genes 
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Target string to be generated 
TARGET = "I love GeeksforGeeks"

class Individual(object): 
    ''' 
    Class representing individual in population 
    '''
    def __init__(self, chromosome): 
        self.chromosome = chromosome 
        self.fitness = self.cal_fitness() 

    @classmethod
    def mutated_genes(self): 
        ''' 
        Create random genes for mutation 
        '''
        global GENES 
        gene = random.choice(GENES) 
        return gene 

    @classmethod
    def create_gnome(self): 
        ''' 
        Create chromosome or string of genes 
        '''
        global TARGET 
        gnome_len = len(TARGET) 
        return [self.mutated_genes() for _ in range(gnome_len)] 

    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring 
        '''

        # Chromosome for offspring 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     

            # Random probability 
            prob = random.random() 

            # If prob is less than 0.45, insert gene 
            # from parent 1 
            if prob < 0.45: 
                child_chromosome.append(gp1) 

            # If prob is between 0.45 and 0.90, insert 
            # gene from parent 2 
            elif prob < 0.90: 
                child_chromosome.append(gp2) 

            # Otherwise insert random gene (mutate), 
            # for maintaining diversity 
            else: 
                child_chromosome.append(self.mutated_genes()) 

        # Create new Individual (offspring) using 
        # generated chromosome for offspring 
        return Individual(child_chromosome) 

    def cal_fitness(self): 
        ''' 
        Calculate fitness score, it is the number of 
        characters in string which differ from target 
        string. 
        '''
        global TARGET 
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET): 
            if gs != gt: 
                fitness += 1
        return fitness 

# Driver code 
def main(): 
    global POPULATION_SIZE 

    # Current generation 
    generation = 1

    found = False
    population = [] 

    # Create initial population 
    for _ in range(POPULATION_SIZE): 
        gnome = Individual.create_gnome()  # Fixed this
        population.append(Individual(gnome)) 

    while not found: 

        # Sort the population in increasing order of fitness score 
        population = sorted(population, key = lambda x:x.fitness) 

        # If the individual having the lowest fitness score is 0, 
        # we have reached the target 
        if population[0].fitness <= 0: 
            found = True
            break

        # Otherwise, generate new offsprings for new generation 
        new_generation = [] 

        # Perform Elitism, that means 10% of fittest population 
        # goes to the next generation 
        s = int((10 * POPULATION_SIZE) / 100) 
        new_generation.extend(population[:s]) 

        # From 50% of the fittest population, individuals 
        # will mate to produce offspring 
        s = int((90 * POPULATION_SIZE) / 100) 
        for _ in range(s): 
            parent1 = random.choice(population[:50]) 
            parent2 = random.choice(population[:50]) 
            child = parent1.mate(parent2) 
            new_generation.append(child) 

        population = new_generation 

        # Print current generation details 
        print("Generation: {}\tString: {}\tFitness: {}".format(
            generation, 
            "".join(population[0].chromosome), 
            population[0].fitness)) 

        generation += 1

    # Print final result
    print("Generation: {}\tString: {}\tFitness: {}".format(
        generation, 
        "".join(population[0].chromosome), 
        population[0].fitness)) 

if __name__ == '__main__': 
    main()
