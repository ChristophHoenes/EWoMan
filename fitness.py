import os
import numpy as np


def default_fitness(p, env):
    os.chdir('./evoman_framework')
    fit, e_p, e_e, t = env.play(pcont=np.asarray(p))
    os.chdir('../')
    return fit

