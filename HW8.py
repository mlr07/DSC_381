#%%
import numpy as np
import scipy.stats as st
from sympy.stats import Die, E, variance

# 1 proof

# 2
n = 100
mu_Xi = 5
sigma_Xi = 5**2
X = 525

# mean and var for sum of Xi --> Xn
E_Xn = n * mu_Xi
Var_Xn = n * sigma_Xi

# get Z and normal dist'n prob
Z = (X - E_Xn) / np.sqrt(Var_Xn)
Pr_Xn = 1 - st.norm.cdf(Z)

print(f"Pr(Xn > 525): Z = {Z:.3f}, Pr = {Pr_Xn:.3f}")

# 3a by Markov
n = 20
lamb = 1
X = 15

E_Xn = n * lamb
Pr_Xn = E_Xn / X

print(f"Pr(Xn > 15) by Markov: {Pr_Xn:.2f}")

# 3b by CLT
E_Xn = n * lamb
Var_Xn = (n * lamb)

Z = (X - E_Xn) / np.sqrt(Var_Xn)
Pr_Xn = 1 - st.norm.cdf(Z)

print(f"Pr(Xn > 15) by CLT: Z = {Z:.3f}, Pr = {Pr_Xn:.3f}")

# 4
X = Die("X_i", 6)
n = 80-1
Xn = 300

E_Xn = float(n * E(X))
Var_Xn = float(n * variance(X))

Z = (Xn - E_Xn) / np.sqrt(Var_Xn)
Pr_Xn = st.norm.cdf(Z)

print(f"E[79 rolls of 6 sided die] = {E_Xn:.3f}")
print(f"Var[79 rolls of 6 sided die] = {Var_Xn:.3f}")
print(f"Pr(Xn < 300) by CLT: Z = {Z:.3f}, Pr = {Pr_Xn:.3f}")

# %%
