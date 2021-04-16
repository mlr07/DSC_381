# %%
import numpy as np
import pandas as pd
import scipy.stats as stats
from statistics import mean


def runner(runs:list=None, q:str=None) -> None:
    """
    Short function to track runs from Statkey.
    Args: 
        runs -> list of run results from statkey
        q -> string question number
    """

    if runs and len(runs) > 0:
        print(f"Q{q}: {len(runs)} run mean = {mean(runs):.3f}")
    else:
        print("No data")


def n_bulbs(ci, me, p_sample):
    "for proportion: find N required for CI and ME"
    ci_ = 1 - ((1 - ci) / 2)
    z_star = stats.norm.ppf(ci_)
    n = np.ceil((z_star / me)**2 * p_sample*(1 - p_sample))
    print(f"N bulbs for {p_sample} defect proportion: z_star = {z_star}, n = {n}")


def n_flights(ci, me, sd_sample):
    "for mean: find N required for CI and ME"
    ci_ = 1 - ((1 - ci) / 2)
    z_star = stats.norm.ppf(ci_)
    n = np.ceil(((z_star * sd_sample) / me)**2)
    print(f"N flights for {ci}% CI and {me} min ME: z_star = {z_star}, n = {n}")


def diff_mean_t_tests(sample1, sample2):
    """run difference mean t-test"""
    X_bar1 = np.mean(sample1)
    sd1 = np.std(sample1, ddof=1)
    n1 = len(sample1)

    X_bar2 = np.mean(sample2)
    sd2 = np.std(sample2, ddof=1)
    n2 = len(sample2)

    df = n1 + n2 - 2

    std_err = np.sqrt((sd1**2/n1) + (sd2**2/n2))
    t = ((X_bar1 - X_bar2) - 0) / std_err
    pval = stats.t.sf(t, df=df) 
    return t, pval

# %%
runner([28.995-24.514, 28.959-24.546, 29.043-24.534], "1")

# %%
data = pd.read_csv("./data/ICUAdmissions.csv")

women = data[data["Sex"] == 1]
men = data[data["Sex"] == 0]

women_age = women["Age"].to_numpy()
men_age = men["Age"].to_numpy()

t, pval = diff_mean_t_tests(women_age, men_age)
t_sci, pval_sci = stats.ttest_ind(a=women_age, b=men_age, equal_var=False, nan_policy="omit", alternative="greater")

print(f"women = {np.mean(women_age)}, {np.std(women_age, ddof=1)}")
print(f"men = {np.mean(men_age)}, {np.std(women_age, ddof=1)}")
print(f"manual: t-stat = {t}, pval = {pval}")
print(f"scipy: t-stat = {t_sci}, pval = {pval_sci}")

# %%
sample = len(women["Status"])
count = sum(women["Status"]==0)

print(sample)
print(count)
print(count/sample)
