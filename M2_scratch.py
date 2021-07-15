# ch7 MGF: sympy
# ch8 joint and conditional distn: simulation, sympy, pacal
# ch9 normal distn and CLT: simulation, scipy.stats, sympy
# ch10 random inference: statkey

# %%
import numpy as np
import scipy.stats as stats
from IPython.display import display
from sympy import *
import pacal as pc
from sympy.stats import Die, E, variance
import pandas as pd

def runner(runs:list=None, q:str=None) -> None:
    """
    Short function to track runs from Statkey.
    Args: 
        runs -> list of run results from statkey
        q -> string question number
    """

    if runs and len(runs) > 0:
        print(f"Q{q}: {len(runs)} run mean = {np.mean(runs):.4f}")
    else:
        print("No data")

theta = symbols("theta")
n = symbols("n")
alpha = symbols("alpha")
i = symbols('i')
x = Function("x")
gamma = Function("Gamma")

#%%
n = 20
lmb_clt = 1
# 3b by CLT
E_Xn = n * lmb_clt
Var_Xn = n * lmb_clt

Z = (a - E_Xn) / (np.sqrt(Var_Xn)/np.sqrt(n))
Pr_Xn = stats.norm.cdf(Z)

print(f"Pr(Xn > 26) by CLT: Z = {Z:.3f}, Pr = {Pr_Xn:.3f}")

# %%
# 4
X = Die("X_i", 6)
n = 720-1
Xn = 300

E_Xn = float(n * E(X))
Var_Xn = float(n * variance(X))

Z = (Xn - E_Xn) / np.sqrt(Var_Xn)
Pr_Xn = stats.norm.cdf(Z)

print(f"E[79 rolls of 6 sided die] = {E_Xn:.3f}")
print(f"Var[79 rolls of 6 sided die] = {Var_Xn:.3f}")
print(f"Pr(Xn < 300) by CLT: Z = {Z:.3f}, Pr = {Pr_Xn:.3f}")
# %%
#6
# A margin of error from 95% CI
ci = (1 - 0.95) / 2  # two tail case
z_star = stats.norm.ppf(1-ci)
p = 0.5
me = 0.06

n = np.ceil((z_star/me)**2 * p*(1-p))

print(f"N 95%CI = {n:.3f}, {z_star:.3f}")

# %%
#7
runner([-0.086-(-0.232), -0.085-(-0.229), -0.083-(-0.230), -0.085-(-0.231)],7)
# %%
#8
runner([0.129*2, 0.125*2, .130*2, 0.122*2],8)
# %%
#9
runner([0.283, 0.277, 0.273, 0.270, 0.278 ],9)Gamma
#%%
#9
runner([0.054, 0.051, 0.054, 0.054],10)
#%%
data = pd.read_csv("final_data/Cars2020.csv")

type = data["Type"]
sedan = sum(data["Type"] == "Sedan")
n = len(type)

print(n, sedan)

prop = sedan / n
print(prop)

runner([0.418-0.273, 0.436-0.264, 0.464-0.236, 0.464-0.236  ],11)
# %%


# 9 with symfit
from symfit import Parameter, Variable, exp, parameters, variables, Fit
from symfit.core.objectives import LogLikelihood

data = np.array([3.2, 3.6, 3.3, 3.5, 3.2, 7.6])

# Define the model
theta = Parameter('theta')
x = Variable('x')
model = ((3**theta)*theta) / x**(theta+1)

# fit
fit = Fit(model, data, objective=LogLikelihood)
fit_result = fit.execute()

print(f"theta mle estimate with symfit: {fit_result.value(theta):.3f}")

# %%
# 1: ans = f
# with pacal from tobor
lmb = 1/2
X = pc.ExponentialDistr(lmb)

W = X**2
W_pdf = W.pdf(2.0)
print(f"W(2.0   ) = {W_pdf:.3f}")

#%%
lmb = 20
EX = lmb
Var_EX = lmb
X = 26

mu = lmb
var = lmb

Pr_X_chernoff = 2*np.exp(-(mu*var)/3)
print(Pr_X_chernoff)

#%%
die = [1,2,3,4,5,6]
X = 130

RUNS = 1000
p_runs = []
total_roll_6 = []

for r in range(RUNS):
    TRIALS = 720
    roll_six = 0
    for trial in range(TRIALS):
        roll = np.random.choice(die)
        if roll == 6:
            roll_six += 1

    # p_roll_six = 1-(roll_six / TRIALS)
    total_roll_6.append(roll_six)
    # p_runs.append(p_roll_six)


result = np.mean((np.array(total_roll_6) < X))
print(result)

mean_p = np.mean(p_runs)
std_p = np.std(p_runs)

# print(f"total roll 6 = {total_roll_6}")
print(f"Mean P(meet) = {mean_p:.3f}")
print(f"STD P(meet) = {std_p:.3f}")

# %%
# 1
# sympy chernoff bound (sharp)

# differentate
# f1 = diff(f, d)
# # equate to zero
# f1_eq = Eq(f1, 0)
# # solve for d
# delta = list(solveset(f1_eq, d, Reals))[0]
# # plug in d and evaluate
# ans = f.subs({d:delta})

# theta = symbols("theta")
# n = symbols("n")
# a = symbols("a")
# t = symbols("t")
# lmb = symbols("lambda")
# # i = symbols('i')
# # x = Function("x")
# # gamma = Function("Gamma")

# f = (exp(lmb*(exp(t)-1))) / exp(t*a)
# display(f)

# f1 = Eq(diff(f, t),0)
# display(f1)

# solve = solve(f1,t)[0]
# display(solve)



# %%
