import numpy as np


def select_mating_partners(fitness, num_matings=10, typ='dummy'):
    if typ == 'dummy':
        print('SELECT MATING PARTNERS')
        sorted_fit = np.argsort(fitness)
        pairs = sorted_fit[:2*num_matings].reshape([num_matings, 2])
        return list(map(tuple, pairs))
    else:
        raise RuntimeError("Unknown type of mating selection encountered! Please check your config.")


def mate(population, partner_ids, typ='dummy', alpha =0.5):
    typ = 'arithmetic'
    if typ == 'dummy':
        children = []
        for pair in partner_ids:
            crossover = np.random.rand(len(population[pair[0]])) > 0.5

            kid = population[pair[0]]

            kid[crossover] = population[pair[1]][crossover]

            children.append(kid)
        return np.stack(children)
    elif typ == 'inverse_child':
        children = []
        for pair in partner_ids:
            crossover = np.random.rand(len(population[pair[0]])) > 0.5

            kid = np.copy(population[pair[0]])
            kid_second = population[pair[1]]

            kid[crossover] = population[pair[1]][crossover]
            kid_second[crossover] = population[pair[0]][crossover]
            #print(kid == kid_second)

            children.append(kid)
            children.append(kid_second)
        return np.stack(children)
    elif typ == 'arithmetic':
        children = []
        for pair in partner_ids:

            kid = np.copy(population[pair[0]])
            kid_second = population[pair[1]]

            for index,val in enumerate(population[pair[0]]):

                kid[index] = alpha * population[pair[0]][index] + (1-alpha) * population[pair[1]][index]
                kid_second[index] = alpha * population[pair[1]][index] + (1-alpha) * population[pair[0]][index]
            
            children.append(kid)
            children.append(kid_second)
        return np.stack(children)
    else:
        raise RuntimeError("Unknown type of mating function encountered! Please check your config.")

