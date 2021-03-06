# %%
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.proportion import proportion_confint
from IPython import display
import seaborn as sns


# %% 1 (HW9 redo)
# h_null = 50
# h_alt <= 50 --> left tail
# inference on single mean with t-dist
# t = (Xbar - mu_null)/SE
# SE = s / sqrt(n)

data = "./data/SalaryGender.csv"
df = pd.read_csv(data)
age = df["Age"].to_numpy()

df_ = len(age) - 1
Xbar = np.mean(age)
sd = np.std(age)
mu_null = 50
std_err = np.std(age) / np.sqrt(len(age))

t = (Xbar - mu_null) / std_err
pval = stats.t.cdf(t, df_) # cdf for left tail, sf for right
t_sci, pval_sci = stats.ttest_1samp(age, 50)

print(f"manual ttest: {t}, {pval}")
print(f"scipy ttest_1samp: {t_sci}, {pval_sci/2}")
print(f"random ttest: none, 0.019")


# %% 2 (HW9 redo)
# get 90% ci for mean math sat score
# CI = Xbar - tstar * SE <= mu <= Xbar + tstar * SE
# SE = s / sqrt(n)

data = pd.read_csv("./data/StudentSurvey.csv")
sat = data["MathSAT"].to_numpy()

n = len(sat)
df = n - 1
Xbar = np.mean(sat)
sd = np.std(sat)
std_err = sd / np.sqrt(n)
t_star = stats.t.ppf(0.95, df)  # account for 2-tail

ci = [Xbar-t_star*std_err,  Xbar+t_star*std_err]
ci_sci = stats.t.interval(0.90, df=df, loc=Xbar, scale=std_err)

print(Xbar, sd, std_err, t_star)
print(f"manual 90% CI: {ci[1] - ci[0]}")
print(f"scipy 90% CI: {ci_sci[1] - ci_sci[0]}")
print("random 90% CI: 12.0")

# %% 3 sample size
# n for mean = ((z_star * sigma_tilda) / ME)**2
# n for proprtion = (z_star/ME)**2 * p_tilda(1 - p_tilda)

# why p_sample = 0.50?
# for proportions... a p_sample = 0.50 is a local maximum.
# this local maximum will require the largest n to obtain the ME and CI.
p_sample = np.linspace(0.0, 1.0, 11)
p_computed = p_sample*(1-p_sample)
plt.plot(p_sample, p_computed)
plt.show()

# %%
# a
ci = (1 - 0.90) / 2
me = 3.5  # hrs
n_start = 18
Xbar = 124.6
sd = 13.3
z_star = stats.norm.ppf(1-ci)  # need to figure why 0.95
n_a = np.ceil(((z_star * sd) / me)**2)

print(f"A: z_star = {z_star}, n = {n_a}")

# b
me = 0.06
p_sample = 0.5  # guess
n_b = np.ceil((z_star / me)**2 * p_sample*(1 - p_sample))
print(f"B: z_star = {z_star}, n = {n_b}")

# c
me = 0.06
p_sample = 0.25  # from q
n_b = np.ceil((z_star / me)**2 * p_sample*(1 - p_sample))
print(f"C: z_star = {z_star}, n = {n_b}")


# %% 4 (HW9 redo) --> not sure about this one...
# inference on a single proportion with norm dist
# z = (phat-pnull) / SE
# SE = sqrt(p_null * (1 - p_null)/n)
# p_null = 0.30
# H_alt =< 0.30
# p_hat = 0.30

data = "./data/CocaineTreatment.csv"
df = pd.read_csv(data)

placebo = df[df["Drug"] == "Placebo"]
n = len(placebo)
count_no = sum(placebo["Relapse"] == "no")
p_hat = count_no / n
p_null = 0.30
std_err = np.sqrt((p_null * (1 - p_null) / n))

if (n*p_hat >= 10) and (n*(1-p_hat >= 10)):
    print("conditions for normal distn met")
else:
    print("conditions not met... proceed with caution.")

z = (p_hat - p_null) / std_err
pval = stats.norm.cdf(z)
z_sm, pval_sm = proportions_ztest(count=count_no, nobs=n, value=p_null)

# result from theoretical is more conservative
print(f"manual z-test: {z}, {pval}")
print(f"sm proportions_ztest: {z_sm}, {pval_sm}")
print("random ttest: none, 0.100")


# %% 5 (HW9 redo)
# inference two proportions --> p1 - p2 --> 2 tail
# sample stat = phat1 - phat2, sample distn = normal
# z = ((phat1 - phat2) - 0) / SE
# SE = sqrt((pbar(1-pbar)/n1) + (pbar(1-pbar)/n2))
# pbar = count(p1)+count(p2) / trials(p1) + trials(p2)

data = "./data/CocaineTreatment.csv"
df = pd.read_csv(data)

lithium = df[df["Drug"] =="Lithium"]
lithium_count = len(lithium)
lithium_sample = sum(lithium["Relapse"] == "no")
lithium_phat = lithium_sample / lithium_count

placebo = df[df["Drug"] == "Placebo"]
placebo_count = len(placebo)
placebo_sample = sum(placebo["Relapse"] == "no")
placebo_phat = placebo_sample / placebo_count


pbar = (lithium_sample + placebo_sample) / (lithium_count + placebo_count)
std_err = np.sqrt((pbar*(1-pbar))/lithium_count + ((pbar*(1-pbar))/placebo_count))


z = ((lithium_phat - placebo_phat) - 0) / std_err
pval =  stats.distributions.norm.sf(z) * 2  # 2 tail with survival
z_sm, pval_sm = proportions_ztest(count=[lithium_sample, placebo_sample], 
                                  nobs=[lithium_count, placebo_count]
)

print(f"manual z-test: {z}, {pval}")
print(f"sm proportions_ztest: {z_sm}, {pval_sm}")
print("random ttest: none, 0.341")


# %% 6 (HW9 redo)
# 83% CI for differnece in propotions
# (phat1 - phat2) - z_star * SE <= phat1 - phat2 <= (phat1 - phat2) + z_star * SE
# SE = sqrt(phat1(1-phat1)/n1 + phat2(1-phat2)/n2)

data = "./data/CocaineTreatment.csv"
df = pd.read_csv(data)

# desipramine no relapse
desip = df[df["Drug"]=="Desipramine"]
desip_sample = len(desip) 
desip_count = sum(desip["Relapse"] == "no")

# lithium no relapse
lithium = df[df["Drug"]=="Lithium"]
lithium_sample = len(lithium)
lithium_count = sum(lithium["Relapse"] == "no")

lithium_phat = lithium_count / lithium_sample
desip_phat = desip_count / desip_sample
ci_ = 1 - ((1 - 0.83) / 2)
z_star = stats.norm.ppf(ci_)
std_err = np.sqrt((lithium_phat*(1-lithium_phat))/lithium_sample + (desip_phat*(1-desip_phat))/desip_sample)

ci = [(lithium_phat-desip_phat)-z_star*std_err, (lithium_phat-desip_phat)+z_star*std_err]
ci_sm = proportion_confint([lithium_count, desip_count], [lithium_sample, desip_sample], alpha=ci_)

print(ci_)
print(f"manual 83% CI: {ci[1] - ci[0]}")
print(f"sm 83% CI: {ci_sm[1][1] - ci_sm[1][0]}")
print("random 83% CI: 0.29")

# %% 7
# wetsuit matched pairs --> data prep with pandas
# make wetsuit_mod_1 --> difference of means
# make wetsuit_mod2  --> difference of matched pairs


# %% 11 / 12 sample size for one proportion

def n_bulbs(ci, me, p_sample):
    "for proportion: find N required for CI and ME"
    ci_ = 1 - ((1 - ci) / 2)
    z_star = stats.norm.ppf(ci_)
    n = np.ceil((z_star / me)**2 * p_sample*(1 - p_sample))
    print(f"N bulbs for {p_sample} defect proportion: z_star = {z_star}, n = {n}")


ci = 0.90
me = 0.02
p_base = 0.50
p_sample = 0.06

n_bulbs(ci, me, p_base)
n_bulbs(ci, me, p_sample)


# %% 13 sample size for one mean

def n_flights(ci, me, sd_sample):
    "for mean: find N required for CI and ME"
    ci_ = 1 - ((1 - ci) / 2)
    z_star = stats.norm.ppf(ci_)
    n = np.ceil(((z_star * sd_sample) / me)**2)
    print(f"N flights for {ci}% CI and {me} min ME: z_star = {z_star}, n = {n}")


ci = 0.99
me = 3  # min
sd_sample = 9.34  # min

n_flights(ci, me, sd_sample)


# %% 14 / 15 / 16
data = pd.read_csv("./data/ImmuneTea.csv")

tea = data[data["Drink"] == "Tea"].iloc[:,0].to_numpy()
coffee = data[data["Drink"] == "Coffee"].iloc[:,0].to_numpy()

# %%
sns.displot(tea, color='darkcyan', bins=10, kde=True)
plt.title(f"Tea n = {len(tea)}", y=1.015, fontsize=15)
plt.xlabel("InterferonGamma", labelpad=12)
plt.ylabel("Count", labelpad=12)

# %%
sns.displot(coffee, color='crimson', bins=10, kde=True)
plt.title(f"Coffee n = {len(coffee)}", y=1.015, fontsize=15)
plt.xlabel("InterferonGamma", labelpad=12)
plt.ylabel("Count", labelpad=12)

# %%
sns.boxplot(x=tea, color='darkcyan', saturation=0.8)
plt.title(f"Tea n = {len(tea)}", y=1.015)
plt.xlabel("InterferonGamma", labelpad=12)

# %%
sns.boxplot(x=coffee, color='crimson', saturation=0.8)
plt.title(f"Coffee n = {len(coffee)}", y=1.015)
plt.xlabel("InterferonGamma", labelpad=12)

# %%
if (len(tea) >= 30 and len(coffee) >= 30):
    print("conditions met to use normal distn.")
elif len(tea) + len(coffee) >= 30:
    print("conditions met to use normal distn.")
else:
    print("conditions not met... use caution.") 

# %%
# FIXME 1 tail case
# difference of means for InterferonGamma between
# h_null = mean_tea == mean_coffee
# h_alt = mean_tea >= mean_coffee

def diff_mean_t_tests(sample1, sample2):

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


t, pval = diff_mean_t_tests(tea, coffee)
# FIXME 1 tail case
t_sci, pval_sci = stats.ttest_ind(a=tea, b=coffee, equal_var=False, nan_policy="omit", alternative="greater")

print(f"tea = {np.mean(tea)}, {np.std(tea, ddof=1)}")
print(f"coffee = {np.mean(coffee)}, {np.std(coffee, ddof=1)}")
print(f"manual: t-stat = {t}, pval = {pval}")
print(f"scipy: t-stat = {t_sci}, pval = {pval_sci}")
# %%
