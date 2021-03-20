# %%
from sympy import *
# NOTE: figure out rational numbers

# %%
# 2A
u = symbols("u")
PDF_a = Integral(1, (u, 1/4, 1/2)) / Integral(1, (u, 1/4, 3/4))
PDF_a.doit()

# %%
# 2B
numer = Integral(1, (u, 0, 1/4))
denom = Integral(1, (u, 0, 1/3)) + Integral(1, (u, 2/3, 1))
PDF_b = numer / denom
PDF_b.doit()