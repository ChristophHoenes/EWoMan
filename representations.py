import json
import numpy as np
import os
import sys
from abc import ABC, abstractmethod

sys.path.insert(0, './evoman_framework')
from demo_controller import player_controller


NUM_SENSORS = 20
NUM_ACTIONS = 5

def select_representation(args):
    if args.representation == "Neurons":
        return NeuronRep(args.num_neurons)
    else:
        raise RuntimeError('Unknown representation type encountered!')


class Representation(ABC):

    def __init__(self, config):
        with open('configs/{}'.format(config)) as c:
            self.config = json.loads(c)
        super(Representation, self).__init__()

    @abstractmethod
    def get_controller(self):
        raise NotImplementedError

    @abstractmethod
    def create_population(self):
        raise NotImplementedError


class NeuronRep(Representation):

    def __init__(self, num_neurons):
        self.config = {"num_neurons": num_neurons,
                       "num_params": (NUM_SENSORS + 1) * num_neurons + (num_neurons + 1) * NUM_ACTIONS}

    def get_controller(self):
        return player_controller(self.config['num_neurons'])

    def create_population(self, population_size):
        # TODO maybe change to uniform distribution
        # TODO check number of parameters/neurons
        return np.random.normal(loc=0, scale=1, size=(population_size, self.config['num_params']))
