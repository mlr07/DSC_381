#%%
from sympy import *
from IPython.display import display
# prob portion

# MGF --> HW6

# chernoff bound --> HW6
# symbols
t = symbols('t', positive=True)
a = symbols('a', positive=True)

# build expression
p1 = exp((t**2/2) - t*a)
p1_alt = (t**2/2) - t*a
display(p1, p1_alt)

# 1st deriv wrt to t, set = 0
p1_min = Eq(diff(p1, t),0).doit()
p1_min_alt = Eq(diff(p1_alt, t),0).doit()
display(p1_min, p1_min_alt)

# solve for t and examine critical value
# note that exponent never goes to zero
# focus on terms outside of exp
# p1_t = solve(p1_min, t)[0]
p1_t_alt = solve(p1_min_alt, t)[0]
display(p1_t_alt) 

#%%
# joint distribution --> HW7
lamb = symbols("lambda", positive=True)
r = symbols("r", positive=True)
x = symbols("x", positive=True)

fy = lamb*exp(-lamb*(r+1)*x)
display(fy)

Fy = integrate(fy, x)
display(Fy)


# CLT --> HW8

# stats portion
# inference --> HW4
# simulation --> HW9
# theoretical distn --> HW10
# chi**2 and ANOVA --> HW11
# MLE --> HW12
# exp families --> HW13

# %%
