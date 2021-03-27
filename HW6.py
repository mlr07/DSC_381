# NOTE: 
# the sympy method gives the sharpest chernoff bound 
# latex equation print needs ipython  
# think of some tests for timer class

from timer import Timer
import numpy as np
import sympy as sp
from sympy.abc import p,t,n,a
from sympy import *


# 1 
# manual chernoff bound (loose)
n = 100
a = 55
p = 0.5

mu = n*p
delta = (a/mu)-1
Pr_X_chernoff = np.exp(-((delta**2)/(2+delta)*mu))

print(f"mu: {mu}")
print(f"delta: {delta:.2f}")
print(f"Pr_X_chernoff: {Pr_X_chernoff:.3f}")


# 1
# sympy chernoff bound (sharp)
n = 100
a = 55
p = .5
q = 1-p
d = symbols(('d'))
f = ((q+p*exp(d))**n) * (exp(-d*a)) 

# differentate
f1 = diff(f, d)
# equate to zero
f1_eq = Eq(f1, 0)
# solve for d
delta = list(solveset(f1_eq, d, Reals))[0]
# plug in d and evaluate
ans = f.subs({d:delta})

@Timer(name="decorator", text="Total time: {:0.4f} seconds")
def chernoff_min(f):   
    f1 = sp.diff(f, d)
    f1_eq = sp.Eq(f1, 0)
    chb = list(sp.solveset(f1_eq, d, sp.Reals))
    delta = chb[0]
    ans = f.subs({d:delta})
    print(f"Chernoff Min: {ans}")


chernoff_min(f)


