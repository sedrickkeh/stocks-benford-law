import os
import argparse
import pandas as pd 

from utils import benford_dist, js


def main(config):
    df = pd.read_csv("output/s&p500_dist_perc.csv")
    constituents = pd.read_csv("data/constituents.csv")
    df = pd.merge(df, constituents, left_on="Stock", right_on="Symbol")

    benford = benford_dist()
    scores = []
    for idx, row in df.iterrows():
        stock = row[0]
        p = list(row[1:10])
        score = js(p, benford)
        scores.append(score)

    df["Score"] = scores
    df.drop(columns=[str(x) for x in range(1, 10)], axis=1, inplace=True)
    df.drop("Stock", axis=1, inplace=True)
    df.to_csv("output/js_scores.csv", index=False)

    df.drop(columns=["Symbol", "Name"], inplace=True)
    df["Score"].fillna(0, inplace=True)

    by_sector = df.groupby(["Sector"]).mean()
    print(by_sector)
    print(df.describe())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    config = parser.parse_args()

    print(config)
    main(config)