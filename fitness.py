import os
import numpy as np


def default_fitness(p, env):
    os.chdir('./evoman_framework')
    fit, e_e, e_p, t = env.play(pcont=np.asarray(p))
    os.chdir('../')
    return fit

