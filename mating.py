import numpy as np


def select_mating_partners(fitness, num_matings=10, typ='dummy'):
    if typ == 'dummy':
        sorted_fit = np.argsort(fitness)
        pairs = sorted_fit[:2*num_matings].reshape([num_matings, 2])
        return list(map(tuple, pairs))
    else:
        raise RuntimeError("Unknown type of mating selection encountered! Please check your config.")


def mate(population, partner_ids, typ='dummy'):
    if typ == 'dummy':
        children = []
        for pair in partner_ids:
            kid = 0.5 * population[pair[0]] + 0.5 * population[pair[1]]
            children.append(kid)
        return np.stack(children)
    else:
        raise RuntimeError("Unknown type of mating function encountered! Please check your config.")

