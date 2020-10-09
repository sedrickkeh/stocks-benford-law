import os
import argparse
import pandas as pd 

from stocks import Stocks
from utils import benford_dist, js


def main(config):
    stock = config.stock
    s = Stocks()

    first_digit_cnts, first_digit_cnts_percs = s.get_dist(stock)

    print("Stock: {}".format(stock))
    print("Earliest_date: {}".format(s.get_earliest_date(stock)))
    print("Number of entries: {}".format(sum(first_digit_cnts)))
    print("Distribution (counts): {}".format(first_digit_cnts))
    print("Distribution (percentages): {}".format([round(x, 3) for x in first_digit_cnts_percs]))
    print("Distribution (Benford): {}".format([round(x, 3) for x in benford_dist()]))
    print("Score: {}".format(js(first_digit_cnts_percs, benford_dist())))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Enter a stock symbol.')
    parser.add_argument('--stock', type=str, default="TGT")
    config = parser.parse_args()

    print(config)
    main(config)