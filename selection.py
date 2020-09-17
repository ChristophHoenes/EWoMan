import numpy as np


def select_strongest_pairs(fitness, num_matings=10):
    sorted_fit = np.argsort(fitness)
    pairs = sorted_fit[:2*num_matings].reshape([num_matings, 2])
    return list(map(tuple, pairs))


def dummy_survivors(population, offspring, die_prob=0.05):
    pop_size = population.shape[0]
    survivors = np.ones(size=pop_size, dtype=bool)
    pop_dead = np.random.choice(pop_size, size=(pop_size*die_prob))
    survivors[pop_dead] = False

    kid_size = offspring.shape[0]
    kid_survivors = np.ones(size=kid_size, dtype=bool)
    kid_dead = np.random.choice(kid_size, size=(kid_size*die_prob**2))
    kid_survivors[kid_dead] = False

    return np.vstack([population[survivors], offspring[kid_survivors]])
