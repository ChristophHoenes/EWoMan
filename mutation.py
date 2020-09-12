import numpy as np


def mutate(population, mutate_prob=0.01, typ='dummy'):
    if typ == 'dummy':
        shape = population.shape
        num_mutate = round(shape[0] * shape[1] * mutate_prob)
        for m in num_mutate:
            mutate_individual = np.random.choice(shape[0])
            mutate_gene = np.random.choice(shape[1])
            population[mutate_individual][mutate_gene] += np.random.normal(loc=0, scale=0.5)

        return population
    else:
        raise RuntimeError("Unknown type of mutation function encountered! Please check your config.")
