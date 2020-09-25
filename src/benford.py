import numpy as np 
import matplotlib.pyplot as plt 

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
