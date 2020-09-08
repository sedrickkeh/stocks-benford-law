import pandas as pd 
from benford import get_dist, benford_dist, mse

df = pd.read_csv("s&p500_dist_perc.csv")
constituents = pd.read_csv("constituents.csv")
df = pd.merge(df, constituents, left_on="Stock", right_on="Symbol")

benford = benford_dist()
scores = []
for idx, row in df.iterrows():
    stock = row[0]
    p = list(row[1:10])
    score = mse(p, benford)
    scores.append(score)

df["Score"] = scores
df.drop(columns=[str(x) for x in range(1, 10)], axis=1, inplace=True)
df.drop("Stock", axis=1, inplace=True)
df.to_csv("mse_scores.csv", index=False)

