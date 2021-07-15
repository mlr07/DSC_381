#%%
from sympy import *
from IPython.display import display
import numpy as np

#%%
# slide 7 l(theta) for newton raphson
theta = symbols('theta', positive=True)  # toggle
n = symbols('n', positive=True)
i = symbols('i', positive=True)
x = Function('x')
y = Function('y')

L_log = Rational(1,2)*Sum((y(i)-log(theta+x(i)))**2, (i, 1, n))
d_dtheta = diff(L_log, theta)
d2_dtheta2 = diff(d_dtheta, theta)

# %%
pprint(L_log)
pprint(d_dtheta)
pprint(simplify(d_dtheta))
pprint(d2_dtheta2)
pprint(simplify(d2_dtheta2))

#%%
# HW 1.1 
l = Rational(1,2)*Sum((y(i)-exp(theta*x(i)))**2, (i, 1, n))
d_dtheta = diff(l, theta)
d2_dtheta2 = diff(d_dtheta, theta)

pprint(l)
pprint(d_dtheta)
pprint(simplify(d_dtheta))

#%%
pprint(d2_dtheta2)
pprint(simplify(d2_dtheta2))

#%%
# latex(d_dtheta)
latex(d2_dtheta2)

# final check on HW derivatives then move to computing theta hat