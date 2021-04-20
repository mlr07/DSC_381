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
# 1
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
# 2
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
# 3
# 90% CI for difference in two proportions  --> meet conditions?
# proportion of non cancer with infections = non cancer infection/non-cancer
# proportion of cancer with infection = cancer infection/cancer

df = pd.read_csv("./data/ICUAdmissions.csv")

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
# 4,5,6

def single_prop_condition(sample, count, q, p0=None):
    if p0:
        prop = p0
    else:
        prop = count / sample

    n_p = sample * prop
    n1_p = sample * (1 - prop)

    print(f"Q{q}: Check Single Proportion Conditions")
    print(f"Sample = {sample}, c = {count}, prop = {prop}")
    if n_p >= 10 and n1_p >=10:
        print(f"np = {n_p:.2f} >= 10 and n(1-p) = {n1_p:.2f} >= 10")
        print("Conditions for single proporiton met!\n")
    else:
        print(f"np = {n_p:.2f} < 10 and n(1-p) = {n1_p:.2f} < 10")
        print("Conditions for single proporiton NOT met!\n")

# 90% CI for single population proportion
sample, defect = 200, 12
single_prop_condition(sample=sample, count=defect, q="4")

# HT for single proportion: Ho <= 0.06, Ha > 0.06
p0 = 0.06
sample, defect = 200, 14
single_prop_condition(sample=sample, count=defect, q="5", p0=p0)

# HT for a single proportion: H0 <= 0.04, Ha > 0.04
p0 = 0.04
sample, defect = 200, 12
single_prop_condition(sample=sample, count=defect, q="6", p0=p0)

# %%
# 7
# curl -o ExerciseHours.csv https://www.lock5stat.com/datasets3e/ExerciseHours.csv
# HT for difference of means: Ho: mean_m == mean_f, Ha: mean_m != mean_f
# condition for t-dist: each group n >= 30

df = pd.read_csv("./data/ExerciseHours.csv")
display(df["Sex"].value_counts())

men = sum(df["Sex"] == "M")
women = sum(df["Sex"] == "F")

print(f"Men n = {men}, Women n = {women}")

if men >= 30 and women >= 30:
    print("Conditions for difference of means MET")
else:
    print("Conditions for difference of means NOT MET")

# %%
# 8
# curl -o TrafficFlow.csv https://www.lock5stat.com/datasets3e/TrafficFlow.csv
# difference of means with paired data
# condition for t-dist: clt or n >= 30 
df = pd.read_csv("./data/TrafficFlow.csv")

time_diff = df["Difference"]
len_time_diff = len(time_diff)

print(f"Difference in times n = {len_time_diff}")
if len_time_diff >= 30:
    print("Conditions for difference of paried means MET")
else:
    print("Conditions for difference of paried means NOT MET")

sns.displot(time_diff, color='darkcyan', bins=8, kde=True)
plt.title(f"{time_diff.name} n = {len_time_diff}", y=1.015, fontsize=15)
plt.xlabel(time_diff.name, labelpad=12)
plt.ylabel("Count", labelpad=12)
plt.show()

# %%
# 9
# test for association between categories
# condition for chi**2: each category expected >= 5 
# from statkey --> there is an equation

desip = {"no":8, "yes":16}
lith = {"no":8, "yes":16}
placebo = {"no":8, "yes":16}
res = []
for i in [desip, lith, placebo]:
    for k,v in i.items():
        if v >= 5:
            res.append(True)
        else:
            res.append(False)
if all(res) == True:
    print("Conditions for Chi**2 association test MET")
else:
    print("Conditions for Chi**2 association test NOT MET")

# %%
# 10
# curl -o RestaurantTips.csv https://www.lock5stat.com/datasets3e/RestaurantTips.csv
# test for a difference of means between groups ANOVA
# condition: clt n >= 30 for each group and SDmax / SDmin < 2

df = pd.read_csv("./data/RestaurantTips.csv")
server_counts = dict(df["Server"].value_counts())
server_counts = {k:v for k,v in sorted(server_counts.items(), key=lambda item: item[0])}
res = []

for k,v in server_counts.items():
    if v >= 30:
        res.append(True)
    else:
        res.append(False)
    server = df[df["Server"] == k]
    pct_tip_std[k] = server["PctTip"].std()

min_std = min(pct_tip_std.values())
max_std = max(pct_tip_std.values())

if all(res) == True:
    print("Count conditions for ANOVA MET")
else:
    print("Count conditions for ANOVA NOT MET")

if max_std / min_std < 2.0:
    print("STD conditions for ANOVE MET")
else:
    print("STD conditions for ANOVA NOT MET")

# %%
# 11
# curl -o FootballBrain.csv https://www.lock5stat.com/datasets3e/FootballBrain.csv
# test for difference of mean between groups ANOVA
# condition: clt n >= 30 for each group and SDmax / SDmin < 2
# Ho: mean1 == mean2 == mean3, Ha: one pair of means !=
# comparative box plots
# ANOVA for diff means: F-stat = 2.651, n = 44, df: groups = 1, error = 42, total = 43
# 1-tail test: pval = 0.115, alpha = 0.05 --> do not reject null
# Difference of means: x1 - x2 = 13.05
# 2-tail test: pval = 0.055, alpha = 0.05 --> do not reject null

df = pd.read_csv("./data/FootballBrain.csv")
display(df.info())

# %%
sns.catplot(x="Group", y="Hipp", kind="violin", inner="stick", data=df)


# %%
sns.catplot(x="Group", y="Cogniton", kind="violin", inner="stick", data=df)

# %%
cognit = df[df['Cogniton'].notnull()] 
cognit_counts = dict(cognit["Group"].value_counts())

res = []
cognit_std = {}
for k,v in cognit_counts.items():
    if v >= 30:
        res.append(True)
    else:
        res.append(False)
    _ = cognit[cognit["Group"] == k]
    hipp_std[k] = _["Cogniton"].std()

min_std = min(hipp_std.values())
max_std = max(hipp_std.values())
condit_std = max_std / min_std 

if all(res) == True:
    print("Count conditions for ANOVA MET")
else:
    print("Count conditions for ANOVA NOT MET")

if condit_std < 2.0:
    print("STD conditions for ANOVA MET")
else:
    print("STD conditions for ANOVA NOT MET")


# %%
# 12

# %%
# 13
# Association between categories --> chi**2
# condition for chi**2: each category expected >= 5 
# chi**2-stat = 8.592
# right 1-tail test: pval = 0.066, alpha = 0.10
# expected counts all >= 5 except Thursday

