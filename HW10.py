# %%
import pandas as pd
import numpy as np
import scipy.stats as stats

# %%
# 1 (HW9 redo)
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
pval = stats.t.cdf(t, df_) # cdf for left tail
t_sci, pval_sci = stats.ttest_1samp(age, 50)

print(f"manual ttest: {t}, {pval}")
print(f"scipy ttest_1samp: {t_sci}, {pval_sci/2}")
print(f"random ttest: none, 0.019")


#%%
# 2 (HW9 redo)
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
t_star = stats.t.ppf(0.90, df)

# THANKS
ci = [Xbar-t_star*std_err,  Xbar+t_star*std_err]
ci_sci = stats.t.interval(0.90, df=df, loc=Xbar, scale=std_err)

print(df, Xbar, sd, std_err)
print(f"manual 90% CI: {ci[1] - ci[0]}")
print(f"scipy 90% CI: {ci_sci[1] - ci_sci[0]}")
print("random 90% CI: 12.0")

#%%





#%%
# 7
# wetsuit matched pairs --> data prep with pandas
# make wetsuit_mod_1 --> difference of means
# make wetsuit_mod2  --> difference of matched pairs
# %%
