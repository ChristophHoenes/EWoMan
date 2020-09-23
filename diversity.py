import numpy as np

# moment of interia diversity
def diversity(population):
    pop = np.asarray(population)
    centroids = pop.mean(axis=0)
    return sum([np.square(ind-centroids).sum() for ind in pop])


# calculate gains like
#gainz = list(map(lambda p: diversity_gain(offspring, p), population))
def diversity_gain(population, individual):
    pop = np.asarray(population)
    ind = np.asarray(individual)
    centroids = pop.mean(axis=0)
    return np.square(ind - centroids).sum()
