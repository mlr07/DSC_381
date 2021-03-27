# %%
import numpy as np
import pacal as pc
from sympy import symbols, Integral, Derivative, Eq
from IPython.display import Latex, display

# NOTE figure out rational numbers
# NOTE figure out how to define symbol types
# NOTE figure out how to combine latex and sympy expressions

# %%

# 1: ans = f
# with pacal from tobor
X = pc.UniformDistr(0,1)
Y = pc.UniformDistr(0,1)
W = X-Y
W_pdf = W.pdf(-0.2)
print(f"W(-0.2) = {W_pdf:.3f}")

# 2A
u = symbols("u")
PDF_a = Integral(1, (u, 1/4, 1/2)) / Integral(1, (u, 1/4, 3/4))
print(PDF_a.doit())

# 2B
numer = Integral(1, (u, 0, 1/4))
denom = Integral(1, (u, 0, 1/3)) + Integral(1, (u, 2/3, 1))
PDF_b = numer / denom
print(PDF_b.doit())

# %%
# 3: ans = b
# analytical solution derived by hand
Pr_AB_meet = 1 - ((2*1/2*45*45) / (60*60))
print(Pr_AB_meet)

# simulation (from mogwai)
RUNS = 10
p_runs = []

for r in range(RUNS):
    TRIALS = 100000
    meet_count = 0
    for trial in range(TRIALS):
        time_a = np.random.uniform(0,60)
        time_b = np.random.uniform(0,60)
        diff = np.abs(time_a - time_b)
        if diff <= 15:
            meet_count += 1

        p_meet = meet_count / TRIALS

    p_runs.append(p_meet)

mean_p = np.mean(p_runs)
std_p = np.std(p_runs)
print(f"Mean P(meet) = {mean_p:.3f}")
print(f"STD P(meet) = {std_p:.3f}")

# %%
# print(f"Met {meet_count} times out of {NUM_TRIALS} trials")
# print(f"P(meeting)={p_meet:.3f}")

# 4a: ans = c, proof

# 4b: ans = d, proof

# 5: ans = a, proof
cdf = Latex(r"$F_y(y) = Pr(Y\leq y) = Pr(F_x(X) \leq y) = y$")
pdf = Latex(r"$f_y(y) = \frac{d}{dy}y$")
y = symbols("y")
ans_a = Eq(Derivative(y), Derivative(y).doit())

display(cdf)
display(pdf)
display(ans_a)

# 6: ans = b, proof

# %%
