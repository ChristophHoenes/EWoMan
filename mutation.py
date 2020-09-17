import numpy as np


def gaussian_dummy_mutate(population, mutate_prob=0.1):
    num_mutate = round(len(population) * mutate_prob)
    for m in range(num_mutate):
        mutate_individual = population[np.random.choice(len(population))]
        for gene in range(round(len(mutate_individual) * mutate_prob)):
            mutate_gene = np.random.choice(len(mutate_individual))
            mutate_individual[mutate_gene] += np.random.normal(loc=0, scale=0.5)
    return population

