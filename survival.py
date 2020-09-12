import numpy as np


def select_survivors(population, offspring, die_prob=0.05, typ='dummy'):
    if typ == 'dummy':
        pop_size = population.shape[0]
        survivors = np.ones(size=pop_size, dtype=bool)
        pop_dead = np.random.choice(pop_size, size=(pop_size*die_prob))
        survivors[pop_dead] = False

        kid_size = offspring.shape[0]
        kid_survivors = np.ones(size=kid_size, dtype=bool)
        kid_dead = np.random.choice(kid_size, size=(kid_size*die_prob**2))
        kid_survivors[kid_dead] = False

        return np.vstack([population[survivors], offspring[kid_survivors]])
    else:
        raise RuntimeError("Unknown type of survival selection encountered! Please check your config.")
