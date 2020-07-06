"""
Simple multithreaded algorithm to show how the 4 phases of a genetic
algorithm works (Evaluation, Selection, Crossover and Mutation)

https://en.wikipedia.org/wiki/Genetic_algorithm

Author: D4rkia
"""

import random
from typing import List, Tuple

N_POPULATION = 200
N_SELECTED = 50
MUTATION_PROBABILITY = 0.1
random.seed(random.randint(0, 1000))


def basic(sentence: str, genes: List[str]) -> Tuple[int, int, str]:
    """The actual algorithm"""
    # Verify that the sentence contains no other genes
    # that the ones inside genes variable
    for i in sentence:
        if i not in genes_list:
            raise ValueError(f"{i} is not in  genes list, evolution can't converge")

    # Generate random starting population
    population = []
    for _ in range(N_POPULATION):
        population.append(
            "".join([random.choice(genes_list) for i in range(len(sentence))])
        )

    # Just some logs to know what the algorithms is doing
    generation, total_population = 0, 0

    # This loop will end when we will find a perfect match for our sentence
    while True:
        generation += 1
        total_population += len(population)

        # Random population created now it's time to evaluate
        def evaluate(item: str, main_sentence: str = sentence) -> Tuple[str, float]:
            """
                Evaluate how similar the item is with the sentence by just
                counting each char in the right position

                >>> evaluate("Helxo Worlx", Hello World)
                ["Helxo Worlx", 9]
            """
            score = 0
            for position, g in enumerate(item):
                if g == main_sentence[position]:
                    score += 1
            return (item, float(score))

        # Adding a bit of concurrency can make everything faster,
        #
        # import concurrent.futures
        # population_score: List[Tuple[str, float]] = []
        # with concurrent.futures.ThreadPoolExecutor(
        #                                   max_workers=NUM_WORKERS) as executor:
        #     futures = {executor.submit(evaluate, item) for item in population}
        #     concurrent.futures.wait(futures)
        #     population_score = [item.result() for item in futures]
        #
        # but with a simple algorithm like this will probably be slower
        # we just need to call evaluate for every item inside population
        population_score = [evaluate(item) for item in population]

        # Check if there is a matching evolution
        population_score = sorted(population_score, key=lambda x: x[1], reverse=True)
        if population_score[0][0] == sentence:
            return (generation, total_population, population_score[0][0])

        # Print the Best result every 10 generation
        # just to know that the algorithm is working
        if generation % 10 == 0:
            print(
                f"\nGeneration: {generation}"
                f"\nTotal Population:{total_population}"
                f"\nBest score: {population_score[0][1]}"
                f"\nSentence: {population_score[0][0]}"
            )

        # Flush the old population
        population = []
        # Normalize population score from 0 to 1
        population_score = [
            (item, score / len(sentence)) for item, score in population_score
        ]

        # Select, Crossover and Mutate a new population
        def select(parent_1: Tuple[str, float]) -> List[str]:
            """Select the second parent and generate new population"""
            pop = []
            # Generate more child proportionally to the fitness score
            child_n = int(parent_1[1] * 100) + 1
            child_n = 10 if child_n >= 10 else child_n
            for _ in range(child_n):
                parent_2 = population_score[random.randint(0, N_SELECTED)][0]
                child_1, child_2 = crossover(parent_1[0], parent_2)
                # Append new string to the population list
                pop.append(mutate(child_1))
                pop.append(mutate(child_2))
            return pop

        def crossover(parent_1: str, parent_2: str) -> Tuple[str, str]:
            """Slice and combine two string in a random point"""
            random_slice = random.randint(0, len(parent_1) - 1)
            child_1 = parent_1[:random_slice] + parent_2[random_slice:]
            child_2 = parent_2[:random_slice] + parent_1[random_slice:]
            return (child_1, child_2)

        def mutate(child: str) -> str:
            """Mutate a random gene of a child with another one from the list"""
            child_list = list(child)
            if random.uniform(0, 1) > MUTATION_PROBABILITY:
                child_list[random.randint(0, len(child)) - 1] = random.choice(genes)
            return "".join(child_list)

        # This is Selection
        for i in range(N_SELECTED):
            population.extend(select(population_score[int(i)]))
            # Check if the population has already reached the maximum value and
            # break the cycle
            # if this check is disabled
            # the algorithm will take forever to compute large strings
            # but will also calcolate small string in a lot less generations
            if len(population) > N_POPULATION:
                break


if __name__ == "__main__":
    sentence_str = (
        "This is a genetic algorithm to evaluate, combine, evolve  mutate a string!"
    )
    genes_list = list(
        " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm"
        "nopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\"
    )
    print(
        "\nGeneration: %s\nTotal Population: %s\nSentence: %s"
        % basic(sentence_str, genes_list)
    )

__author__ = "D4rkia.Fudo"
