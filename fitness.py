import os

def evaluate_fitness(p, env, typ='default'):
    if typ == 'default':
        os.chdir('./evoman_framework')
        fit, e_e, e_p, t = env.play(pcont=p)
        os.chdir('../')
        return fit
    else:
        raise RuntimeError("Unknown type of fitness function encountered! Please check your config.")

