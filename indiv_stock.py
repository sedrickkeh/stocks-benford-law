import pandas as pd 
import yfinance as yf
from benford import get_dist 

import argparse
parser = argparse.ArgumentParser(description='Enter a stock symbol.')
parser.add_argument('--stock', type=str, default="TSLA")
args = parser.parse_args()

stock = args.stock
ticker = yf.Ticker(stock)
df = ticker.history(period="max")

close_prices = df["Close"]
first_digit_cnts, first_digit_cnts_percs = get_dist(close_prices)

print("Stock: {}".format(stock))
print("Earliest_date: {}".format(close_prices.index[0]))
print("Number of entries: {}".format(sum(first_digit_cnts)))
print(first_digit_cnts[1:])
print(first_digit_cnts_percs[1:])