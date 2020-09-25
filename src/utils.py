import numpy as np 
import yfinance as yf

class Stocks:
    def __init__(self):
        return None

    def get_closing_prices(self, sym):
        ticker = yf.Ticker(sym)
        df = ticker.history(period="max")
        close_prices = df["Close"]
        return close_prices

    def get_dist(self, price_arr):
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

        first_digit_cnts_percs = [(x/s) for x in first_digit_cnts]
        return first_digit_cnts[1:], first_digit_cnts_percs[1:]


def kl_divergence(p, q):
	return np.sum(p[i] * np.log2(p[i]/q[i]) for i in range(len(p)))

def mse(p, q):
    return np.mean((np.array(p)-np.array(q))**2)

def chi_squared(o, e):
    return np.sum(((p-q)**2)/q for (p,q) in zip(o, e))

def get_score(p):
    benford = benford_dist()
    return chi_squared(p, benford)