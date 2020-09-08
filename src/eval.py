import pandas as pd 
from benford import get_dist, benford_dist, mse

df = pd.read_csv("s&p500_dist_perc.csv")
constituents = pd.read_csv("constituents.csv")
df = pd.merge(df, constituents, left_on="Stock", right_on="Symbol")
df.drop(columns=["Symbol", "Name"], inplace=True)

benford = benford_dist()
scores = []
for idx, row in df.iterrows():
    stock = row[0]
    p = list(row[1:10])
    score = mse(p, benford)
    scores.append(score)

df["Scores"] = scores
df["Scores"].fillna(0, inplace=True)

by_sector = df.groupby(["Sector"]).mean()
print(by_sector)
print(df.describe())