import numpy as np 
import matplotlib.pyplot as plt  

def get_dist(price_arr):
    first_digit_cnts = [0 for i in range(10)]
    for p in price_arr:
        try:
            for dig in str(p):
                if (dig != '.' and dig != '0'): 
                    first_nonzero_dig = dig 
                    break
            first_digit_cnts[int(first_nonzero_dig)]+= 1
        except: continue

    s = sum(first_digit_cnts)
    if (s == 0): return [],[]

    first_digit_cnts_percs = [x/s for x in first_digit_cnts]
    return first_digit_cnts[1:], first_digit_cnts_percs[1:]


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
	return sum(p[i] * np.log2(p[i]/q[i]) for i in range(len(p)))

def mse(p, q):
    return np.mean((np.array(p)-np.array(q))**2)

generate_benford_plots()