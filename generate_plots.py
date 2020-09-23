import pickle
from util import plot_diversity

if __name__ == "__main__":
    log_path = "deap_roundrobin_23_Sep_2020_11-28-58/logs_iter_30"
    logs = pickle.load(open(log_path, "rb"))
    plot_diversity(logs)
