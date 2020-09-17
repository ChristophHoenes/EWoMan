import os
import numpy as np


def default_fitness(p, env):
    #if typ == 'default':
    os.chdir('./evoman_framework')
    fit, e_e, e_p, t = env.play(pcont=np.asarray(p))
    os.chdir('../')
    return fit
    #else:
    #    raise RuntimeError("Unknown type of fitness function encountered! Please check your config.")

