import numpy as np


def average_parents(population, partner_ids):
    children = []
    for pair in partner_ids:
        kid = 0.5 * population[pair[0]] + 0.5 * population[pair[1]]
        children.append(kid)
    return np.stack(children)

