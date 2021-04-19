# %%
import pandas as pd
import numpy as np
import scipy.stats as sp
import statsmodels.stats as sm
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

# BUG: don't think this works in ipython
sns.set(rc={'figure.figsize':(12,10)})

# %%
# curl -o MustangPrice.csv https://www.lock5stat.com/datasets3e/MustangPrice.csv
# 90% CI for single population mean price --> test for conditions

df = pd.read_csv("./data/MustangPrice.csv")
price = df["Price"]

if len(price) >= 30:
    print(f"Conditions for '{price.name}' met. n= {len(price)} >= 30.")

else:
    print(f"Conditions for '{price.name}' not met. n = {len(price)} <= 30.")

print("")

sns.displot(price, color='darkcyan', bins=10, kde=True)
plt.title(f"{price.name} n = {len(price)}", y=1.015, fontsize=15)
plt.xlabel(price.name, labelpad=12)
plt.ylabel("Count", labelpad=12)
plt.show()


# %%
# curl -o CommuteAtlanta.csv https://www.lock5stat.com/datasets3e/CommuteAtlanta.csv
# HT on single mean: Ho = 30min, Ha < 30min

def single_mean_conditions(data, col):
    df = pd.read_csv(data)
    series = df[col]

    if len(series) >= 30:
        print(f"Conditions for '{series.name}' met. n = {len(series)} >= 30.\n")
    else:
        print(f"Conditions for '{series.name}' not met. n = {len(series)} <= 30.\n")

    display(df.describe().T)
    print("")

    sns.displot(series, color='darkcyan', bins=10, kde=True)
    plt.title(f"{series.name} n = {len(series)}", y=1.015, fontsize=15)
    plt.xlabel(series.name, labelpad=12)
    plt.ylabel("Count", labelpad=12)
    plt.show()

data = "./data/CommuteAtlanta.csv"
col = "Time"

single_mean_conditions(data, col)

# %%
df = pd.read_csv("./data/ICUAdmissions.csv")

# 90% CI for difference in two proportions  --> meet conditions?
# proportion of non cancer with infections = non cancer infection/non-cancer
# proportion of cancer with infection = cancer infection/cancer

no_cancer = df[df["Cancer"] == 0]
no_cancer_infect = no_cancer["Infection"] == 1
prop_no_cancer_infect = sum(no_cancer_infect) / len(no_cancer)
print(f"No cancer infected: prop = {prop_no_cancer_infect:.2f}, c = {sum(no_cancer_infect)}, n = {len(no_cancer)}")


cancer = df[df["Cancer"]== 1]
cancer_infect = cancer["Infection"] == 1
prop_cancer_infect = sum(cancer_infect) / len(cancer)
print(f"Cancer infected: prop = {prop_cancer_infect:.2f}, c = {sum(cancer_infect)}, n = {len(cancer)}")


# TODO: make verbose with p1, p2, n1, n2
if (prop_no_cancer_infect*len(no_cancer) >= 10) and ((1-prop_no_cancer_infect)*len(no_cancer) >= 10):
    if (prop_cancer_infect*len(cancer) >= 10) and ((1-prop_cancer_infect)*len(cancer) >= 10):
        print("Both proportions satisfy conditions.")
    else:
        print("One proportion does not satisfy conditions.")
else:
    print("Neither proprotions satisfy conditions.")

# %%

# 90% CI for single population proportion

sample = 200
defective = 12
prop = defective / sample
np = sample * prop
n1_p = sample * (1 - prop)

print(f"Sample = {sample}, c = {defective}, prop = {prop}")
print(f"np = {np} >= 10 and n(1-p) = {n1_p} >= 10")

if np >= 10 and n1_p >=10:
    print("Conditions for single proporiton met.")
    
else:
    print("Conditions for single proporiton NOT met.")


# %%
