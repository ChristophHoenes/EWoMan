import numpy as np
from deap import tools
import random


#def select_strongest_pairs(fitness, num_matings=5):
#    sorted_fit = np.argsort(fitness)
#    pairs = sorted_fit[:2*num_matings].reshape([num_matings, 2])
#    return list(map(tuple, pairs))

def select_k_strongest_pairs(population, k=9):
    fitness = [p.fitness.values[0] for p in population]
    sorted_idxs = [x for x, y in sorted(enumerate(fitness), key=lambda tup: tup[1])]
    top_k = sorted_idxs[:k]
    parents = [population[top_k[np.random.choice(len(top_k))]] for i in range(2*len(population))]
    return zip(parents[::2], parents[1::2])


def dummy_survivors(population, k=3):
    fitness = [p.fitness.values[0] for p in population]
    sorted_idxs = [x for x, y in sorted(enumerate(fitness), key=lambda tup: tup[1])]
    top_k = sorted_idxs[:k]
    return [population[i] for i in top_k]


def deap_tournament_pairs(population, k=50, tournsize=3):
    parents = tools.selTournament(population, k=k, tournsize=tournsize)
    return zip(parents[::2], parents[1::2])


def deap_tournament(population, k=3, tournsize=2):
    return tools.selTournament(population, k=k, tournsize=tournsize)

def round_robin_tournament(population, k=100, tournsize=10):
    wins = np.zeros(len(population))
    for id, x in enumerate(population):
        for j in range(tournsize):
            rival = random.choice(population)
            if x.fitness.values[0] > rival.fitness.values[0]:
                wins[id] += 1
    winner_idx = wins.argsort()[::-1][:k]
    survivors = [population[i] for i in winner_idx]
    return survivors
