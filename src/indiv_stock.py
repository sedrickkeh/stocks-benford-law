import os
import argparse
import pandas as pd 

from utils import Stocks, chi_squared
from benford import benford_dist


def main(config):
    stock = config.stock
    s = Stocks()

    closing_prices = s.get_closing_prices(stock)
    first_digit_cnts, first_digit_cnts_percs = s.get_dist(closing_prices)

    print("Stock: {}".format(stock))
    print("Earliest_date: {}".format(closing_prices.index[0]))
    print("Number of entries: {}".format(sum(first_digit_cnts)))
    print("Distribution (counts): {}".format(first_digit_cnts))
    print("Distribution (percentages): {}".format([round(x, 3) for x in first_digit_cnts_percs]))
    print("Distribution (Benford): {}".format([round(x, 3) for x in benford_dist()]))
    print("Score: {}".format(chi_squared(first_digit_cnts_percs, benford_dist())))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Enter a stock symbol.')
    parser.add_argument('--stock', type=str, default="TSLA")
    config = parser.parse_args()

    print(config)
    main(config)