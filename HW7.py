# %%
from sympy import *
from IPython.display import Latex, display

# NOTE: figure out rational numbers
# NOTE: figure out how to define symbol types
# NOTE: figure out how to combine latex and sympy expressions

# %%
# 1
# ans = f

# 2A
u = symbols("u")
PDF_a = Integral(1, (u, 1/4, 1/2)) / Integral(1, (u, 1/4, 3/4))
PDF_a.doit()

# 2B
numer = Integral(1, (u, 0, 1/4))
denom = Integral(1, (u, 0, 1/3)) + Integral(1, (u, 2/3, 1))
PDF_b = numer / denom
PDF_b.doit()

# 3
Pr_AB_meet = 1 - ((2*1/2*45*45) / (60*60))
Pr_AB_meet
5/9

# 4a
# ans = 

# 4b
# ans = a or b

# %%
# 5
# ans = a
cdf = Latex(r"$F_y(y) = Pr(Y\leq y) = Pr(F_x(X) \leq y) = y$")
pdf = Latex(r"$f_y(y) = \frac{d}{dy}y$")
y = symbols("y")
ans_a = Eq(Derivative(y), Derivative(y).doit())

display(cdf)
display(pdf)
display(ans_a)

# 6 
# ans = b
