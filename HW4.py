# HW4 Q10

import pandas as pd

data = "data/StudentSurvey.csv"
df_filled = pd.read_csv(data).fillna("none")

n = len(df_filled)
X = df_filled["Year"].value_counts()[0]
p_hat = X / n

print(f"population n = {n}")
print(f"sample X = {X}")
print(f"p hat = {p_hat:.2f}")