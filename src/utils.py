import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial import distance 

def benford_dist():
    return [np.log10(1 + (1/x)) for x in range(1, 10)]

def generate_benford_plots():
    a = benford_dist()
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.bar(height=a, x=range(1, 10))
    for i, v in enumerate(a):
        ax.text(i+0.64, v+0.002, str(round(v,3)))

    plt.title("Benford's Law Proportions", size=16)
    plt.xticks(range(1, 10))
    plt.xlabel("First Digits")
    plt.ylabel("Proportions")
    plt.show()


def kl_divergence(p, q):
	return np.sum(p[i] * np.log2(p[i]/q[i]) for i in range(len(p)))

def mse(p, q):
    return np.mean((np.array(p)-np.array(q))**2)

def chi_squared(o, e):
    return np.sum(((p-q)**2)/q for (p,q) in zip(o, e))

def js(p, q):
    return distance.jensenshannon(p, q)
    
def get_score(dist_cnts, dist_percs):
    n = np.sum(dist_cnts)
    benford = benford_dist()
    benford_cnts = [(x*n) for x in benford]
    return chi_squared(dist_cnts, benford_cnts)