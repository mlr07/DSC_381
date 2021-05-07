#%%
from sympy import *
from IPython.display import display
import numpy as np

#%%
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
y = symbols("y", positive=True)
s, t = symbols("s t")


fy = lamb*exp(-lamb*(r+1)*x)
display(fy)

Fy = integrate(fy, x)
display(Fy)

r_ = Eq((1-y)/y, r)
display(r_)

y_ = solve(r_, r+1)[0]
display(y_)

# Q4 1a
F_x1_x2 = lamb*exp(-lamb*s)
display(F_x1_x2)

# add bound for s
F_x1_x2_ = integrate(F_x1_x2, (x, 0, s))
display(F_x1_x2_)

# eval F(x1, x2) with lambda = 2.0, s = 3.0
result = 2.0*3.0*np.exp(-2.0*3.0)
display(result)

# Q4 1b
F_t2_x3 = exp(-lamb*(s-t))*lamb**2*t*exp(-lamb*t)
display(F_t2_x3)

# add bound for s
F_t2_x3 = integrate(F_t2_x3, (t, 0, s))
display(F_t2_x3)

result = ((2.0*3.0)**2)/2*np.exp(-2.0*3.0)
display(result)



# CLT --> HW8

# stats portion
# inference --> HW4
# simulation --> HW9
# theoretical distn --> HW10
# chi**2 and ANOVA --> HW11
# MLE --> HW12
# exp families --> HW13

# %%
