import os
import argparse
import pandas as pd 
from tqdm import tqdm

from utils import Stocks


def main(config):
    s = Stocks()
    sp_companies = pd.read_csv("data/constituents.csv")
   
    company_list, digit_distributions, digit_distributions_perc = [], [], []
    for sym in tqdm(sp_companies["Symbol"]):
        closing_prices = s.get_closing_prices(sym)
        first_digit_cnts, first_digit_cnts_percs = s.get_dist(closing_prices)
        if (len(first_digit_cnts) == 0): continue

        company_list.append(sym)
        digit_distributions.append(first_digit_cnts)
        digit_distributions_perc.append(first_digit_cnts_percs)


    ## Compiling and saving distributions
    companies_df = pd.DataFrame(data=company_list, columns=["Stock"])

    compiled_dist = pd.DataFrame(digit_distributions)
    compiled_dist.columns = range(1, 10)
    compiled_df = companies_df.join(compiled_dist)
    compiled_df.to_csv("output/s&p500_dist.csv", index=False)

    compiled_dist_perc = pd.DataFrame(digit_distributions_perc)
    compiled_dist_perc.columns = range(1, 10)
    compiled_df_perc = companies_df.join(compiled_dist_perc)
    compiled_df_perc.to_csv("output/s&p500_dist_perc.csv", index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    config = parser.parse_args()

    print(config)
    main(config)