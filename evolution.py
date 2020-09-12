# standard library imports
import argparse
import json
import sys
import os
# third party imports

# local imports
# change directory and add evoman to path to be able to load framework without errors
os.chdir('./evoman_framework')
sys.path.insert(0, 'evoman')
from environment import Environment
# change working directory back to root
os.chdir('../')

from fitness import evaluate_fitness
from mating import mate, select_mating_partners
from mutation import mutate
from representations import select_representation
from survival import select_survivors


def start_evolution(args, config):

    # pick problem representation
    rep = select_representation(args)
    # initialize controller that handles the representation
    controller = rep.get_controller()

    #create folder for experiment
    # TODO "overthink" folder structure to resolve directory changes
    os.chdir('./evoman_framework')
    exp_name = "specialist_{}".format(args.enemies)
    if not os.path.exists(exp_name):
        os.mkdir(exp_name)

    # create environment
    env = Environment(experiment_name=exp_name,
                      enemies=args.enemies,
                      playermode="ai",
                      player_controller=controller,
                      enemymode="static",
                      level=args.level,
                      speed="fastest",
                      randomini=args.random_loc,
                      contacthurt=args.contacthurt,
                      sound="off")
    os.chdir('../')

    # create initial population
    population = rep.create_population(args.pop_size)

    # loop through training iterations
    for i in range(args.num_iter):

        # test fitness of population
        fitness = list(map(lambda p: evaluate_fitness(p, env, typ=config["fitness"]), population))
        # mating selection
        partner_ids = select_mating_partners(fitness, typ=config["mate_select"])
        # mating mechanism (creating offspring from selection) and random mutation
        offspring = mate(population, partner_ids, typ=config["mate"])
        # random mutations of existing individuals?? (optional)
        population = mutate(population, typ=config["mutate"])
        offspring = mutate(offspring, typ=config["mutate"])
        # survivor selection (define population of next iteration; which individuals are kept)
        population = select_survivors(population, offspring, typ=config["survive_select"])

        # TODO (see comment below)
        # record statistics and save intermediate results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evolution Parameters.')
    parser.add_argument('--num_iter', default=100,
                        help='Number of iterations of the evolution (number of generated generations).')
    parser.add_argument('--num_neurons',  default=10,
                        help='Number of neurons used for the population.')
    parser.add_argument('--enemies', default=[2], nargs='+', type=int,
                        help='ID(s) of the enemy to specialize.')
    parser.add_argument('--level', default=1, type=int,
                        help='Difficulty of the game.')
    parser.add_argument('--random_loc', default="no", type=str, choices=["yes", "no"],
                        help='Whether or not to randomly initialize location of enemy.')
    parser.add_argument('--contacthurt', default="player", type=str, choices=["player", "enemy"],
                        help='Who is hurt by contact with the opponent.')
    parser.add_argument('--pop_size', default=100, type=int,
                        help='Population size (initial number of individuals).')
    parser.add_argument('--config', default="default_config.json", type=str,
                        help='Configuration file that specifies some parameters.')
    parser.add_argument('--representation', default="Neurons", type=str, choices=["Neurons"],
                        help='Type of problem representation.')

    args = parser.parse_args()

    # load config from file
    with open('configs/{}'.format(args.config)) as c:
        config = json.loads(c.read())

    start_evolution(args, config)
