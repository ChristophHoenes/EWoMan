import numpy as np


#def select_strongest_pairs(fitness, num_matings=5):
#    sorted_fit = np.argsort(fitness)
#    pairs = sorted_fit[:2*num_matings].reshape([num_matings, 2])
#    return list(map(tuple, pairs))

def select_k_strongest_pairs(population, k=9):
    fitness = [p.fitness.values[0] for p in population]
    sorted_idxs = [x for x, y in sorted(enumerate(fitness), key=lambda tup: tup[1])]
    top_k = sorted_idxs[:k]
    return [population[top_k[np.random.choice(len(top_k))]] for i in range(2*len(population))]


def dummy_survivors(population, k=3):
    fitness = [p.fitness.values[0] for p in population]
    sorted_idxs = [x for x, y in sorted(enumerate(fitness), key=lambda tup: tup[1])]
    top_k = sorted_idxs[:k]
    return [population[i] for i in top_k]
