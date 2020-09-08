import numpy as np
import pandas as pd 
import yfinance as yf 
from benford import get_dist

sp_companies = pd.read_csv("constituents.csv")
company_list, digit_distributions, digit_distributions_perc = [], [], []

for sym in sp_companies["Symbol"]:
    ticker = yf.Ticker(sym)
    df = ticker.history(period="max")
    close_prices = df["Close"]

    first_digit_cnts, first_digit_cnts_percs = get_dist(close_prices)
    if (len(first_digit_cnts) == 0): continue

    company_list.append(sym)
    digit_distributions.append(first_digit_cnts)
    digit_distributions_perc.append(first_digit_cnts_percs)


## Compiling and saving distributions
companies_df = pd.DataFrame(data=company_list, columns=["Stock"])

compiled_dist = pd.DataFrame(digit_distributions)
compiled_dist.columns = range(1, 10)
compiled_df = companies_df.join(compiled_dist)
compiled_df.to_csv("s&p500_dist.csv", index=False)

compiled_dist_perc = pd.DataFrame(digit_distributions_perc)
compiled_dist_perc.columns = range(1, 10)
compiled_df_perc = companies_df.join(compiled_dist_perc)
compiled_df_perc.to_csv("s&p500_dist_perc.csv", index=False)
