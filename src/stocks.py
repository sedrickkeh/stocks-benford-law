import os
import numpy as np
import pandas as pd 

class Stocks:
    def __init__(self):
        self.df = pd.read_csv("data/prices.csv", index_col="Start Date")
        self.dates = self.df.index

    def __getitem__(self, sym):
        return self.df[sym].dropna()

    def get_by_date(self, sym, start_date="1980-01-01", end_date="2020-09-29"):
        return self.df[sym][start_date:end_date]

    def get_latest_price(self, sym):
        return self.df[sym][-1]
    
    def get_earliest_date(self, sym):
        return self.df[sym].dropna().index[0]

    def get_dist(self, sym):
        first_digit_cnts = [0 for i in range(10)]
        price_arr = self[sym]
        for p in price_arr:
            try:
                for digit in str(p):
                    if (digit != '.' and digit != '0'): 
                        first_nonzero_dig = digit 
                        break
                first_digit_cnts[int(first_nonzero_dig)] += 1
            except: continue

        s = sum(first_digit_cnts)
        if (s == 0): return [],[]

        first_digit_cnts_percs = [(x/s) for x in first_digit_cnts]
        return first_digit_cnts[1:], first_digit_cnts_percs[1:]

    def get_volatility(self, sym):
        prices = self[sym]
        yesterday = prices[1:].values
        today = prices[:-1].values
        returns = (today-yesterday)/yesterday
        return np.std(returns)