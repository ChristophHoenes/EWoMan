import sys, os
import numpy as np
import csv
import datetime
from statistics import mean
import pickle
from deap import creator, base
import evolution

os.chdir('./evoman_framework')
sys.path.insert(0, 'evoman')
from environment import Environment
# change working directory back to root
os.chdir('../')


def get_best_individuals(enemy = 2):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    top_individuals = []

    seeds = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1010]
    methods = ["method_1", "method2", "method3"]
    for method in methods:
        top_individuals_bymethod = []
        if method == 'method_1':
            prefix = 'roundrobin'
        elif method == 'method2':
            prefix = 'diversity_roundrobin'
        elif method == "method3":
            prefix = "diversity_075_roundrobin"
        for seed in seeds:

            top5_path = 'results/{}/{}_enemy{}_seed_{}/top5_iter_30'.format(method, prefix, enemy, seed)
            top_ind = pickle.load(open(top5_path, "rb"))[0]
            top_individuals.append(top_ind)

    return top_individuals

if __name__ == "__main__":

    experiment_name = 'experiment'
    if not os.path.exists(experiment_name):
        os.makedirs(experiment_name)

    en = 2
    results = {}
    count = 0
    top_individuals = get_best_individuals(enemy=en)
    for individual in top_individuals:
        ind_results = []
        for iter in range(5):
            env = Environment(experiment_name=experiment_name,
                              enemies=[en])
            fit, e_e, e_p, t = env.play(pcont=np.asarray(individual))
            ind_results.append(e_p-e_e)
        results[individual] = mean(ind_results)

        print("Count "+str(count))

    with open('experiment_results.csv', 'a') as f:
        write = csv.writer(f)
        f.write(str(en))
        for individual in results.keys():
            f.write(individual)

