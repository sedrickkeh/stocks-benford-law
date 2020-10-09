import os
import argparse
import pandas as pd 
from tqdm import tqdm

from stocks import Stocks

def save_files(company_list, digit_distributions, digit_distributions_perc):
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


def main(config):
    s = Stocks()
    df = pd.read_csv("data/prices.csv")

    company_list, digit_distributions, digit_distributions_perc = [], [], []
    for sym in df.columns[1:]:
        first_digit_cnts, first_digit_cnts_percs = s.get_dist(sym)
        company_list.append(sym)
        digit_distributions.append(first_digit_cnts)
        digit_distributions_perc.append(first_digit_cnts_percs)

    save_files(company_list, digit_distributions, digit_distributions_perc)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    config = parser.parse_args()

    print(config)
    main(config)